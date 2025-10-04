"""Docker operations for workflow execution."""

import asyncio

from imbi_automations import mixins, models, prompts


class DockerActions(mixins.WorkflowLoggerMixin):
    """Executes Docker operations including container file extraction.

    Manages Docker container lifecycle for build, extract, pull, and push
    operations with automatic cleanup.
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

    async def execute(self, action: models.WorkflowDockerAction) -> None:
        """Execute a docker action based on the command type.

        Args:
            context: Workflow context
            action: Docker action containing the command and parameters

        Raises:
            RuntimeError: If docker operation fails
            ValueError: If required parameters are missing or invalid

        """
        match action.command:
            case models.WorkflowDockerActionCommand.build:
                await self._execute_build(action)
            case models.WorkflowDockerActionCommand.extract:
                await self._execute_extract(action)
            case models.WorkflowDockerActionCommand.pull:
                await self._execute_pull(action)
            case models.WorkflowDockerActionCommand.push:
                await self._execute_push(action)
            case _:
                raise RuntimeError(
                    f'Unsupported docker command: {action.command}'
                )

    async def _execute_build(
        self, action: models.WorkflowDockerAction
    ) -> None:
        """Execute docker build command."""
        raise NotImplementedError('Docker build not yet supported')

    async def _execute_extract(
        self, action: models.WorkflowDockerAction
    ) -> None:
        """Execute docker extract command to copy files from container."""
        image = (
            prompts.render(self.context, str(action.image))
            if prompts.has_template_syntax(action.image)
            else action.image
        )
        image = f'{image}:{action.tag}' if ':' not in image else image
        source_path = str(action.source)
        # Extract destination URL path - yarl parses file://name as host,
        # not path
        dest_url = str(action.destination)
        import yarl

        dest_uri = yarl.URL(dest_url)
        dest_filename = (
            str(dest_uri.host + dest_uri.path.lstrip('/'))
            if dest_uri.host
            else dest_uri.path.lstrip('/')
        )
        dest_path = (
            self.context.working_directory / 'extracted' / dest_filename
        )
        self._log_verbose_info(
            'Extracting %s from container %s to %s',
            source_path,
            image,
            dest_path,
        )
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        container_name = f'imbi-extract-{id(action)}'
        try:
            await self._run_docker_command(['docker', 'pull', image])
            await self._run_docker_command(
                ['docker', 'create', '--name', container_name, image]
            )
            await self._run_docker_command(
                [
                    'docker',
                    'cp',
                    f'{container_name}:{source_path}',
                    str(dest_path),
                ]
            )
            self.logger.debug(
                'Successfully extracted %s to %s', source_path, dest_path
            )
        finally:
            try:
                await self._run_docker_command(
                    ['docker', 'rm', container_name], check_exit_code=False
                )
            except RuntimeError as exc:
                self.logger.debug(
                    'Failed to cleanup container %s: %s', container_name, exc
                )

    async def _execute_pull(self, action: models.WorkflowDockerAction) -> None:
        """Execute docker pull command."""
        raise NotImplementedError('Docker pull not yet supported')

    async def _execute_push(self, action: models.WorkflowDockerAction) -> None:
        """Execute docker push command."""
        raise NotImplementedError('Docker push not yet supported')

    async def _run_docker_command(
        self, command: list[str], check_exit_code: bool = True
    ) -> tuple[int, str, str]:
        """Run a docker command and return exit code, stdout, stderr.

        Args:
            command: Docker command as list of arguments
            check_exit_code: Whether to raise exception on non-zero exit

        Returns:
            Tuple of (exit_code, stdout, stderr)

        Raises:
            RuntimeError: If command fails and check_exit_code is True

        """
        self.logger.debug('Running docker command: %s', ' '.join(command))

        try:
            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await process.communicate()

            stdout_str = stdout.decode('utf-8') if stdout else ''
            stderr_str = stderr.decode('utf-8') if stderr else ''

            self.logger.debug(
                'Docker command completed with exit code %d',
                process.returncode,
            )

            if stdout_str:
                self.logger.debug('Docker stdout: %s', stdout_str)
            if stderr_str:
                self.logger.debug('Docker stderr: %s', stderr_str)

            if check_exit_code and process.returncode != 0:
                raise RuntimeError(
                    f'Docker command failed (exit code {process.returncode}): '
                    f'{stderr_str or stdout_str}'
                )

            return process.returncode, stdout_str, stderr_str

        except FileNotFoundError as exc:
            raise RuntimeError(
                'Docker command not found - is Docker installed and in PATH?'
            ) from exc
