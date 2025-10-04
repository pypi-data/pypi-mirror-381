"""Utility functions for configuration, directory, and URL management.

Provides helper functions for loading TOML configuration files, creating
directories, masking passwords in URLs, and other common utilities used
throughout the codebase.
"""

import json
import logging
import pathlib
import re
import tomllib
import typing

import pydantic
import yarl

from imbi_automations import models

LOGGER = logging.getLogger(__name__)


def copy(source: pathlib.Path, destination: pathlib.Path) -> None:
    """Copy a file from source to destination."""
    LOGGER.debug('Copying %s to %s', source, destination)
    destination.write_bytes(source.read_bytes())


def compare_semver_with_build_numbers(
    current_version: str, target_version: str
) -> bool:
    """Compare versions including build numbers.

    Handles semantic versions with optional build numbers in the format:
    "major.minor.patch" or "major.minor.patch-build"

    Args:
        current_version: Current version (e.g., "3.9.18-0")
        target_version: Target version (e.g., "3.9.18-4")

    Returns:
        True if current_version is older than target_version

    Examples:
        compare_semver_with_build_numbers("3.9.18-0", "3.9.18-4") → True
        compare_semver_with_build_numbers("3.9.17-4", "3.9.18-0") → True
        compare_semver_with_build_numbers("3.9.18-4", "3.9.18-0") → False

    """
    import semver

    # Split versions into semantic version and build number
    if '-' in current_version:
        current_sem, current_build_str = current_version.rsplit('-', 1)
        try:
            current_build = int(current_build_str)
        except ValueError:
            current_build = 0
    else:
        current_sem = current_version
        current_build = 0

    if '-' in target_version:
        target_sem, target_build_str = target_version.rsplit('-', 1)
        try:
            target_build = int(target_build_str)
        except ValueError:
            target_build = 0
    else:
        target_sem = target_version
        target_build = 0

    # Compare semantic versions first
    current_version_obj = semver.Version.parse(current_sem)
    target_version_obj = semver.Version.parse(target_sem)
    sem_comparison = current_version_obj.compare(target_version_obj)

    if sem_comparison < 0:
        # Current semantic version is older
        return True
    elif sem_comparison > 0:
        # Current semantic version is newer
        return False
    else:
        # Semantic versions are equal, compare build numbers
        return current_build < target_build


def append_file(file: str, value: str) -> str:
    """Append a value to a file.

    Args:
        file: Path to the file to append to
        value: Content to append to the file

    Returns:
        Status string: 'success' or 'failed'

    """
    try:
        file_path = pathlib.Path(file)

        # Create parent directory if it doesn't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Append the value to the file
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(value)

        LOGGER.debug('Successfully appended to file: %s', file)
        return 'success'

    except (OSError, UnicodeDecodeError) as exc:
        LOGGER.error('Failed to append to file %s: %s', file, exc)
        return 'failed'


def resolve_path(
    context: models.WorkflowContext, path: models.ResourceUrl | None
) -> pathlib.Path:
    """Resolve a path relative to the workflow context working directory."""
    if path is None:
        raise ValueError('Path cannot be None')
    path_str = str(path)
    if not isinstance(path_str, str):
        raise TypeError(
            f'str(path) returned {type(path_str)}, expected str. '
            f'path type: {type(path)}, path value: {path!r}'
        )
    uri = yarl.URL(path_str)

    # Handle yarl.URL parsing: scheme://path parses as host, not path
    # When we have a host (e.g., repository://file.txt), yarl treats
    # "file.txt" as the host, not the path. We need to reconstruct the
    # path component from both host and path.
    if uri.host:
        # Use pathlib to ensure proper path separator when combining
        path_component = str(pathlib.Path(uri.host) / uri.path.lstrip('/'))
    else:
        path_component = uri.path.lstrip('/')

    match uri.scheme:
        case 'extracted':
            return context.working_directory / str(uri.scheme) / path_component
        case 'repository':
            return context.working_directory / str(uri.scheme) / path_component
        case 'workflow':
            return context.working_directory / str(uri.scheme) / path_component
        case 'file':
            return context.working_directory / path_component
        case '':
            return context.working_directory / path_component
        case _:
            raise RuntimeError(f'Invalid path scheme: {uri.scheme}')


def sanitize(url: str | pydantic.AnyUrl) -> str:
    """Mask passwords in URLs for security.

    Args:
        url: Input string that may contain URLs with passwords

    Returns:
        Text with passwords in URLs replaced with asterisks

    """
    pattern = re.compile(r'(\w+?://[^:@]+:)([^@]+)(@)')
    return pattern.sub(r'\1******\3', str(url))


def load_toml(toml_file: typing.TextIO) -> dict:
    """Load TOML data from a file-like object

    Args:
        toml_file: The file-like object to load as TOML

    Raises:
        tomllib.TOMLDecodeError: If TOML parsing fails

    """
    return tomllib.loads(toml_file.read())


def extract_image_from_dockerfile(
    context: models.WorkflowContext, path: pathlib.Path
) -> str | None:
    """Extract the Docker image name from a Dockerfile in the workflow context.

    Args:
        context: Workflow context containing working directory
        path: Path to the Dockerfile relative to working directory

    Returns:
        Docker image name from FROM instruction, or error string if not found

    """
    LOGGER.debug('Extracting Docker image from %s', path)
    dockerfile = context.working_directory / path
    if not dockerfile.exists():
        LOGGER.error('Dockerfile does not exist at %s', path)
        return 'ERROR: file_not_found'

    try:
        content = dockerfile.read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError) as exc:
        LOGGER.error('Failed to read Dockerfile %s: %s', path, exc)
        return f'ERROR: {exc}'

    for line_num, line in enumerate(content.splitlines(), 1):
        line = line.strip()
        if line.upper().startswith('FROM '):
            image_spec = line[5:].strip()
            if ' AS ' in image_spec.upper():
                image_spec = image_spec.split(' AS ')[0].strip()
            if '#' in image_spec:  # Remove any trailing comments
                image_spec = image_spec.split('#')[0].strip()
            if image_spec:
                LOGGER.debug(
                    'Found Docker image "%s" at line %d in %s',
                    image_spec,
                    line_num,
                    path,
                )
                return image_spec

    LOGGER.warning('No FROM instruction found in Dockerfile %s', path)
    return 'ERROR: FROM not found'


def extract_json(response: str) -> dict[str, typing.Any]:
    """Extract JSON from Claude Code response text."""
    # Try parsing as-is first
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    # Find JSON in code blocks
    patterns = [
        r'```json\s*\n(.*?)\n```',  # JSON code block
        r'```\s*\n(.*?)\n```',  # Generic code block
        r'(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})',  # Raw JSON object
    ]

    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue

    # Last resort: find last JSON-like structure
    try:
        start = response.rfind('{"')
        end = response.rfind('"}') + 1
        if 0 <= start < end:
            return json.loads(response[start:end])
    except json.JSONDecodeError:
        pass

    raise ValueError(f'No valid JSON found in response: {response[:200]}...')
