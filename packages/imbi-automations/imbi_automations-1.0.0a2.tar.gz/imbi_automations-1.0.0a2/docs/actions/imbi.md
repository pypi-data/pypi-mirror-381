# Imbi Actions

Imbi actions provide integration with the Imbi project management system, enabling workflows to interact with and update project metadata, facts, and configurations.

## Configuration

```toml
[[actions]]
name = "action-name"
type = "imbi"
command = "set_project_fact"  # Required
```

## Available Commands

### set_project_fact

**Status:** Not yet implemented

Updates or creates a fact for the current project in Imbi.

**Configuration:**
```toml
[[actions]]
name = "update-python-version"
type = "imbi"
command = "set_project_fact"
fact_name = "Python Version"
fact_value = "3.12"
```

**Fields:**

- `fact_name` (string, required): Name of the fact to set
- `fact_value` (string, required): Value to assign to the fact

**Use Cases:**

- Update project metadata after automated changes
- Track migration status across projects
- Record version upgrades or dependency changes
- Maintain synchronization between repository state and Imbi

## Context Access

Imbi actions have access to the current project data through the workflow context:

```python
context.imbi_project.id           # Project ID
context.imbi_project.name         # Project name
context.imbi_project.namespace    # Project namespace
context.imbi_project.project_type # Project type
context.imbi_project.facts        # Current project facts
```

## Examples

### Update Python Version Fact

```toml
[[actions]]
name = "upgrade-python"
type = "claude"
prompt = "workflow:///prompts/upgrade-python.md"

[[actions]]
name = "record-python-version"
type = "imbi"
command = "set_project_fact"
fact_name = "Programming Language"
fact_value = "Python 3.12"
```

### Track Migration Status

```toml
[[actions]]
name = "migrate-config"
type = "file"
command = "copy"
source = "workflow:///new-config.yaml"
destination = "repository:///config.yaml"

[[actions]]
name = "mark-migration-complete"
type = "imbi"
command = "set_project_fact"
fact_name = "Config Migration Status"
fact_value = "Completed"
```

### Record Docker Image Version

```toml
[[actions]]
name = "update-dockerfile"
type = "claude"
prompt = "workflow:///prompts/update-docker.md"

[[actions]]
name = "record-base-image"
type = "imbi"
command = "set_project_fact"
fact_name = "Docker Base Image"
fact_value = "python:3.12-slim"
```

## Common Patterns

### Post-Migration Tracking

```toml
# Perform migration
[[actions]]
name = "migrate-to-new-framework"
type = "claude"
prompt = "workflow:///prompts/framework-migration.md"

# Record successful migration
[[actions]]
name = "update-framework-fact"
type = "imbi"
command = "set_project_fact"
fact_name = "Framework"
fact_value = "FastAPI 0.110"
```

### Conditional Updates Based on Facts

Use workflow filters to target projects by existing facts, then update after transformation:

```toml
# In workflow config.toml
[filter]
project_facts = {"Framework" = "Flask"}

# Actions update to FastAPI and record change
[[actions]]
name = "migrate-flask-to-fastapi"
type = "claude"
prompt = "workflow:///prompts/flask-to-fastapi.md"

[[actions]]
name = "update-framework-fact"
type = "imbi"
command = "set_project_fact"
fact_name = "Framework"
fact_value = "FastAPI"
```

## Implementation Status

Currently, Imbi actions are defined but not fully implemented. The `set_project_fact` command raises `NotImplementedError`.

**Planned Implementation:**

- Integration with Imbi API for fact updates
- Support for creating new facts
- Validation of fact names against Imbi schema
- Batch fact updates
- Conditional fact updates

## Integration with Other Actions

### With Claude Actions

```toml
[[actions]]
name = "ai-dependency-update"
type = "claude"
prompt = "workflow:///prompts/update-deps.md"

[[actions]]
name = "record-dependency-version"
type = "imbi"
command = "set_project_fact"
fact_name = "Primary Dependencies"
fact_value = "httpx>=0.27, pydantic>=2.0"
```

### With Shell Actions

```toml
[[actions]]
name = "detect-python-version"
type = "shell"
command = "python --version | cut -d' ' -f2"
working_directory = "repository:///"

[[actions]]
name = "record-detected-version"
type = "imbi"
command = "set_project_fact"
fact_name = "Python Version"
fact_value = "{{ shell_output }}"  # From previous action
```

## Future Enhancements

Planned additions to Imbi action functionality:

- **get_project_fact**: Retrieve fact values for conditional logic
- **delete_project_fact**: Remove obsolete facts
- **set_project_metadata**: Update project name, description, etc.
- **add_project_link**: Add external links to projects
- **update_project_type**: Change project classification
- **batch_update_facts**: Update multiple facts in one operation

## Best Practices

1. **Use After Transformations**: Record changes after successful transformations
2. **Semantic Fact Names**: Use clear, descriptive fact names that match Imbi's schema
3. **Version Tracking**: Record version numbers for dependencies and tools
4. **Status Tracking**: Use facts to track migration/upgrade status across projects
5. **Conditional Execution**: Combine with workflow filters to target specific project states

## See Also

- [Callable Actions](callable.md) - Direct Imbi API method calls (alternative approach)
- [Workflow Configuration](../workflows.md) - Using project facts in filters
- [Utility Actions](utility.md) - Logging and state management
