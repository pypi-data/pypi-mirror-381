# Debugging Workflows

Imbi Automations provides comprehensive debugging capabilities to troubleshoot workflow failures, including error preservation, detailed logging, and diagnostic tools.

## Quick Start

To debug a failing workflow, use these flags together:

```bash
imbi-automations config.toml workflows/failing-workflow \
  --all-projects \
  --preserve-on-error \
  --error-dir ./debug \
  --debug \
  --verbose
```

This will:
- `--preserve-on-error`: Save working directory state on failures
- `--error-dir ./debug`: Store error states in `./debug/`
- `--debug`: Enable DEBUG level logging (all log messages)
- `--verbose`: Show action start/end messages

## Debugging Flags

### --preserve-on-error

Preserves the complete working directory when a workflow fails, including:
- Cloned repository state
- Workflow resource files
- Extracted Docker files
- All intermediate files

**Usage:**
```bash
imbi-automations config.toml workflows/my-workflow \
  --all-projects \
  --preserve-on-error
```

**Default:** `false` (working directories are cleaned up)

**When to Use:**
- Investigating why a workflow failed
- Examining repository state at time of failure
- Debugging file operations
- Analyzing Claude action failures

### --error-dir

Specifies where to save preserved error states.

**Usage:**
```bash
imbi-automations config.toml workflows/my-workflow \
  --all-projects \
  --preserve-on-error \
  --error-dir /tmp/imbi-errors
```

**Default:** `./errors`

**Directory Structure:**
```
errors/
└── workflow-name/
    └── project-slug-timestamp/
        ├── repository/          # Cloned Git repository
        ├── workflow/            # Workflow resources
        ├── extracted/           # Docker extracted files (if any)
        ├── debug.log            # Complete DEBUG level logs
        └── other temporary files
```

**Example Paths:**
```
errors/
└── python39-project-fix/
    ├── api-service-20250103-143052/
    │   ├── repository/
    │   ├── workflow/
    │   └── debug.log
    └── consumer-app-20250103-143105/
        ├── repository/
        ├── workflow/
        └── debug.log
```

### --debug

Enables DEBUG level logging for all components, showing detailed operation traces.

**Usage:**
```bash
imbi-automations config.toml workflows/my-workflow \
  --all-projects \
  --debug
```

**Default:** `false` (INFO level)

**What Gets Logged:**
- All action executions with parameters
- HTTP requests/responses
- Git operations
- File operations
- Template rendering
- Claude API interactions
- Condition evaluations
- All internal state changes

**Example Output:**
```
2025-01-03 14:30:52 - imbi_automations.workflow_engine - DEBUG - Executing action: copy-gitignore
2025-01-03 14:30:52 - imbi_automations.actions.filea - DEBUG - Copying workflow:///.gitignore to repository:///.gitignore
2025-01-03 14:30:52 - imbi_automations.utils - DEBUG - Resolved path: /tmp/workflow123/workflow/.gitignore
2025-01-03 14:30:52 - imbi_automations.utils - DEBUG - Resolved path: /tmp/workflow123/repository/.gitignore
```

### --verbose

Shows action start/end messages at INFO level without full DEBUG output.

**Usage:**
```bash
imbi-automations config.toml workflows/my-workflow \
  --all-projects \
  --verbose
```

**Default:** `false`

**What Gets Logged:**
- Action start messages
- Action completion messages
- Major workflow milestones
- Success/failure summaries

**Example Output:**
```
2025-01-03 14:30:50 - imbi_automations.workflow_engine - INFO - Starting action: backup-files
2025-01-03 14:30:52 - imbi_automations.workflow_engine - INFO - Completed action: backup-files
2025-01-03 14:30:52 - imbi_automations.workflow_engine - INFO - Starting action: ai-refactor
```

### --exit-on-error

Stop processing immediately when any project fails instead of continuing with remaining projects.

**Usage:**
```bash
imbi-automations config.toml workflows/my-workflow \
  --all-projects \
  --exit-on-error
```

**Default:** `false` (continue with other projects)

**When to Use:**
- Testing workflows on small batches
- CI/CD environments
- When failures are critical
- Debugging specific project issues

## debug.log File

When `--preserve-on-error` is enabled, a `debug.log` file is automatically created in each error directory containing ALL DEBUG level logs for that specific project execution.

### Contents

The `debug.log` file includes:
- Complete action execution trace
- All HTTP API requests and responses
- File operations with full paths
- Git commands and output
- Template rendering details
- Claude/Anthropic API interactions
- Error messages and stack traces
- Timing information

### Format

```
2025-01-03 14:30:50,123 - imbi_automations.controller - INFO - Processing my-project (123)
2025-01-03 14:30:50,456 - imbi_automations.git - DEBUG - Cloning repository: https://github.com/org/repo.git
2025-01-03 14:30:52,789 - imbi_automations.workflow_engine - DEBUG - Executing action: copy-files
2025-01-03 14:30:52,890 - imbi_automations.actions.filea - DEBUG - Copying workflow:///templates/ to repository:///config/
2025-01-03 14:30:53,123 - imbi_automations.actions.filea - ERROR - Failed to copy: Source directory not found
```

