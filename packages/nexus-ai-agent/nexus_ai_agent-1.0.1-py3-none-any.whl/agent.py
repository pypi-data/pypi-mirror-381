import anthropic
import json
import os
from dotenv import load_dotenv
from tools import tools
from tool_functions import tool_functions

# Load environment variables from .env file
load_dotenv()
# Read the env variable for the API key
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable.")

# Read the env variable for the model
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")
ANTHROPIC_MAX_TOKENS = int(os.getenv("ANTHROPIC_MAX_TOKENS", "4096"))

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def process_tool_call(tool_name, tool_input):
    """Execute the appropriate tool function"""
    func = tool_functions.get(tool_name)
    if func:
        return func(**tool_input)
    return f"Unknown tool: {tool_name}"

def chat_with_tools_agentic(user_message, max_iterations=15):
    """
    Enhanced agentic function that creates a plan first, then executes step-by-step.
    Includes loop detection and iteration limits to avoid infinite loops.
    """
    print(f"\n{'='*60}")
    print(f"🎯 User Task: {user_message}")
    print(f"{'='*60}\n")
    
    # System prompt to encourage planning
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
    tool_usage_history = []  # Track tools used to detect loops
    completed_actions = set()  # Track completed actions
    
    # Agentic loop with safeguards
    while iteration_count < max_iterations:
        iteration_count += 1
        print(f"\n📍 Iteration {iteration_count}/{max_iterations}")
        
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=ANTHROPIC_MAX_TOKENS,
            tools=tools,
            system=system_prompt,
            tool_choice={"type": "auto"},
            messages=messages
        )
        
        print(f"Stop Reason: {response.stop_reason}")
        
        # Extract and show thinking/planning
        for block in response.content:
            if hasattr(block, "text") and block.text:
                print(f"\n💭 Agent Thinking:\n{block.text}\n")
        
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
                    
                    # Create action signature for loop detection
                    action_signature = f"{tool_name}:{json.dumps(tool_input, sort_keys=True)}"
                    current_tools_used.append(action_signature)
                    
                    print(f"\n🔧 Tool Used: {tool_name}")
                    print(f"📥 Input: {json.dumps(tool_input, indent=2)}")
                    
                    # Check for repeated actions (loop detection)
                    if action_signature in completed_actions:
                        print(f"⚠️  Warning: This exact action was already performed!")
                        result = "Note: This action was already performed earlier. Please use the previous result instead of repeating."
                    else:
                        # Execute the tool
                        result = process_tool_call(tool_name, tool_input)
                        completed_actions.add(action_signature)
                        print(f"📤 Result: {result}\n")
                    
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            
            # Track tool usage for loop detection
            tool_usage_history.append(current_tools_used)
            
            # Detect potential infinite loops (same tools used 3+ times in a row)
            if len(tool_usage_history) >= 3:
                last_three = tool_usage_history[-3:]
                if last_three[0] == last_three[1] == last_three[2]:
                    print("\n⚠️  WARNING: Potential infinite loop detected!")
                    messages.append({
                        "role": "user", 
                        "content": tool_results + [{
                            "type": "text",
                            "text": "WARNING: You seem to be repeating the same actions. Please review what you've already done and either complete the task or explain why you cannot proceed."
                        }]
                    })
                else:
                    messages.append({"role": "user", "content": tool_results})
            else:
                messages.append({"role": "user", "content": tool_results})
            
        else:
            # Claude is done using tools, extract final response
            final_response = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_response += block.text
            
            print(f"\n{'='*60}")
            print(f"✅ Final Response:")
            print(f"{'='*60}")
            print(f"{final_response}\n")
            print(f"📊 Stats: {iteration_count} iterations, {len(completed_actions)} unique actions")
            print(f"{'='*60}\n")
            return final_response
    
    # Max iterations reached
    print(f"\n⚠️  Maximum iterations ({max_iterations}) reached!")
    return "Task incomplete: Maximum iteration limit reached. Please try breaking down the task into smaller steps."


def chat_with_tools(user_message):
    """
    Simple function to interact with Claude using tools (backward compatibility).
    For better agentic behavior, use chat_with_tools_agentic() instead.
    """
    print(f"\n{'='*60}")
    print(f"User: {user_message}")
    print(f"{'='*60}\n")
    
    messages = [{"role": "user", "content": user_message}]
    
    # Agentic loop - keep going until Claude stops using tools
    while True:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=ANTHROPIC_MAX_TOKENS,
            tools=tools,
            tool_choice={"type": "auto"},  # Let Claude decide automatically
            messages=messages
        )
        
        print(f"Stop Reason: {response.stop_reason}")
        
        # Add assistant's response to messages
        messages.append({"role": "assistant", "content": response.content})
        
        # Check if Claude wants to use tools
        if response.stop_reason == "tool_use":
            # Process all tool uses in the response
            tool_results = []
            
            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    
                    print(f"\nTool Used: {tool_name}")
                    print(f"Tool Input: {json.dumps(tool_input, indent=2)}")
                    
                    # Execute the tool
                    result = process_tool_call(tool_name, tool_input)
                    print(f"Tool Result: {result}\n")
                    
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            
            # Add tool results to messages and continue the loop
            messages.append({"role": "user", "content": tool_results})
            
        else:
            # Claude is done using tools, extract final response
            final_response = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_response += block.text
            
            print(f"\nClaude: {final_response}\n")
            return final_response