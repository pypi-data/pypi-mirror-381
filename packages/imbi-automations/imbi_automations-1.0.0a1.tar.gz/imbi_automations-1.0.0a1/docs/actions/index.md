# Workflow Actions

Workflow actions are the core building blocks of automation in Imbi Automations. Each action type provides specific capabilities for interacting with repositories, external services, and project files.

## Action Types Overview

| Action Type | Purpose | Use Cases |
|------------|---------|-----------|
| [Callable](callable.md) | Direct API method calls | GitHub/GitLab operations, Imbi updates |
| [Claude](claude.md) | AI-powered transformations | Complex code changes, intelligent analysis |
| [Docker](docker.md) | Container operations | Extract files from images, build images |
| [File](file.md) | File manipulation | Copy, move, delete, append, write files |
| [Git](git.md) | Version control operations | Extract commits, branch management |
| [GitHub](github.md) | GitHub-specific operations | Environment sync, workflow management |
| [Shell](shell.md) | Command execution | Run tests, build processes, scripts |
| [Template](template.md) | Jinja2 file generation | Generate configs, documentation |
| [Utility](utility.md) | Helper operations | Logging, state management |

## ResourceUrl Path System

All file and resource paths in actions use the `ResourceUrl` type, which supports multiple schemes for flexible file addressing:

### Path Schemes

#### `file:///` - Relative to Working Directory
Default scheme for simple paths. Resolves relative to the workflow's working directory:

```toml
[[actions]]
type = "file"
command = "copy"
source = "file:///config.yaml"      # Or just "config.yaml"
destination = "file:///backup/config.yaml"
```

Equivalent simplified syntax:
```toml
source = "config.yaml"
destination = "backup/config.yaml"
```

#### `repository:///` - Repository Files
Paths within the cloned Git repository:

```toml
[[actions]]
type = "file"
command = "copy"
source = "repository:///.github/workflows/ci.yml"
destination = "repository:///.github/workflows/ci-backup.yml"
```

The `repository:///` prefix maps to `{working_directory}/repository/` where the actual repository is cloned.

#### `workflow:///` - Workflow Resources
Paths to files bundled with the workflow itself:

```toml
[[actions]]
type = "file"
command = "copy"
source = "workflow:///.gitignore"           # From workflow directory
destination = "repository:///.gitignore"     # To repository
```

The `workflow:///` prefix maps to `{working_directory}/workflow/` where workflow resources are staged.

#### `extracted:///` - Docker Extracted Files
Files extracted from Docker containers via docker actions:

```toml
[[actions]]
name = "extract-from-image"
type = "docker"
command = "extract"
image = "myapp:latest"
source = "/app/config/"
destination = "extracted:///configs/"

[[actions]]
name = "copy-extracted"
type = "file"
command = "copy"
source = "extracted:///configs/app.yaml"
destination = "repository:///config/app.yaml"
```

The `extracted:///` prefix maps to `{working_directory}/extracted/` where Docker-extracted files are stored.

### Path Resolution Examples

```toml
# Example 1: Copy workflow template to repository
[[actions]]
type = "file"
command = "copy"
source = "workflow:///templates/README.md"
destination = "repository:///README.md"

# Example 2: Extract Docker config and use it
[[actions]]
name = "extract-config"
type = "docker"
command = "extract"
image = "python:3.12"
source = "/usr/local/lib/python3.12/"
destination = "extracted:///python-libs/"

[[actions]]
name = "analyze-libs"
type = "shell"
command = "ls -lah {{ working_directory }}/extracted/python-libs"

# Example 3: Multiple file operations
[[actions]]
type = "file"
command = "copy"
source = "repository:///old-config.yaml"
destination = "repository:///backup/config.yaml"

[[actions]]
type = "file"
command = "write"
path = "repository:///config.yaml"
content = "new_config: true"
```

### Working Directory Structure

During workflow execution, the working directory contains:

```
{working_directory}/
├── repository/          # Cloned Git repository
│   ├── .git/
│   ├── README.md
│   └── ...
├── workflow/            # Workflow resources (templates, files)
│   ├── templates/
│   ├── .gitignore
│   └── ...
├── extracted/           # Files extracted from Docker
│   └── configs/
└── other files...       # Working files (logs, temp files)
```

### Case Sensitivity

**Important**: File paths preserve case sensitivity. The three-slash format (`file:///`) ensures paths are treated correctly on both case-sensitive (Linux) and case-insensitive (macOS/Windows) filesystems.

```toml
# Correct - case is preserved
source = "README.md"              # Becomes file:///README.md
source = "repository:///LICENSE"  # Exact case maintained

# Incorrect legacy format (deprecated)
source = "file://readme.md"       # Would lowercase on some systems
```

## Common Action Patterns

### Sequential File Operations

```toml
[[actions]]
name = "backup-config"
type = "file"
command = "copy"
source = "repository:///config.yaml"
destination = "repository:///config.yaml.bak"

[[actions]]
name = "update-config"
type = "file"
command = "write"
path = "repository:///config.yaml"
content = """
version: 2
updated: true
"""
```

### Template Generation Pipeline

```toml
[[actions]]
name = "render-templates"
type = "template"
source_path = "workflow:///templates/"
destination_path = "repository:///config/"

[[actions]]
name = "validate-configs"
type = "shell"
command = "python -m yamllint {{ working_directory }}/repository/config/"
```

### Docker Extract and Transform

```toml
[[actions]]
name = "extract-from-base"
type = "docker"
command = "extract"
image = "base:latest"
source = "/app/"
destination = "extracted:///base-app/"

[[actions]]
name = "merge-with-repo"
type = "file"
command = "copy"
source = "extracted:///base-app/config.json"
destination = "repository:///config/base.json"
```

## Action Execution Context

All actions execute with access to these context variables (via Jinja2 templating where supported):

- `workflow`: Current workflow configuration
- `imbi_project`: Imbi project data (ID, name, type, facts, etc.)
- `github_repository`: GitHub repository data (if applicable)
- `gitlab_project`: GitLab project data (if applicable)
- `working_directory`: Temporary execution directory path
- `starting_commit`: Initial Git commit SHA (for tracking changes)

See individual action type documentation for specific configuration options and examples.
