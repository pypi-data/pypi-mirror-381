"""Command-line interface for Imbi Automations.

Provides the main entry point for the imbi-automations CLI tool, handling
argument parsing, configuration loading, colored logging setup, and
orchestrating workflow execution through the controller.
"""

import argparse
import asyncio
import logging
import pathlib
import sys
import tomllib
import typing

import colorlog
import pydantic

from imbi_automations import controller, models, utils, version

LOGGER = logging.getLogger(__name__)


def configure_logging(debug: bool) -> None:
    """Configure colored logging for CLI applications."""
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - '
            '%(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        )
    )

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO, handlers=[handler]
    )

    for logger_name in ('anthropic', 'httpcore', 'httpx'):
        logging.getLogger(logger_name).setLevel(logging.WARNING)


def load_configuration(config_file: typing.TextIO) -> models.Configuration:
    """Load configuration from config file

    Args:
        config_file: Path to the main configuration file or file-like object

    Returns:
        Configuration object with merged data

    Raises:
        tomllib.TOMLDecodeError: If TOML parsing fails
        pydantic.ValidationError: If configuration validation fails

    """
    return models.Configuration.model_validate(utils.load_toml(config_file))


def workflow(path: str) -> models.Workflow:
    """Argument type for parsing a workflow and its configuration."""
    path_obj = pathlib.Path(path)
    if not path_obj.is_dir():
        raise argparse.ArgumentTypeError(
            f'Workflow path is not a directory: {path}'
        )

    config_file = path_obj / 'config.toml'
    if not config_file.is_file():
        raise argparse.ArgumentTypeError(
            f'Missing config.toml in workflow directory: {path}\n'
            f'Expected: {config_file}'
        )
    try:
        with path_obj.joinpath('config.toml').open('r') as f:
            config_data = utils.load_toml(f)

        configuration = models.WorkflowConfiguration.model_validate(
            config_data
        )

        return models.Workflow(path=path_obj, configuration=configuration)
    except OSError as exc:
        raise argparse.ArgumentTypeError(
            f'Failed to read config.toml in workflow directory: {path}\n'
            f'Error: {exc}'
        ) from exc
    except (tomllib.TOMLDecodeError, pydantic.ValidationError) as exc:
        # Handle TOML parsing or Pydantic validation errors
        error_msg = str(exc)
        if 'validation error' in error_msg.lower():
            # Extract the most relevant part of Pydantic validation errors
            lines = error_msg.split('\n')
            main_error = next(
                (line for line in lines if 'Input should be' in line),
                error_msg,
            )
            raise argparse.ArgumentTypeError(
                f'Invalid workflow configuration in {path}/config.toml:\n'
                f'{main_error}'
            ) from exc
        else:
            raise argparse.ArgumentTypeError(
                f'Failed to parse workflow config in {path}/config.toml:\n'
                f'{error_msg}'
            ) from exc


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for imbi-automations.

    Args:
        args: List of command-line arguments. Defaults to sys.argv if None.

    Returns:
        Parsed argument namespace with configuration, workflow, and
        targeting options.
    """
    parser = argparse.ArgumentParser(
        description='Imbi Automations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.register('type', 'workflow', workflow)
    parser.add_argument(
        'config',
        type=argparse.FileType('r'),
        metavar='CONFIG',
        help='Configuration file',
        nargs=1,
    )
    parser.add_argument(
        'workflow',
        metavar='WORKFLOW',
        type='workflow',
        help='Path to the directory containing the workflow to run',
    )

    # Target argument group - specify how to target repositories
    target_group = parser.add_mutually_exclusive_group(required=True)
    target_group.add_argument(
        '--project-id',
        type=int,
        metavar='ID',
        help='Process a single project by Project ID',
    )
    target_group.add_argument(
        '--project-type',
        metavar='SLUG',
        help='Process all projects of a specific type slug',
    )
    target_group.add_argument(
        '--all-projects', action='store_true', help='Process all projects'
    )
    target_group.add_argument(
        '--github-repository',
        metavar='URL',
        help='Process a single GitHub repository by URL',
    )
    target_group.add_argument(
        '--github-organization',
        metavar='ORG',
        help='Process all repositories in a GitHub organization',
    )
    target_group.add_argument(
        '--all-github-repositories',
        action='store_true',
        help='Process all GitHub repositories across all organizations',
    )
    target_group.add_argument(
        '--gitlab-repository',
        metavar='URL',
        help='Process a single GitLab repository by URL',
    )
    target_group.add_argument(
        '--gitlab-group',
        metavar='GROUP',
        help='Recursively process all repositories in a GitLab group',
    )
    target_group.add_argument(
        '--all-gitlab-repositories',
        action='store_true',
        help='Process all GitLab repositories across all organizations',
    )

    parser.add_argument(
        '--start-from-project',
        metavar='ID_OR_SLUG',
        help='When processing multiple projects, skip all projects up to '
        'and including this project (accepts project ID or slug)',
    )

    parser.add_argument(
        '--max-concurrency',
        type=int,
        default=1,
        help='How many concurrent tasks to run at a time',
    )

    parser.add_argument(
        '--exit-on-error',
        action='store_true',
        help='Exit immediately when any action fails '
        '(default: continue with other projects)',
    )
    parser.add_argument(
        '--preserve-on-error',
        action='store_true',
        help='Preserve working directory on error for debugging '
        '(saved to error-dir/<workflow>/<project>-<timestamp>)',
    )
    parser.add_argument(
        '--error-dir',
        type=pathlib.Path,
        default=pathlib.Path('./errors'),
        help='Directory to save error states when --preserve-on-error is used',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Show action start/end INFO messages',
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging (shows all debug messages)',
    )
    parser.add_argument('-V', '--version', action='version', version=version)
    return parser.parse_args(args)


def main() -> None:
    """Main entry point for imbi-automations CLI.

    Parses arguments, loads configuration, validates workflow requirements,
    and executes the automation controller with proper error handling.
    """
    args = parse_args()
    configure_logging(args.debug)

    config = load_configuration(args.config[0])
    args.config[0].close()

    # Override config with CLI args for error preservation
    if args.preserve_on_error:
        config.preserve_on_error = True
    if args.error_dir:
        config.error_dir = args.error_dir

    LOGGER.info('Imbi Automations v%s starting', version)
    try:
        automation_controller = controller.Automation(
            args=args, configuration=config, workflow=args.workflow
        )
    except RuntimeError as err:
        sys.stderr.write(f'ERROR: {err}\n')
        sys.exit(1)
    try:
        success = asyncio.run(automation_controller.run())
    except KeyboardInterrupt:
        LOGGER.info('Interrupted, exiting')
        sys.exit(2)
    except RuntimeError as err:
        sys.stderr.write(f'Error running automation: {err}\n')
        sys.exit(3)
    if not success:
        sys.exit(5)
