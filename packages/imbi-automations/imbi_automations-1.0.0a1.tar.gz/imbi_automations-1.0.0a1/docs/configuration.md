# Configuration

Imbi Automations uses TOML-based configuration files with Pydantic validation for all settings. This document describes all available configuration options.

## Configuration File Location

By default, the CLI expects a `config.toml` file as the first argument:

```bash
imbi-automations config.toml workflows/workflow-name --all-projects
```

## Complete Configuration Example

```toml
# Global Settings
ai_commits = false
commit_author = "Imbi Automations <noreply@example.com>"
error_dir = "./errors"
preserve_on_error = false

# Anthropic API Configuration
[anthropic]
api_key = "${ANTHROPIC_API_KEY}"  # Or set directly
bedrock = false
model = "claude-3-5-sonnet-latest"

# Claude Code SDK Configuration
[claude_code]
executable = "claude"
enabled = true

# GitHub API Configuration
[github]
api_key = "ghp_your_github_token"
hostname = "github.com"

# GitLab API Configuration (optional)
[gitlab]
api_key = "glpat_your_gitlab_token"
hostname = "gitlab.com"

# Imbi Project Management Configuration
[imbi]
api_key = "your-imbi-api-key"
hostname = "imbi.example.com"
github_identifier = "github"
gitlab_identifier = "gitlab"
github_link = "GitHub Repository"
gitlab_link = "GitLab Project"
```

## Global Settings

### ai_commits

Enable AI-powered commit message generation.

**Type:** `boolean`
**Default:** `false`

When enabled, uses Anthropic API to generate commit messages based on changes.

```toml
ai_commits = true
```

### commit_author

Git commit author information for automated commits.

**Type:** `string`
**Default:** `"Imbi Automations <noreply@aweber.com>"`
**Format:** `"Name <email>"`

```toml
commit_author = "Bot User <bot@example.com>"
```

### error_dir

Directory to store error logs and debugging information when workflows fail.

**Type:** `path`
**Default:** `"./errors"`

```toml
error_dir = "/var/log/imbi-automations/errors"
```

### preserve_on_error

Preserve working directories when errors occur for debugging.

**Type:** `boolean`
**Default:** `false`

When `true`, temporary directories are not cleaned up after failures, allowing manual inspection.

```toml
preserve_on_error = true
```

## Anthropic Configuration

Configuration for Anthropic Claude API used in Claude actions and AI commit generation.

### [anthropic].api_key

Anthropic API key for Claude models.

**Type:** `string` (secret)
**Default:** `$ANTHROPIC_API_KEY` environment variable
**Required:** For Claude actions or `ai_commits = true`

```toml
[anthropic]
api_key = "sk-ant-api03-..."
```

Or use environment variable:
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

### [anthropic].bedrock

Use AWS Bedrock instead of direct Anthropic API.

**Type:** `boolean`
**Default:** `false`

```toml
[anthropic]
bedrock = true
```

**Note:** Requires AWS credentials configured separately.

### [anthropic].model

Claude model to use for API requests.

**Type:** `string`
**Default:** `"claude-3-5-haiku-latest"`

**Available Models:**
- `claude-3-5-sonnet-latest` - Most capable, higher cost
- `claude-3-5-haiku-latest` - Fast and efficient (default)
- `claude-3-opus-latest` - Highest capability, highest cost

```toml
[anthropic]
model = "claude-3-5-sonnet-latest"
```

## Claude Code Configuration

Configuration for Claude Code SDK integration.

### [claude_code].executable

Path or command name for Claude Code executable.

**Type:** `string`
**Default:** `"claude"`

```toml
[claude_code]
executable = "/usr/local/bin/claude"
```

### [claude_code].enabled

Enable Claude Code actions in workflows.

**Type:** `boolean`
**Default:** `true`

Set to `false` to disable all Claude actions:

```toml
[claude_code]
enabled = false
```

### [claude_code].base_prompt

Custom base prompt file for Claude Code sessions.

**Type:** `path`
**Default:** `src/imbi_automations/prompts/claude.md`

