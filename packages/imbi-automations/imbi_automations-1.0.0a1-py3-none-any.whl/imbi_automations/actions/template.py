"""Template action implementation for rendering Jinja2 templates."""

from imbi_automations import mixins, models, prompts, utils


class TemplateAction(mixins.WorkflowLoggerMixin):
    """Renders Jinja2 templates with full workflow context.

    Supports single file or directory rendering with automatic variable
    substitution from workflow, project, and repository context.
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

    async def execute(self, action: models.WorkflowTemplateAction) -> None:
        """Execute template action to render Jinja2 templates.

        Args:
            action: Template action configuration

        Raises:
            RuntimeError: If template rendering fails

        """
        source_path = utils.resolve_path(self.context, action.source_path)
        destination_path = utils.resolve_path(
            self.context, action.destination_path
        )

        if not source_path.exists():
            raise RuntimeError(
                f'Template source path does not exist: {source_path}'
            )

        if source_path.is_file():
            # Single file template
            self.logger.debug(
                'Rendering template from %s to %s',
                source_path,
                destination_path,
            )
            with destination_path.open('w', encoding='utf-8') as fh:
                fh.write(prompts.render(self.context, source_path))
            self._log_verbose_info('Rendered template to %s', destination_path)
            return

        # Directory of templates - glob everything
        self.logger.debug(
            'Rendering all templates from directory %s to %s',
            source_path,
            destination_path,
        )
        destination_path.mkdir(parents=True, exist_ok=True)

        template_files = list(source_path.rglob('*'))
        file_count = 0

        for template_file in template_files:
            if template_file.is_file():
                relative_path = template_file.relative_to(source_path)
                dest_file = destination_path / relative_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                with dest_file.open('w', encoding='utf-8') as fh:
                    fh.write(prompts.render(self.context, template_file))
                file_count += 1

        self._log_verbose_info(
            'Rendered %d templates from %s to %s',
            file_count,
            source_path,
            destination_path,
        )
