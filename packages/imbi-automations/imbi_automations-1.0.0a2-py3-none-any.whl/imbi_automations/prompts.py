"""Jinja2 template rendering for prompts and dynamic content generation.

Provides template rendering functionality for Claude Code prompts, pull request
messages, commit messages, and other dynamic content using Jinja2 with full
workflow context support.
"""

import logging
import pathlib
import typing

import jinja2
import pydantic

from imbi_automations import models, utils


def render(
    context: models.WorkflowContext | None = None,
    source: models.ResourceUrl | pathlib.Path | str | None = None,
    **kwargs: typing.Any,
) -> str | bytes:
    """Render a Jinja2 template with workflow context and variables.

    Args:
        context: Workflow context for global variables and path resolution.
        source: Template source as URL, path, or string content.
        **kwargs: Additional variables to pass to template rendering.

    Returns:
        Rendered template as string or bytes.

    Raises:
        ValueError: If source is not provided.
    """
    if not source:
        raise ValueError('source is required')
    elif isinstance(source, pydantic.AnyUrl):
        source = utils.resolve_path(context, source)

    env = jinja2.Environment(
        autoescape=False,  # noqa: S701
        undefined=jinja2.StrictUndefined,
    )
    if context:
        env.globals['extract_image_from_dockerfile'] = (
            lambda dockerfile: utils.extract_image_from_dockerfile(
                context, dockerfile
            )
        )
    if isinstance(source, pathlib.Path):
        source = source.read_text(encoding='utf-8')
    template = env.from_string(source)
    return template.render(kwargs)


def render_file(
    context: models.WorkflowContext,
    source: pathlib.Path,
    destination: pathlib.Path,
    **kwargs: typing.Any,
) -> None:
    """Render a file from source to destination."""
    logging.info('Rendering %s to %s', source, destination)
    destination.write_text(render(context, source, **kwargs), encoding='utf-8')


def has_template_syntax(value: str) -> bool:
    """Check if value contains Jinja2 templating syntax."""
    template_patterns = [
        '{{',  # Variable substitution
        '{%',  # Control structures
        '{#',  # Comments
    ]
    return any(pattern in value for pattern in template_patterns)