```toml
[claude_code]
base_prompt = "/path/to/custom-prompt.md"
```

## GitHub Configuration

Configuration for GitHub API integration.

### [github].api_key

GitHub personal access token or fine-grained token.

**Type:** `string` (secret)
**Required:** For GitHub workflows

**Token Permissions Required:**
- `repo` - Full repository access
- `workflow` - Update GitHub Actions workflows
- `admin:org` - Manage organization (for environment sync)

```toml
[github]
api_key = "ghp_your_github_personal_access_token"
```

### [github].hostname

GitHub hostname for Enterprise installations.

**Type:** `string`
**Default:** `"github.com"`

For GitHub Enterprise:
```toml
[github]
hostname = "github.enterprise.com"
```

## GitLab Configuration

Configuration for GitLab API integration (optional).

### [gitlab].api_key

GitLab personal access token.

**Type:** `string` (secret)
**Required:** For GitLab workflows

**Token Scopes Required:**
- `api` - Full API access
- `read_repository` - Read repository files
- `write_repository` - Create/update files

```toml
[gitlab]
api_key = "glpat_your_gitlab_token"
```

### [gitlab].hostname

GitLab hostname for self-hosted installations.

**Type:** `string`
**Default:** `"gitlab.com"`

For self-hosted:
```toml
[gitlab]
hostname = "gitlab.example.com"
```

## Imbi Configuration

Configuration for Imbi project management system integration.

### [imbi].api_key

Imbi API authentication key.

**Type:** `string` (secret)
**Required:** Always (core functionality)

```toml
[imbi]
api_key = "your-imbi-api-key-uuid"
```

### [imbi].hostname

Imbi instance hostname.

**Type:** `string`
**Required:** Always

```toml
[imbi]
hostname = "imbi.example.com"
```

### [imbi].*_identifier

Project identifier field names in Imbi for external systems.

**Type:** `string`
**Defaults:**
- `github_identifier = "github"`
- `gitlab_identifier = "gitlab"`
- `pagerduty_identifier = "pagerduty"`
- `sonarqube_identifier = "sonarqube"`
- `sentry_identifier = "sentry"`

These specify which Imbi project identifier fields contain external system references:

```toml
[imbi]
github_identifier = "github-id"
gitlab_identifier = "gitlab-id"
```

### [imbi].*_link

Link type names in Imbi for external system URLs.

**Type:** `string`
**Defaults:**
- `github_link = "GitHub Repository"`
- `gitlab_link = "GitLab Project"`
- `grafana_link = "Grafana Dashboard"`
- `pagerduty_link = "PagerDuty"`
- `sentry_link = "Sentry"`
- `sonarqube_link = "SonarQube"`

These specify the link type names used in Imbi to store external URLs:

```toml
[imbi]
github_link = "GitHub Repo"
gitlab_link = "GitLab"
```

## Environment Variables

Several configuration values support environment variable substitution:

### Supported in Configuration File

```toml
[github]
api_key = "${GITHUB_TOKEN}"

[anthropic]
api_key = "${ANTHROPIC_API_KEY}"

[imbi]
api_key = "${IMBI_API_KEY}"
```

### Environment Variable Defaults

Some fields use environment variables as defaults if not specified:

| Configuration Field | Environment Variable |
|---------------------|---------------------|
| `anthropic.api_key` | `ANTHROPIC_API_KEY` |

## Minimal Configuration

The absolute minimum configuration for basic GitHub workflows:

```toml
[github]
api_key = "ghp_your_token"

[imbi]
api_key = "your-imbi-key"
hostname = "imbi.example.com"
```

## Configuration Validation

Configuration is validated at startup using Pydantic. Common errors:

### Missing Required Fields

```
ValidationError: 1 validation error for Configuration
github.api_key
  field required (type=value_error.missing)
```

**Solution:** Add the required field to your config.toml

### Invalid API Key Format

```
ValidationError: 1 validation error for Configuration
github.api_key
  string does not match regex (type=value_error.str.regex)
```

**Solution:** Check API key format and validity

### Invalid Hostname

