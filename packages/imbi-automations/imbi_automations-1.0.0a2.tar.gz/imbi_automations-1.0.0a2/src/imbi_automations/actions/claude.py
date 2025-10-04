"""Claude Code action implementation for AI-powered transformations.

Executes Claude Code actions using agent-based workflows (task/validator) with
prompt templating, failure detection, and restart capabilities for reliable
AI-powered code transformations.
"""

import enum
import pathlib
from email import utils

from imbi_automations import claude, mixins, models, prompts


class AgentType(enum.StrEnum):
    """Claude Code agent types for task execution and validation workflows."""

    task = 'task'
    validator = 'validator'


class ClaudeAction(mixins.WorkflowLoggerMixin):
    """Executes AI-powered code transformations using Claude Code SDK.

    Manages agent-based workflows with task/validator cycles, prompt
    templating, and automatic restart on failure detection.
    """

    def __init__(
        self,
        configuration: models.Configuration,
        context: models.WorkflowContext,
        verbose: bool,
    ) -> None:
        super().__init__(verbose)
        self._set_workflow_logger(context.workflow)
        self.claude = claude.Claude(configuration, context, verbose)
        self.configuration = configuration
        self.context = context
        self.last_error: models.AgentRun | None = None
        commit_author = utils.parseaddr(self.configuration.commit_author)
        self.prompt_kwargs = {
            'commit_author': self.configuration.commit_author,
            'commit_author_name': commit_author[0],
            'commit_author_address': commit_author[1],
            'workflow_name': context.workflow.configuration.name,
            'working_directory': self.context.working_directory,
        }

    async def execute(self, action: models.WorkflowClaudeAction) -> None:
        """Execute the Claude Code action."""
        success = False
        self.last_error = None
        for cycle in range(1, action.max_cycles + 1):
            self._log_verbose_info(
                'Claude Code cycle %d/%d for action %s',
                cycle,
                action.max_cycles,
                action.name,
            )
            if await self._execute_cycle(action, cycle):
                self.logger.debug(
                    'Claude Code %s cycle %d successful', action.name, cycle
                )
                success = True
                break

        if not success:
            raise RuntimeError(
                f'Claude Code action {action.name} failed after '
                f'{action.max_cycles} cycles'
            )

    async def _execute_cycle(
        self, action: models.WorkflowClaudeAction, cycle: int
    ) -> bool:
        for agent in [AgentType.task, AgentType.validator]:
            if agent == AgentType.validator and not action.validation_prompt:
                self.logger.debug('No validation prompt, skipping')
                continue
            self._log_verbose_info(
                'Executing Claude Code %s agent %s in cycle %d',
                agent,
                action.name,
                cycle,
            )
            prompt = self._get_prompt(action, agent)
            self.logger.debug('Execute agent prompt: %s', prompt)
            run = await self.claude.agent_query(prompt)
            self.logger.debug('Execute agent result: %r', run)
            if run.result == models.AgentRunResult.failure:
                self.last_error = run
                self.logger.error(
                    'Claude Code %s agent %s failed in cycle %d',
                    agent,
                    action.name,
                    cycle,
                )
                return False
            self.last_error = None
        return True

    def _get_prompt(
        self,
        action: models.WorkflowAction | models.WorkflowClaudeAction,
        agent: AgentType,
    ) -> str:
        """Return the rendered prompt for the given agent."""
        prompt = f'Use the "{agent}" agent to complete the following task:\n\n'

        if agent == AgentType.task:
            prompt_file = (
                self.context.working_directory / 'workflow' / action.prompt
            )
        elif agent == AgentType.validator:
            prompt_file = (
                self.context.working_directory
                / 'workflow'
                / action.validation_prompt
            )
        else:
            raise RuntimeError(f'Unknown agent: {agent}')

        if prompt_file.suffix == '.j2':
            data = dict(self.prompt_kwargs)
            data.update(self.context.model_dump())
            data.update({'action': action.model_dump()})
            for key in {'source', 'destination'}:
                if key in data:
                    del data[key]
            prompt += prompts.render(self.context, prompt_file, **data)
        else:
            prompt += prompt_file.read_text(encoding='utf-8')

        if self.last_error:
            prompt_file = (
                pathlib.Path(__file__).parent / 'prompts' / 'last-error.md.j2'
            )
            return prompts.render(
                self.context,
                prompt_file,
                last_error=self.last_error.model_dump_json(indent=2),
                original_prompt=prompt,
            )

        return prompt
