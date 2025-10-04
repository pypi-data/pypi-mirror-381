"""Git commit handling with AI-powered and manual commit support.

Manages git commits for workflow actions, supporting both Claude
AI-powered commit message generation and manual commits with templated
messages.
"""

import logging
import pathlib

from imbi_automations import claude, git, mixins, models, prompts

LOGGER = logging.getLogger(__name__)

BASE_PATH = pathlib.Path(__file__).parent


class Committer(mixins.WorkflowLoggerMixin):
    """Handles git commits for workflow actions.

    Supports both AI-powered commit message generation via Claude and manual
    commits with templated messages.
    """

    def __init__(
        self, configuration: models.Configuration, verbose: bool
    ) -> None:
        super().__init__(verbose)
        self.configuration = configuration
        self.logger = LOGGER

    async def commit(
        self, context: models.WorkflowContext, action: models.WorkflowAction
    ) -> None:
        self._set_workflow_logger(context.workflow)
        if (
            action.ai_commit
            and self.configuration.ai_commits
            and self.configuration.claude_code.enabled
        ):
            await self._claude_commit(context, action)
        else:
            await self._manual_commit(context, action)

    async def _claude_commit(
        self, context: models.WorkflowContext, action: models.WorkflowAction
    ) -> None:
        """Leverage Claude Code to commit changes."""
        self._log_verbose_info(
            'Using Claude Code to commit changes for %s', action.name
        )
        client = claude.Claude(self.configuration, context, self.verbose)

        # Build the commit prompt from the command template
        commit_template = BASE_PATH / 'prompts' / 'commit.md.j2'
        prompt = prompts.render(
            source=commit_template,
            action_name=action.name,
            **client.prompt_kwargs,
        )

        run = await client.agent_query(prompt)

        if run.result == models.AgentRunResult.failure:
            for phrase in ['no changes to commit', 'working tree is clean']:
                if phrase in (run.message or '').lower():
                    return None
            raise RuntimeError(f'Claude Code commit failed: {run.message}')
        return None

    async def _manual_commit(
        self, context: models.WorkflowContext, action: models.WorkflowAction
    ) -> None:
        """Fallback commit implementation without Claude.

        - Stages all pending changes
        - Creates a commit with required format and trailer
        """
        repo_dir = context.working_directory / 'repository'

        # Stage all changes including deletions
        await git.add_files(working_directory=repo_dir)

        # Build commit message
        body = f'{action.commit_message}\n\n' if action.commit_message else ''
        message = (
            f'imbi-automations: {context.workflow.configuration.name} '
            f'- {action.name}\n\n{body}'
            '🤖 Generated with [Imbi Automations]'
            '(https://github.com/AWeber-Imbi/).'
        )
        try:
            commit_sha = await git.commit_changes(
                working_directory=repo_dir,
                message=message,
                commit_author=self.configuration.commit_author,
            )
        except RuntimeError as exc:
            self.logger.error('git commit failed: %s', exc)
            raise
        else:
            if commit_sha:
                self.logger.info('Committed changes: %s', commit_sha)
            else:
                self.logger.info('No changes to commit')
