"""Comprehensive tests for the claude module."""

import json
import pathlib
import tempfile
import unittest
from unittest import mock

import claude_agent_sdk
import pydantic

from imbi_automations import claude, models
from tests import base


def _test_response_validator(message: str) -> str:
    """Test helper function that replicates response_validator logic."""
    try:
        payload = json.loads(message)
    except json.JSONDecodeError:
        return 'Payload not validate as JSON'
    try:
        models.AgentRun.model_validate(payload)
    except pydantic.ValidationError as exc:
        return str(exc)
    return 'Response is valid'


class ResponseValidatorTestCase(unittest.TestCase):
    """Test cases for the response_validator function logic."""

    def test_response_validator_valid_json(self) -> None:
        """Test response_validator with valid JSON."""
        valid_payload = {
            'result': 'success',
            'message': 'Test successful',
            'errors': [],
        }
        json_message = json.dumps(valid_payload)

        result = _test_response_validator(json_message)

        self.assertEqual(result, 'Response is valid')

    def test_response_validator_invalid_json(self) -> None:
        """Test response_validator with invalid JSON."""
        invalid_json = '{"invalid": json syntax'

        result = _test_response_validator(invalid_json)

        self.assertEqual(result, 'Payload not validate as JSON')

    def test_response_validator_invalid_schema(self) -> None:
        """Test response_validator with invalid AgentRun schema."""
        invalid_payload = {'wrong_field': 'invalid', 'missing_result': True}
        json_message = json.dumps(invalid_payload)

        result = _test_response_validator(json_message)

        self.assertIn('validation error', result)


