# Nexus - Intelligent Agentic File Assistant

[![PyPI version](https://badge.fury.io/py/nexus-ai-agent.svg)](https://pypi.org/project/nexus-ai-agent/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful AI agent powered by Claude that plans and executes complex file operations step-by-step with built-in safety mechanisms.

## 🚀 Quick Start

```bash
pip install nexus-ai-agent
```

**Windows:** Use `python -m cli "your task"` (the `nexus` command requires PATH setup - [see why](#windows-setup))  
**Linux/Mac:** Use `nexus "your task"`

## Features

### Agentic Planning

- **Automatic Planning**: Creates a TODO list before executing tasks
- **Step-by-Step Execution**: Executes each step methodically
- **Loop Detection**: Prevents infinite loops and repeated actions
- **Adaptive Planning**: Adjusts plan if something fails
- **Progress Tracking**: Shows thinking, progress, and stats

### Smart File Operations

- **Create/Read/Edit/Delete files** with intelligent handling
- **Smart Reading**: Line ranges, previews, search within files
- **Smart Search**: Find files by name pattern or content
- **Directory Exclusions**: Automatically skips .git, node_modules, **pycache**, etc.
- **Token Optimization**: 10K character limit prevents token explosion

### Safety Mechanisms

- **Iteration Limits**: Max 15 iterations to prevent runaway
- **Loop Detection**: Detects and warns about repeated actions
- **Action Tracking**: Prevents duplicate operations
- **Error Handling**: Graceful failure with helpful messages

## Project Structure

```
agent/
├── agent.py              # Core agentic logic with planning
├── tools.py              # Tool definitions for Anthropic API
├── tool_functions.py     # Tool implementations
├── examples.py           # Usage examples
├── .env                  # Configuration (API key)
└── README.md            # This file
```

## Quick Start

### 1. Installation

```bash
pip install nexus-ai-agent
```

**Source installation:**

```bash
git clone https://github.com/Remote-Skills/nexus.git
cd nexus
pip install -e .
```

### 2. Configuration

Create a `.env` file in your working directory:

```env
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
ANTHROPIC_MAX_TOKENS=4096
```

### 3. Usage

**⚠️ Windows Users: Use `python -m cli` instead of `nexus`**

The `nexus` command requires Python's Scripts folder in your PATH. On Windows, use:

```powershell
python -m cli "your task"
python -m cli  # Interactive mode
```

To permanently enable the `nexus` command, see [Windows Setup](#windows-setup) below.

---

#### CLI Mode (Recommended)

**Linux/Mac:**
```bash
nexus "Create a Python web app with Flask"
nexus  # Interactive mode
```

**Windows (or if `nexus` not found):**
```powershell
python -m cli "Create a Python web app with Flask"
python -m cli  # Interactive mode
```

#### Python API - Agentic Mode

```python
from agent import chat_with_tools_agentic

# Complex multi-step task with automatic planning
chat_with_tools_agentic(
    "Create a Python project with main.py, requirements.txt, and README.md. "
    "The main.py should have a hello world function."
)
```

#### Python API - Simple Mode

```python
from agent import chat_with_tools

# Direct tool usage without planning
chat_with_tools("Create a file called test.txt with hello world")
```

## How It Works

### Agentic Mode Flow

```
User Request
    ↓
1. Agent analyzes task
    ↓
2. Creates TODO listi/plan
    ↓
3. Shows plan to user
    ↓
4. Executes step-by-step
    ↓
5. Checks results
    ↓
6. Adapts if needed
    ↓
7. Final summary
```

### Safety Features

1. **Loop Detection**: Tracks all actions and prevents repeats
2. **Iteration Limit**: Max 15 iterations (configurable)
3. **Pattern Detection**: Warns if same tools used 3+ times
4. **Action History**: Remembers completed actions

## Available Tools

| Tool           | Description                                     |
| -------------- | ----------------------------------------------- |
| `create_file`  | Create files with content                       |
| `read_file`    | Smart reading with line ranges, search, preview |
| `edit_file`    | Replace or append content                       |
| `delete_file`  | Delete files                                    |
| `list_files`   | List directory contents (excludes build dirs)   |
| `smart_search` | Search by filename or content (recursive)       |

### Smart Reading Features

```python
# Preview a large file
"Preview the file 'large_dataset.csv'"

# Read specific lines
"Read lines 100 to 200 from 'app.log'"

# Search within file
"Find all ERROR messages in 'debug.log'"

# Character limit
"Read config.json but limit to 5000 characters"
```

## Example Tasks

### Project Creation

```python
chat_with_tools_agentic(
    "Create a Flask web app with proper structure: "
    "app.py, requirements.txt, README.md, and a templates folder"
)
```

### Code Analysis

```python
chat_with_tools_agentic(
    "Analyze all Python files, find TODO comments, "
    "and create a summary in todos.md"
)
```

### Refactoring

```python
chat_with_tools_agentic(
    "Find all files with 'old_function_name' and create a plan "
    "to refactor them to 'new_function_name'"
)
```

## Best Practices

### Do:

- Use agentic mode for complex multi-step tasks
- Let the agent create a plan first
- Provide clear, specific task descriptions
- Break down very large tasks into smaller ones

### Don't:

- Request tasks that would require >15 iterations
- Ask for operations on extremely large files without using smart reading
- Request recursive operations without clear boundaries

## Debugging

The agent shows detailed output:

- **Agent Thinking**: Planning and reasoning
- **Tool Used**: Which tool is being called
- **Input**: Tool parameters
- **Result**: Tool output
- **Stats**: Iterations and actions performed

## Safety & Limitations

- **Iteration Limit**: 15 iterations maximum
- **File Size**: 50KB+ files trigger warnings
- **Character Limit**: 10K default for reads
- **Loop Detection**: Prevents infinite loops
- **Excluded Dirs**: Skips .git, node_modules, etc.

## Windows Setup

### Why `nexus` command doesn't work on Windows

After `pip install nexus-ai-agent`, the `nexus` command is installed to Python's Scripts folder (e.g., `C:\Users\YourName\AppData\Local\Programs\Python\Python312\Scripts\`). If this folder isn't in your Windows PATH, the command won't be recognized.

### Solution 1: Use `python -m cli` (Easiest - Works Immediately)

```powershell
python -m cli "your task"
```

This works without any setup! Just use this instead of `nexus`.

### Solution 2: Add Scripts to PATH (One-time setup for `nexus` command)

**Step 1: Find your Scripts folder**
```powershell
python -c "import os, sys; print(os.path.join(sys.prefix, 'Scripts'))"
```

**Step 2: Add to PATH**
1. Press `Win + X` → Select "System"
2. Click "Advanced system settings"  
3. Click "Environment Variables"
4. Under "User variables", select "Path" → Click "Edit"
5. Click "New"
6. Paste your Scripts folder path
7. Click "OK" on all windows
8. **Restart PowerShell**

**Step 3: Test**
```powershell
nexus "test task"
```

### Solution 3: Create PowerShell Alias

Add to your PowerShell profile (`notepad $PROFILE`):

```powershell
function nexus { python -m cli $args }
```

Save, reload (`. $PROFILE`), and now `nexus` works!

**For detailed troubleshooting, see:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | [WINDOWS_CLI_FIX.md](WINDOWS_CLI_FIX.md)

## Contributing

Feel free to add new tools or improve the planning logic!

## License

MIT License - Feel free to use and modify!