```
ValidationError: 1 validation error for Configuration
imbi.hostname
  invalid hostname (type=value_error.url.host)
```

**Solution:** Use valid hostname without protocol (no `https://`)

## Security Best Practices

### API Key Storage

**DO NOT** commit API keys to version control:

```toml
# ❌ BAD - Keys in config file
[github]
api_key = "ghp_actual_key_here"

# ✅ GOOD - Environment variables
[github]
api_key = "${GITHUB_TOKEN}"
```

### File Permissions

Restrict config file permissions:

```bash
chmod 600 config.toml
```

### Environment Variables

Set sensitive values via environment:

```bash
export GITHUB_TOKEN="ghp_..."
export ANTHROPIC_API_KEY="sk-ant-..."
export IMBI_API_KEY="uuid-here"

imbi-automations config.toml workflows/workflow-name --all-projects
```

### Separate Configurations

Use different config files for different environments:

```bash
# Development
imbi-automations config.dev.toml workflows/test

# Production
imbi-automations config.prod.toml workflows/deploy
```

## Configuration Examples

### GitHub Only Workflows

```toml
commit_author = "GitHub Bot <bot@example.com>"

[github]
api_key = "${GITHUB_TOKEN}"

[imbi]
api_key = "${IMBI_API_KEY}"
hostname = "imbi.example.com"
```

### GitHub Enterprise

```toml
[github]
api_key = "${GITHUB_ENTERPRISE_TOKEN}"
hostname = "github.enterprise.com"

[imbi]
api_key = "${IMBI_API_KEY}"
hostname = "imbi.example.com"
```

### With AI Features

```toml
ai_commits = true

[anthropic]
api_key = "${ANTHROPIC_API_KEY}"
model = "claude-3-5-sonnet-latest"

[claude_code]
enabled = true
executable = "claude"

[github]
api_key = "${GITHUB_TOKEN}"

[imbi]
api_key = "${IMBI_API_KEY}"
hostname = "imbi.example.com"
```

### Multi-Platform

```toml
[github]
api_key = "${GITHUB_TOKEN}"

[gitlab]
api_key = "${GITLAB_TOKEN}"

[imbi]
api_key = "${IMBI_API_KEY}"
hostname = "imbi.example.com"
github_identifier = "github"
gitlab_identifier = "gitlab"
```

### With Debugging

```toml
preserve_on_error = true
error_dir = "/tmp/imbi-errors"

[github]
api_key = "${GITHUB_TOKEN}"

[imbi]
api_key = "${IMBI_API_KEY}"
hostname = "imbi.example.com"
```

## Troubleshooting

### Configuration Not Loading

**Problem:** `FileNotFoundError: config.toml not found`

**Solution:** Provide full path to config file:
```bash
imbi-automations /path/to/config.toml workflows/name --all-projects
```

### Authentication Failures

**Problem:** `401 Unauthorized` errors

**Solutions:**
1. Verify API key is valid and not expired
2. Check API key has required permissions
3. Ensure environment variables are exported
4. Test API access manually with curl

### Invalid TOML Syntax

**Problem:** `toml.decoder.TomlDecodeError`

**Solutions:**
1. Validate TOML syntax with online validator
2. Check for missing quotes around strings
3. Verify section headers use `[section]` format
4. Ensure key-value pairs use `key = "value"` format

## Advanced Configuration

### Custom Error Directory Structure

```toml
error_dir = "/var/log/imbi-automations/errors"
```

Creates:
```
/var/log/imbi-automations/errors/
└── workflow-name/
    └── project-slug-timestamp/
        ├── repository/
        ├── workflow/
        └── error.log
```

### Custom Commit Author Per Workflow

Set in workflow config.toml instead:

```toml
# workflows/my-workflow/config.toml
commit_author = "Workflow Bot <workflow@example.com>"
```

Overrides global `commit_author` for that workflow only.

## See Also

- [Workflow Actions](actions/index.md) - Complete action configuration reference
- [Architecture](architecture.md) - System design and components
- [GitHub Actions](actions/github.md) - GitHub-specific configuration
- [Claude Actions](actions/claude.md) - AI transformation configuration