### Location

```bash
# Default location
./errors/workflow-name/project-slug-timestamp/debug.log

# Custom error-dir
/tmp/debug/workflow-name/project-slug-timestamp/debug.log
```

### Per-Project Isolation

Each project execution gets its own `debug.log` file, even when running workflows concurrently with `--max-concurrency > 1`. This is achieved using Python's `contextvars` to isolate log captures per async task.

## Error Directory Contents

When a workflow fails and `--preserve-on-error` is enabled, the error directory contains:

### repository/

Complete clone of the Git repository at the point of failure:
- All files in their current state
- `.git/` directory with full history
- Working tree changes (staged and unstaged)
- Any files created by workflow actions

**Use Cases:**
- Examine file modifications made by actions
- Check what Claude Code changed
- Review git history and commits
- Test fixes locally

```bash
cd errors/workflow-name/project-slug-timestamp/repository/
git log
git diff HEAD
git status
```

### workflow/

Copy of workflow resources:
- Template files
- Prompt files
- Static resources
- Any files copied from workflow directory

**Use Cases:**
- Verify template content
- Check prompt files
- Review workflow resources

### extracted/ (if present)

Files extracted from Docker containers by docker actions:
- Configuration files
- Binary artifacts
- Library files

**Use Cases:**
- Verify Docker extraction worked
- Check extracted file contents
- Debug docker action issues

### debug.log

Complete DEBUG level logs (see above section).

### Other Files

Any temporary files created during workflow execution:
- Action-specific output files
- Intermediate processing files
- Failure indicator files (e.g., `ACTION_FAILED`)

## Common Debugging Scenarios

### Debugging Failed Actions

**Scenario:** An action fails and you need to understand why.

**Steps:**
1. Run with error preservation:
   ```bash
   imbi-automations config.toml workflows/my-workflow \
     --project-id 123 \
     --preserve-on-error \
     --debug
   ```

2. Check console output for immediate errors

3. Examine the error directory:
   ```bash
   cd errors/my-workflow/project-name-*
   cat debug.log | grep ERROR
   ```

4. Review repository state:
   ```bash
   cd repository/
   git status
   git log -1
   ```

5. Check for failure files:
   ```bash
   find . -name "*FAILED"
   cat ACTION_FAILED  # If exists
   ```

### Debugging Claude Actions

**Scenario:** Claude Code action fails or produces unexpected results.

**Steps:**
1. Enable full debugging:
   ```bash
   imbi-automations config.toml workflows/claude-workflow \
     --project-id 123 \
     --preserve-on-error \
     --debug \
     --verbose
   ```

2. Check `debug.log` for Claude interactions:
   ```bash
   cd errors/claude-workflow/project-*
   grep -A 10 "Claude" debug.log
   grep -A 5 "Anthropic" debug.log
   ```

3. Review the prompt sent to Claude:
   ```bash
   grep -B 5 -A 20 "Execute agent prompt" debug.log
   ```

4. Check for failure files:
   ```bash
   ls repository/*FAILED
   cat repository/ACTION_FAILED
   ```

5. Examine repository changes:
   ```bash
   cd repository/
   git diff
   ```

### Debugging File Actions

**Scenario:** File copy/move operations aren't working as expected.

**Steps:**
1. Run with verbose debugging:
   ```bash
   imbi-automations config.toml workflows/file-workflow \
     --project-id 123 \
     --preserve-on-error \
     --debug
   ```

2. Check resolved paths in `debug.log`:
   ```bash
   grep "Resolved path" debug.log
   grep "Copying\|Moving\|Writing" debug.log
   ```

3. Verify file existence:
   ```bash
   cd errors/file-workflow/project-*/
   ls -laR repository/
   ls -laR workflow/
   ```

4. Check for permission or path errors:
   ```bash
   grep "Permission denied\|No such file" debug.log
   ```

### Debugging Template Actions

**Scenario:** Templates aren't rendering correctly or variables are undefined.

**Steps:**
1. Enable debugging:
   ```bash
   imbi-automations config.toml workflows/template-workflow \
     --project-id 123 \
     --preserve-on-error \
     --debug
   ```

2. Check template rendering in logs:
   ```bash
   grep "Template\|Jinja2" debug.log
   ```

3. Examine rendered output:
   ```bash
   cd errors/template-workflow/project-*/repository/
   cat rendered-file.yaml
   ```

4. Review workflow template files:
   ```bash
   cd ../workflow/
   cat template-file.j2
   ```

5. Check for undefined variable errors:
   ```bash
   grep "undefined\|UndefinedError" debug.log
   ```

### Debugging Shell Actions

**Scenario:** Shell commands fail or produce unexpected output.

**Steps:**
1. Enable debugging:
   ```bash
   imbi-automations config.toml workflows/shell-workflow \
     --project-id 123 \
     --preserve-on-error \
     --debug
   ```

2. Check command execution in logs:
   ```bash
   grep "Executing shell command\|Command stdout\|Command stderr" debug.log
   ```

