# Nexus

**Intelligent Agentic File Assistant** - A powerful AI agent that thinks, plans, and executes complex file operations.

## Name Origin

**Nexus** (Latin: connection, link) - represents the intelligent connection between human intent and automated execution. The agent acts as a nexus point, bridging complex tasks with systematic, intelligent action.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY

# Interactive mode
python cli.py

# Single command mode
python cli.py "Create a Python project with tests and docs"
```

## Features

### Agentic Intelligence
- Creates action plans before executing
- Thinks step-by-step through complex tasks
- Adapts when errors occur
- Tracks completed actions

### Safety Mechanisms
- Maximum iteration limits
- Duplicate action detection
- Loop pattern recognition
- Auto-excludes build directories

### Developer Experience
- Clean, modern CLI with Rich library
- Real-time token usage tracking
- Cost estimation per session
- Syntax-highlighted output
- Progress indicators

### Smart File Operations
- Preview mode (500 chars)
- Line range reading
- Content search within files
- 10K character safety limit
- Automatic directory exclusions

## CLI Commands

```bash
# Interactive mode
python cli.py

# Single command
python cli.py "your task here"

# Help
python cli.py help
```

### Available Commands (Interactive Mode)
- `exit/quit` - Exit the application
- `stats` - Show token usage and costs
- `help` - Display help information

## Example Tasks

```bash
# Project creation
python cli.py "Create a Flask API with proper structure"

# Code analysis
python cli.py "Find all TODO comments and create a summary"

# Smart file reading
python cli.py "Preview large_dataset.csv and analyze first 500 characters"

# Search operations
python cli.py "Search for ERROR in all log files"
```

## Token Tracking

Nexus automatically tracks:
- Input tokens
- Output tokens
- API request count
- Session duration
- Estimated cost (Claude Sonnet 4 pricing)

View stats anytime with the `stats` command.

## Safety Features

- **Iteration Limit**: Max 15 iterations (configurable)
- **Loop Detection**: Prevents infinite loops
- **Action Tracking**: No duplicate operations
- **File Size Warnings**: Alerts for files > 50KB
- **Directory Exclusions**: Skips .git, node_modules, __pycache__, etc.

## Configuration

Environment variables (`.env`):
```env
ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
ANTHROPIC_MAX_TOKENS=4096
```

## Architecture

```
nexus/
├── cli.py              # Modern CLI interface
├── agent.py            # Core agentic logic
├── tools.py            # Tool definitions
├── tool_functions.py   # Tool implementations
└── examples.py         # Usage examples
```

## Requirements

```
anthropic>=0.25.0
python-dotenv>=1.0.0
rich>=13.0.0
```

## License

MIT License - See LICENSE file for details

## Credits

Powered by Anthropic's Claude and built for developers who value clean, intelligent automation.