class ClaudeTestCase(base.AsyncTestCase):
    """Test cases for the Claude class."""

    def setUp(self) -> None:
        super().setUp()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.working_directory = pathlib.Path(self.temp_dir.name)
        self.config = models.Configuration(
            claude_code=models.ClaudeCodeConfiguration(executable='claude'),
            anthropic=models.AnthropicConfiguration(),
            imbi=models.ImbiConfiguration(api_key='test', hostname='test.com'),
            commit_author='Test Author <test@example.com>',
        )

        # Create required directory structure
        (self.working_directory / 'workflow').mkdir()
        (self.working_directory / 'extracted').mkdir()
        (self.working_directory / 'repository').mkdir()

        # Create mock workflow and context
        self.workflow = models.Workflow(
            path=pathlib.Path('/mock/workflow'),
            configuration=models.WorkflowConfiguration(
                name='test-workflow', actions=[]
            ),
        )

        self.context = models.WorkflowContext(
            workflow=self.workflow,
            imbi_project=models.ImbiProject(
                id=123,
                dependencies=None,
                description='Test project',
                environments=None,
                facts=None,
                identifiers=None,
                links=None,
                name='test-project',
                namespace='test-namespace',
                namespace_slug='test-namespace',
                project_score=None,
                project_type='API',
                project_type_slug='api',
                slug='test-project',
                urls=None,
                imbi_url='https://imbi.example.com/projects/123',
            ),
            working_directory=self.working_directory,
        )

    def tearDown(self) -> None:
        super().tearDown()
        self.temp_dir.cleanup()

    @mock.patch('claude_agent_sdk.ClaudeSDKClient')
    @mock.patch('claude_agent_sdk.create_sdk_mcp_server')
    @mock.patch(
        'builtins.open',
        new_callable=mock.mock_open,
        read_data='Mock system prompt',
    )
    def test_claude_init(
        self,
        mock_file: mock.MagicMock,
        mock_create_server: mock.MagicMock,
        mock_client_class: mock.MagicMock,
    ) -> None:
        """Test Claude initialization."""
        mock_server = mock.MagicMock()
        mock_create_server.return_value = mock_server
        mock_client_instance = mock.MagicMock()
        mock_client_class.return_value = mock_client_instance

        claude_instance = claude.Claude(
            configuration=self.config, context=self.context, verbose=True
        )

        # Verify initialization
        self.assertEqual(claude_instance.configuration, self.config)
        self.assertEqual(
            claude_instance.context.working_directory, self.working_directory
        )
        self.assertEqual(claude_instance.context.workflow, self.workflow)
        self.assertTrue(claude_instance.verbose)
        self.assertIsNone(claude_instance.session_id)

        # Verify client creation was called
        mock_client_class.assert_called_once()
        mock_create_server.assert_called_once()

    def test_parse_message_result_message_success(self) -> None:
        """Test _parse_message with successful ResultMessage."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        # Test with plain JSON
        valid_result = {'result': 'success', 'message': 'Operation completed'}

        # Create mock ResultMessage
        message = mock.MagicMock(spec=claude_agent_sdk.ResultMessage)
        message.session_id = 'test-session'
        message.result = json.dumps(valid_result)
        message.is_error = False

        result = claude_instance._parse_message(message)

        self.assertIsInstance(result, models.AgentRun)
        self.assertEqual(result.result, models.AgentRunResult.success)
        self.assertEqual(result.message, 'Operation completed')
        self.assertEqual(claude_instance.session_id, 'test-session')

    def test_parse_message_result_message_with_json_code_blocks(self) -> None:
        """Test _parse_message with JSON code blocks."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        valid_result = {'result': 'success', 'message': 'Operation completed'}

        # Test with ```json wrapper
        json_with_wrapper = f'```json\n{json.dumps(valid_result)}\n```'

        message = mock.MagicMock(spec=claude_agent_sdk.ResultMessage)
        message.session_id = 'test-session'
        message.result = json_with_wrapper
        message.is_error = False

        result = claude_instance._parse_message(message)

        self.assertIsInstance(result, models.AgentRun)
        self.assertEqual(result.result, models.AgentRunResult.success)
        self.assertEqual(result.message, 'Operation completed')

    def test_parse_message_result_message_error(self) -> None:
        """Test _parse_message with error ResultMessage."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        message = mock.MagicMock(spec=claude_agent_sdk.ResultMessage)
        message.session_id = 'test-session'
        message.result = 'Error occurred'
        message.is_error = True

        result = claude_instance._parse_message(message)

        self.assertIsInstance(result, models.AgentRun)
        self.assertEqual(result.result, models.AgentRunResult.failure)
        self.assertEqual(result.message, 'Claude Error')
        self.assertEqual(result.errors, ['Error occurred'])

    def test_parse_message_result_message_invalid_json(self) -> None:
        """Test _parse_message with ResultMessage containing invalid JSON."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        message = mock.MagicMock(spec=claude_agent_sdk.ResultMessage)
        message.session_id = 'test-session'
        message.result = '{"invalid": json syntax'
        message.is_error = False

        result = claude_instance._parse_message(message)

        self.assertIsInstance(result, models.AgentRun)
        self.assertEqual(result.result, models.AgentRunResult.failure)
        self.assertEqual(result.message, 'Agent Contract Failure')
        self.assertTrue(
            any(
                'Failed to parse JSON result' in error
                for error in result.errors
            )
        )

    def test_parse_message_assistant_message(self) -> None:
        """Test _parse_message with AssistantMessage."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        message = mock.MagicMock(spec=claude_agent_sdk.AssistantMessage)
        message.content = [mock.MagicMock(spec=claude_agent_sdk.TextBlock)]

        with mock.patch.object(claude_instance, '_log_message') as mock_log:
            result = claude_instance._parse_message(message)

        self.assertIsNone(result)
        mock_log.assert_called_once_with('Claude Assistant', message.content)

    def test_parse_message_system_message(self) -> None:
        """Test _parse_message with SystemMessage."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        message = mock.MagicMock(spec=claude_agent_sdk.SystemMessage)
        message.data = 'System message'

        result = claude_instance._parse_message(message)

        self.assertIsNone(result)

    def test_parse_message_user_message(self) -> None:
        """Test _parse_message with UserMessage."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        message = mock.MagicMock(spec=claude_agent_sdk.UserMessage)
        message.content = [mock.MagicMock(spec=claude_agent_sdk.TextBlock)]

        with mock.patch.object(claude_instance, '_log_message') as mock_log:
            result = claude_instance._parse_message(message)

        self.assertIsNone(result)
        mock_log.assert_called_once_with('Claude User', message.content)

    def test_log_message_with_text_list(self) -> None:
        """Test _log_message method with list of text blocks."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        text_block1 = mock.MagicMock(spec=claude_agent_sdk.TextBlock)
        text_block1.text = 'First message'
        text_block2 = mock.MagicMock(spec=claude_agent_sdk.TextBlock)
        text_block2.text = 'Second message'
        tool_block = mock.MagicMock(spec=claude_agent_sdk.ToolUseBlock)

        content = [text_block1, text_block2, tool_block]

        with mock.patch.object(claude_instance.logger, 'debug') as mock_debug:
            claude_instance._log_message('Test Type', content)

        # Verify only text blocks were logged
        self.assertEqual(mock_debug.call_count, 2)
        mock_debug.assert_has_calls(
            [
                mock.call('%s: %s', 'Test Type', 'First message'),
                mock.call('%s: %s', 'Test Type', 'Second message'),
            ]
        )

    def test_log_message_with_string(self) -> None:
        """Test _log_message method with string content."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        with mock.patch.object(claude_instance.logger, 'debug') as mock_debug:
            claude_instance._log_message('Test Type', 'Simple string message')

        mock_debug.assert_called_once_with(
            '%s: %s', 'Test Type', 'Simple string message'
        )

    def test_log_message_with_unknown_block_type(self) -> None:
        """Test _log_message method with unknown block type."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        # Create a mock unknown block type
        unknown_block = mock.MagicMock()
        unknown_block.__class__.__name__ = 'UnknownBlock'
        content = [unknown_block]

        with self.assertRaises(RuntimeError) as exc_context:
            claude_instance._log_message('Test Type', content)

        self.assertIn('Unknown message type', str(exc_context.exception))

    # Note: execute-related tests moved to tests/actions/test_claude.py

    def test_parse_message_with_session_id_update(self) -> None:
        """Test _parse_message updates session_id when different."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        # Set initial session_id
        claude_instance.session_id = 'old-session'

        valid_result = {'result': 'success', 'message': 'Session updated'}

        message = mock.MagicMock(spec=claude_agent_sdk.ResultMessage)
        message.session_id = 'new-session'
        message.result = json.dumps(valid_result)
        message.is_error = False

        result = claude_instance._parse_message(message)

        self.assertIsInstance(result, models.AgentRun)
        self.assertEqual(claude_instance.session_id, 'new-session')

    def test_parse_message_with_same_session_id(self) -> None:
        """Test _parse_message doesn't update session_id when same."""
        with (
            mock.patch('claude_agent_sdk.ClaudeSDKClient'),
            mock.patch('claude_agent_sdk.create_sdk_mcp_server'),
            mock.patch(
                'builtins.open',
                new_callable=mock.mock_open,
                read_data='Mock system prompt',
            ),
        ):
            claude_instance = claude.Claude(
                configuration=self.config, context=self.context
            )

        # Set initial session_id
        claude_instance.session_id = 'same-session'

        valid_result = {'result': 'success', 'message': 'Same session'}

        message = mock.MagicMock(spec=claude_agent_sdk.ResultMessage)
        message.session_id = 'same-session'
        message.result = json.dumps(valid_result)
        message.is_error = False

        result = claude_instance._parse_message(message)

        self.assertIsInstance(result, models.AgentRun)
        # Session ID should remain unchanged since it's the same
        self.assertEqual(claude_instance.session_id, 'same-session')


if __name__ == '__main__':
    unittest.main()