3. Re-run command manually:
   ```bash
   cd errors/shell-workflow/project-*/repository/
   # Copy command from debug.log and run it
   pytest tests/ -v
   ```

4. Check exit codes:
   ```bash
   grep "exit code" debug.log
   ```

### Debugging Concurrent Execution

**Scenario:** Running with `--max-concurrency > 1` and need to debug specific project.

**Steps:**
1. First, identify the failing project in normal execution
2. Re-run with just that project:
   ```bash
   imbi-automations config.toml workflows/my-workflow \
     --project-id 123 \
     --preserve-on-error \
     --debug \
     --exit-on-error
   ```

3. Each project gets isolated `debug.log` even in concurrent mode
4. Check error directory for all failed projects:
   ```bash
   ls -ltr errors/my-workflow/
   ```

## Configuration File Debugging

You can also set error preservation in `config.toml`:

```toml
preserve_on_error = true
error_dir = "/var/log/imbi-errors"
```

**Note:** CLI flags override config file settings.

## Log Levels

Imbi Automations uses Python's standard logging levels:

| Level | Description | When to Use |
|-------|-------------|-------------|
| DEBUG | All operations and internal state | Debugging failures |
| INFO | Major milestones and progress | Normal operation |
| WARNING | Recoverable issues | Monitoring |
| ERROR | Action failures | Alert on issues |
| CRITICAL | Fatal errors | System failures |

**Set via CLI:**
```bash
# DEBUG level
--debug

# INFO level (default)
# No flag needed

# INFO level with action details
--verbose
```

## Performance Impact

### --preserve-on-error

**Impact:** Minimal during execution, significant on failure
- No overhead during successful workflows
- On failure: Copies entire working directory (can be large)
- Storage: Requires disk space for preserved directories

**Recommendation:** Enable for debugging, disable for production batch processing

### --debug

**Impact:** Moderate logging overhead
- Increases log volume significantly
- Slightly slower due to additional logging calls
- Memory impact from buffering logs

**Recommendation:** Use for troubleshooting specific issues, not for large batch runs

### --verbose

**Impact:** Minimal
- Only logs action start/end messages
- Negligible performance impact

**Recommendation:** Safe to use in production

## Cleaning Up Error Directories

Error directories accumulate over time. Clean them periodically:

```bash
# Remove all error directories
rm -rf errors/

# Remove errors older than 7 days
find errors/ -type d -mtime +7 -exec rm -rf {} +

# Remove errors for specific workflow
rm -rf errors/workflow-name/

# Keep only latest N errors per workflow
cd errors/workflow-name/
ls -t | tail -n +6 | xargs rm -rf
```

## Best Practices

1. **Start Small**: Debug single projects before batch runs
   ```bash
   --project-id 123 --preserve-on-error --debug
   ```

2. **Isolate Issues**: Use `--exit-on-error` when debugging
   ```bash
   --all-projects --exit-on-error --preserve-on-error
   ```

3. **Review Logs First**: Check `debug.log` before examining files
   ```bash
   grep ERROR errors/workflow/project/debug.log
   ```

4. **Clean Up Regularly**: Remove old error directories
   ```bash
   find errors/ -mtime +7 -delete
   ```

5. **Use Specific Targeting**: Debug exact failing project
   ```bash
   --project-id 123  # Instead of --all-projects
   ```

6. **Disable in Production**: Don't preserve errors for large batch runs
   ```bash
   # Production: no preserve-on-error
   imbi-automations config.toml workflows/prod --all-projects
   ```

7. **Combine Flags Effectively**:
   ```bash
   # Maximum debugging
   --preserve-on-error --debug --verbose --exit-on-error

   # Light debugging
   --verbose

   # Specific issue
   --project-id 123 --preserve-on-error --debug
   ```

## Troubleshooting the Debugger

### Error Directories Not Created

**Problem:** `--preserve-on-error` set but no directories in `errors/`

**Causes:**
- Workflow succeeded (no errors to preserve)
- Insufficient permissions to create directories
- Disk space full

**Solution:**
```bash
# Check permissions
ls -ld errors/
mkdir -p errors/test

# Check disk space
df -h .

# Try explicit error-dir
--error-dir /tmp/imbi-errors
```

### debug.log Missing or Empty

**Problem:** Error directory created but `debug.log` missing

**Causes:**
- Failure occurred before logging started
- Logging not properly initialized
- Concurrent execution issue

**Solution:**
```bash
# Run single-threaded
--max-concurrency 1

# Ensure debug logging
--debug --preserve-on-error
```

### Too Much Log Output

**Problem:** `--debug` generates too much output

**Solution:**
```bash
# Use --verbose instead for less output
--verbose

# Or filter debug output
--debug 2>&1 | grep -v "anthropic\|httpx\|httpcore"
```

## See Also

- [Configuration](configuration.md) - Configure error directories in config.toml
- [Architecture](architecture.md) - Understanding workflow execution
- [Actions](actions/index.md) - Action-specific debugging tips
