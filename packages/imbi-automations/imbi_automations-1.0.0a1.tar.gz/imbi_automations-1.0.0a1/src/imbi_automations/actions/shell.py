"""Shell command execution action with templating and environment support.

Executes shell commands with Jinja2 template variable substitution, working
directory management, and proper async subprocess handling for workflow
automation.
"""

import asyncio
import shlex
import subprocess

from imbi_automations import mixins, models, prompts, utils


class ShellAction(mixins.WorkflowLoggerMixin):
    """Executes shell commands with Jinja2 template variable substitution.

    Provides async subprocess execution with working directory management and
    optional error handling.
    """

    def __init__(
        self,
        configuration: models.Configuration,
        context: models.WorkflowContext,
        verbose: bool,
    ) -> None:
        super().__init__(verbose)
        self._set_workflow_logger(context.workflow)
        self.configuration = configuration
        self.context = context

    async def execute(self, action: models.WorkflowShellAction) -> None:
        """Execute a shell command with optional template rendering.

        Args:
            action: Shell action containing the command to execute

        Raises:
            subprocess.CalledProcessError: If command execution fails
            ValueError: If cmd syntax is invalid or template rendering fails

        """
        # Render command if it contains templating
        command_str = self._render_command(action.command, self.context)

        self.logger.debug('Executing shell command: %s', command_str)

        # Parse command string into arguments using shell-like parsing
        try:
            command_args = shlex.split(command_str)
        except ValueError as exc:
            raise ValueError(f'Invalid shell command syntax: {exc}') from exc

        if not command_args:
            raise ValueError('Empty command after template rendering')

        # Set working directory using resolve_path
        cwd = utils.resolve_path(self.context, action.working_directory)

        try:
            # Execute command asynchronously
            process = await asyncio.create_subprocess_exec(
                *command_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=cwd,
            )

            stdout, stderr = await process.communicate()

            # Decode output
            stdout_str = stdout.decode('utf-8') if stdout else ''
            stderr_str = stderr.decode('utf-8') if stderr else ''

            self.logger.debug(
                'Shell command completed with exit code %d', process.returncode
            )

            if stdout_str:
                self.logger.debug('Command stdout: %s', stdout_str)
            if stderr_str:
                self.logger.debug('Command stderr: %s', stderr_str)

            if process.returncode != 0:
                error_output = stderr_str if stderr_str else stdout_str
                if action.ignore_errors:
                    self.logger.info(
                        'Shell command failed with exit code %d (ignored)\n'
                        'Command: %s\nOutput: %s',
                        process.returncode,
                        command_str,
                        error_output,
                    )
                else:
                    self.logger.error(
                        'Shell command failed with exit code %d\n'
                        'Command: %s\nOutput: %s',
                        process.returncode,
                        command_str,
                        error_output,
                    )
                    raise subprocess.CalledProcessError(
                        process.returncode,
                        command_args,
                        output=stdout,
                        stderr=stderr,
                    )

        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f'Command not found: {command_args[0]}'
            ) from exc

    def _render_command(
        self, command: str, context: models.WorkflowContext
    ) -> str:
        """Render command template if it contains Jinja2 syntax.

        Args:
            command: Command string that may contain templates
            context: Workflow context for template variables

        Returns:
            Rendered command string

        """
        if prompts.has_template_syntax(command):
            self.logger.debug('Rendering templated command: %s', command)
            return prompts.render(context, command, **context.model_dump())
        return command
