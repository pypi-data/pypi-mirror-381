"""
Nexus - Intelligent Agentic File Assistant
A powerful AI agent that thinks, plans, and executes complex file operations.
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.prompt import Prompt, Confirm
from rich.live import Live
from rich.layout import Layout
from rich import box
from rich.text import Text
import json
import time
from datetime import datetime
from agent import client, tools, process_tool_call, ANTHROPIC_MODEL, ANTHROPIC_MAX_TOKENS
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Initialize Rich console
console = Console()

class TokenTracker:
    """Track token usage across the session"""
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.requests_count = 0
        self.start_time = datetime.now()
    
    def add_usage(self, input_tokens, output_tokens):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.requests_count += 1
    
    def get_stats(self):
        total = self.total_input_tokens + self.total_output_tokens
        duration = (datetime.now() - self.start_time).total_seconds()
        
        # Rough cost estimation (adjust based on actual pricing)
        # Claude Sonnet 4: ~$3 per million input tokens, ~$15 per million output tokens
        cost_input = (self.total_input_tokens / 1_000_000) * 3.0
        cost_output = (self.total_output_tokens / 1_000_000) * 15.0
        total_cost = cost_input + cost_output
        
        return {
            'input': self.total_input_tokens,
            'output': self.total_output_tokens,
            'total': total,
            'requests': self.requests_count,
            'duration': duration,
            'cost': total_cost
        }

# Global token tracker
token_tracker = TokenTracker()

def print_banner():
    """Display welcome banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║                      N E X U S                            ║
    ║                                                           ║
    ║        Intelligent Agentic File Assistant v1.0            ║
    ║        Planning • Execution • Safety • Transparency       ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    console.print(banner, style="bold cyan")
    console.print(f"Model: [yellow]{ANTHROPIC_MODEL}[/yellow]", justify="center")
    console.print(f"Max Tokens: [yellow]{ANTHROPIC_MAX_TOKENS}[/yellow]\n", justify="center")

def print_task_header(task):
    """Display task in a nice panel"""
    console.print()
    panel = Panel(
        f"[bold white]{task}[/bold white]",
        title="[bold cyan]TASK[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(panel)

def print_thinking(text, iteration, max_iterations):
    """Display agent's thinking process"""
    progress_bar = "█" * iteration + "░" * (max_iterations - iteration)
    
    panel = Panel(
        Markdown(text),
        title=f"[bold magenta]THINKING[/bold magenta] [{iteration}/{max_iterations}] {progress_bar}",
        border_style="magenta",
        padding=(1, 2)
    )
    console.print(panel)

def print_tool_call(tool_name, tool_input, result=None):
    """Display tool execution with syntax highlighting"""
    # Tool header
    console.print(f"\n[bold cyan]TOOL:[/bold cyan] [yellow]{tool_name}[/yellow]")
    
    # Input parameters
    if tool_input:
        input_json = json.dumps(tool_input, indent=2)
        syntax = Syntax(input_json, "json", theme="monokai", line_numbers=False)
        console.print(Panel(syntax, title="INPUT", border_style="blue", padding=(0, 1)))
    
    # Result
    if result:
        # Truncate long results
        display_result = result if len(result) < 500 else result[:500] + "\n... (truncated)"
        console.print(Panel(
            display_result,
            title="RESULT",
            border_style="green",
            padding=(0, 1)
        ))

def print_final_response(response, stats):
    """Display final response with stats"""
    console.print()
    
    # Response
    panel = Panel(
        Markdown(response),
        title="[bold green]COMPLETED[/bold green]",
        border_style="green",
        padding=(1, 2)
    )
    console.print(panel)
    
    # Stats table
    table = Table(title="Execution Statistics", box=box.ROUNDED, show_header=False)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="yellow")
    
    table.add_row("Iterations", str(stats['iterations']))
    table.add_row("Unique Actions", str(stats['actions']))
    table.add_row("Duration", f"{stats.get('duration', 0):.2f}s")
    
    console.print(table)

def print_token_stats():
    """Display token usage statistics"""
    stats = token_tracker.get_stats()
    
    table = Table(title="Token Usage & Cost", box=box.ROUNDED)
    table.add_column("Metric", style="cyan", justify="left")
    table.add_column("Value", style="yellow", justify="right")
    
    table.add_row("Input Tokens", f"{stats['input']:,}")
    table.add_row("Output Tokens", f"{stats['output']:,}")
    table.add_row("Total Tokens", f"{stats['total']:,}")
    table.add_row("API Requests", str(stats['requests']))
    table.add_row("Session Duration", f"{stats['duration']:.1f}s")
    table.add_row("Estimated Cost", f"${stats['cost']:.4f}")
    
    console.print()
    console.print(table)

def print_warning(message):
    """Display warning message"""
    console.print(f"\n[bold yellow]WARNING:[/bold yellow] {message}")

def print_error(message):
    """Display error message"""
    console.print(f"\n[bold red]ERROR:[/bold red] {message}")

