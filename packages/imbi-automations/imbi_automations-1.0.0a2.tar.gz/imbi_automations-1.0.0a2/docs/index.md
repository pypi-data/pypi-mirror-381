# Imbi Automations CLI

A comprehensive CLI framework for executing automated workflows across software project repositories with AI-powered transformations and deep integration to the Imbi project management system.

## Overview

Imbi Automations enables bulk automation across your software projects with intelligent targeting, conditional execution, and powerful transformation capabilities. Built on a modern async Python architecture, it provides seamless integration with GitHub and the Imbi project management platform.

### Key Features

- **GitHub Integration**: Native GitHub API integration for comprehensive repository operations
- **AI-Powered Transformations**: Claude Code SDK for intelligent code changes
- **Advanced Filtering**: Target specific project subsets with multiple criteria
- **Conditional Execution**: Smart workflow execution based on repository state
- **Batch Processing**: Concurrent processing with resumption capabilities
- **Template System**: Jinja2-based file generation with full project context

### Use Cases

Across all of your software projects and repositories, Imbi Automations can automate the following tasks:

- **Project Updates**: Upgrade projects to the latest syntax, update dependencies, and fix CI/CD pipelines
- **Project Migrations**: Convert all projects from a language like JavaScript to TypeScript
- **Standards Compliance**: Identify and report on places where project standards are not being followed
- **Project Analysis**: Update Imbi Project Facts based on project analysis results
- **Code Quality Improvements**: Apply linting, formatting, and pre-commit hooks
- **Infrastructure Updates**: Modernize project configurations and tooling
- **Project Reviews**: Automated code reviews and code quality analysis
- **Security Updates**: Update dependencies with security patches
- **Software Upgrades**: Upgrade projects to newer software versions

### Action Types

The framework supports multiple transformation types:

- **Callable Actions**: Direct API method calls with dynamic parameters
- **Claude Code Integration**: Complex multi-file analysis and AI transformations
- **Docker Operations**: Container-based file extraction and manipulation
- **File Actions**: Copy, move, delete, and regex replacement operations
- **Git Operations**: Extract files from previous commits, clone repositories, etc.
- **Imbi Actions**: Update project facts
- **Shell Commands**: Execute arbitrary commands with template variables
- **Utility Actions**: Helper operations for common workflow patterns

## Installation

### From PyPI

```bash
pip install imbi-automations
```

### Development Installation

```bash
git clone <repository-url>
cd imbi-automations-cli
pip install -e .[dev]
pre-commit install
```

## Getting Started

### 1. Configuration

Create a `config.toml` file with your API credentials:

```toml
[github]
api_key = "ghp_your_github_token"
hostname = "github.com"  # Optional, defaults to github.com

[imbi]
api_key = "your-imbi-api-key"
hostname = "imbi.example.com"

[claude_code]
executable = "claude"  # Optional, defaults to 'claude'
```

### 2. Run a Workflow

Execute workflows across all your projects:

```bash
# Run a specific workflow
imbi-automations config.toml workflows/workflow-name --all-projects

# Resume from a specific project (useful for large batches)
imbi-automations config.toml workflows/workflow-name --all-projects --start-from-project my-project-slug
```

### 3. Available Workflows

The tool includes 20 pre-built workflows for common tasks:

- **Python Version Updates**: Upgrade projects to newer Python versions
- **Docker Image Updates**: Update base images and dependencies
- **GitHub Actions**: Fix and optimize CI/CD pipelines
- **Code Quality**: Apply linting, formatting, and pre-commit hooks
- **Infrastructure Updates**: Modernize project configurations and tooling

## Documentation

- **[Architecture Guide](architecture.md)**: Comprehensive technical documentation
- **[Workflow Configuration](workflows.md)**: Creating and running workflows
- **[Workflow Actions](actions/index.md)**: Complete action types reference

## Requirements

- Python 3.12 or higher
- Imbi project management system access
- GitHub API access (for GitHub workflows)