def chat_with_tools_cli(user_message, max_iterations=15):
    """
    CLI version of agentic chat with beautiful output
    """
    print_task_header(user_message)
    
    system_prompt = """You are an agentic AI assistant that thinks step-by-step and creates plans before executing.

For every user request:
1. First, analyze the task and create a clear TODO list/plan
2. Show your plan to the user before executing
3. Execute each step one by one, checking results
4. If something fails, adapt your plan
5. Keep track of what you've already done to avoid repeating actions
6. When all steps are complete, provide a final summary

IMPORTANT RULES:
- Always create a plan before using tools
- Don't repeat the same action multiple times unless needed
- If you've already read a file, use that information instead of reading again
- If a tool fails, try a different approach
- After completing the task, provide a clear summary of what was done"""

    messages = [{"role": "user", "content": user_message}]
    
    iteration_count = 0
    tool_usage_history = []
    completed_actions = set()
    start_time = time.time()
    
    # Agentic loop
    while iteration_count < max_iterations:
        iteration_count += 1
        
        try:
            response = client.messages.create(
                model=ANTHROPIC_MODEL,
                max_tokens=ANTHROPIC_MAX_TOKENS,
                tools=tools,
                system=system_prompt,
                tool_choice={"type": "auto"},
                messages=messages
            )
            
            # Track token usage
            token_tracker.add_usage(
                response.usage.input_tokens,
                response.usage.output_tokens
            )
            
            # Extract thinking
            thinking_text = ""
            for block in response.content:
                if hasattr(block, "text") and block.text:
                    thinking_text += block.text
            
            if thinking_text:
                print_thinking(thinking_text, iteration_count, max_iterations)
            
            # Add assistant's response to messages
            messages.append({"role": "assistant", "content": response.content})
            
            # Check if Claude wants to use tools
            if response.stop_reason == "tool_use":
                tool_results = []
                current_tools_used = []
                
                for block in response.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input
                        
                        # Create action signature
                        action_signature = f"{tool_name}:{json.dumps(tool_input, sort_keys=True)}"
                        current_tools_used.append(action_signature)
                        
                        # Check for repeated actions
                        if action_signature in completed_actions:
                            print_warning("This exact action was already performed!")
                            result = "Note: This action was already performed earlier. Please use the previous result."
                        else:
                            # Execute the tool
                            result = process_tool_call(tool_name, tool_input)
                            completed_actions.add(action_signature)
                        
                        print_tool_call(tool_name, tool_input, result)
                        
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        })
                
                # Track tool usage
                tool_usage_history.append(current_tools_used)
                
                # Detect loops
                if len(tool_usage_history) >= 3:
                    last_three = tool_usage_history[-3:]
                    if last_three[0] == last_three[1] == last_three[2]:
                        print_warning("Potential infinite loop detected!")
                        messages.append({
                            "role": "user", 
                            "content": tool_results + [{
                                "type": "text",
                                "text": "WARNING: You seem to be repeating the same actions. Please complete the task or explain why you cannot proceed."
                            }]
                        })
                    else:
                        messages.append({"role": "user", "content": tool_results})
                else:
                    messages.append({"role": "user", "content": tool_results})
                
            else:
                # Extract final response
                final_response = ""
                for block in response.content:
                    if hasattr(block, "text"):
                        final_response += block.text
                
                duration = time.time() - start_time
                stats = {
                    'iterations': iteration_count,
                    'actions': len(completed_actions),
                    'duration': duration
                }
                
                print_final_response(final_response, stats)
                return final_response
        
        except Exception as e:
            print_error(f"An error occurred: {str(e)}")
            return None
    
    # Max iterations reached
    print_warning(f"Maximum iterations ({max_iterations}) reached!")
    return "Task incomplete: Maximum iteration limit reached."

def interactive_mode():
    """Interactive CLI mode"""
    print_banner()
    
    console.print("[dim]Type 'exit' or 'quit' to leave, 'stats' for token usage, 'help' for commands[/dim]\n")
    
    while True:
        try:
            # Get user input
            task = Prompt.ask("\n[bold cyan]> What would you like me to do?[/bold cyan]")
            
            if task.lower() in ['exit', 'quit', 'q']:
                print_token_stats()
                console.print("\n[bold cyan]Session ended. Goodbye![/bold cyan]\n")
                break
            
            if task.lower() == 'stats':
                print_token_stats()
                continue
            
            if task.lower() == 'help':
                print_help()
                continue
            
            if not task.strip():
                continue
            
            # Execute task
            chat_with_tools_cli(task)
            
        except KeyboardInterrupt:
            console.print("\n\n[yellow]Interrupted by user[/yellow]")
            if Confirm.ask("Exit the application?"):
                print_token_stats()
                console.print("\n[bold cyan]Session ended.[/bold cyan]\n")
                break
        except Exception as e:
            print_error(f"Unexpected error: {str(e)}")

def print_help():
    """Display help information"""
    help_text = """
# Available Commands

- **exit/quit** - Exit the application
- **stats** - Show token usage and cost statistics
- **help** - Show this help message

# Example Tasks

- "Create a Python project with main.py and README.md"
- "Search for TODO comments in all Python files"
- "Preview the file large_data.csv"
- "List all files excluding build directories"
"""
    console.print(Panel(Markdown(help_text), title="[bold cyan]HELP[/bold cyan]", border_style="cyan"))

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Single command mode
        task = " ".join(sys.argv[1:])
        print_banner()
        chat_with_tools_cli(task)
        print_token_stats()
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
