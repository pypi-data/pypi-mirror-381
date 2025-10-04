# Claude Agent SDK for Python - Complete API Reference

**Source**: https://docs.claude.com/en/api/agent-sdk/python.md
**Last Updated**: 2025-10-03
**SDK Version**: 1.0.0+

---

## Installation

```bash
pip install claude-agent-sdk
```

**Prerequisites:**
- Python 3.10+
- Node.js
- Claude Code CLI: `npm install -g @anthropic-ai/claude-code`

---

## Core Concepts

### Two Interaction Methods

#### 1. `query()` - Single-Session Interactions
- Stateless, one-off queries
- Returns `AsyncIterator` of messages
- Simpler for basic use cases
- Good for serverless/lambda functions

#### 2. `ClaudeSDKClient` - Continuous Conversations
- Stateful, persistent sessions
- Bidirectional communication
- Supports custom tools and hooks
- Full control over conversation lifecycle

---

## API Reference

### `query()` Function

**Signature:**
```python
async def query(
    prompt: str,
    options: ClaudeAgentOptions | None = None
) -> AsyncIterator[Message]
```

**Parameters:**
- `prompt`: User message to send to Claude
- `options`: Optional configuration (see ClaudeAgentOptions below)

**Returns:** AsyncIterator yielding message objects

**Example:**
```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a Python expert",
        allowed_tools=["Read", "Write", "Bash"],
        permission_mode="acceptEdits"
    )

    async for message in query(prompt="Create hello.py", options=options):
        print(message)

asyncio.run(main)
```

---

### `ClaudeSDKClient` Class

**Signature:**
```python
class ClaudeSDKClient:
    def __init__(self, options: ClaudeAgentOptions | None = None)
```

#### Methods

##### `async def connect()`
Establishes connection to Claude Code CLI.

```python
async with ClaudeSDKClient(options=options) as client:
    # Client automatically connected
    pass
```

##### `async def query(prompt: str)`
Sends a message to Claude.

```python
await client.query("Analyze this code")
```

##### `async def receive_response() -> AsyncIterator[Message]`
Receives streaming responses from Claude.

```python
async for message in client.receive_response():
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text)
```

##### `async def interrupt()`
Stops current task execution.

```python
await client.interrupt()
```

##### `async def disconnect()`
Closes connection to Claude Code CLI.

```python
await client.disconnect()
```

#### Context Manager Support

```python
async with ClaudeSDKClient(options=options) as client:
    await client.query("Hello")
    async for msg in client.receive_response():
        print(msg)
# Automatically disconnects
```

---

## `ClaudeAgentOptions` Configuration

### Complete Parameter Reference

```python
from claude_agent_sdk import ClaudeAgentOptions
from pathlib import Path

options = ClaudeAgentOptions(
    # System Configuration
    system_prompt: str | dict | None = None,
    model: str | None = None,
    max_turns: int | None = None,

    # Working Directory
    cwd: str | Path | None = None,

    # Tool Configuration
    allowed_tools: list[str] | None = None,
    permission_mode: str | None = None,

    # MCP Servers
    mcp_servers: dict | str | Path | None = None,

    # Agents & Subagents
    agents: dict[str, AgentDefinition] | None = None,

    # Settings
    setting_sources: list[str] | None = None,
    add_dirs: list[Path] | None = None,

    # Hooks
    hooks: dict[str, list[HookMatcher]] | None = None,
)
```

---

### Parameter Details

#### `system_prompt`
Defines Claude's behavior and expertise.

**Types:**
- `str`: Custom system prompt
- `dict`: Preset with optional append
- `None`: Use default

**Examples:**
```python
# Custom prompt
system_prompt = "You are an expert investment analyst specializing in fundamental analysis."

# Preset with append
system_prompt = {
    "type": "preset",
    "preset": "claude_code",
    "append": "Focus on Python best practices and type hints."
}

# Available presets: "claude_code", "general", "concise"
```

---

#### `model`
Specify Claude model to use.

**Options:**
- `"sonnet"` (default): Claude 3.5 Sonnet - balanced performance
- `"haiku"`: Claude 3.5 Haiku - faster, cheaper
- `"opus"`: Claude 3 Opus - most capable (if available)

**Example:**
```python
# Use Haiku for faster, cheaper responses
options = ClaudeAgentOptions(model="haiku")
```

---

#### `max_turns`
Limit conversation turns (safety/cost control).

**Type:** `int | None`

**Example:**
```python
# Limit to 5 back-and-forth exchanges
options = ClaudeAgentOptions(max_turns=5)
```

---

#### `cwd`
Set working directory for file operations.

**Type:** `str | Path | None`

**Example:**
```python
from pathlib import Path

options = ClaudeAgentOptions(
    cwd="/path/to/project"  # or Path("/path/to/project")
)
```

---

#### `allowed_tools`
Specify which tools Claude can use.

**Type:** `list[str] | None`

**Wildcards:** Use `*` for pattern matching

**Built-in Tools:**
- `Read`, `Write`, `Edit` - File operations
- `Glob`, `Grep` - File search
- `Bash` - Shell commands
- `WebSearch`, `WebFetch` - Web access
- `TodoWrite` - Task management

**MCP Tools:** Format: `mcp__<server>__<tool>`

**Examples:**
```python
# Allow specific tools only
allowed_tools = ["Read", "Write", "Bash"]

# Allow all MCP tools from specific server
allowed_tools = ["Read", "mcp__stock-analyzer__*"]

# Allow specific MCP tool
allowed_tools = ["mcp__company-research__get_company_profile"]

# Allow everything (use cautiously!)
allowed_tools = ["*"]
```

---

#### `permission_mode`
Control tool execution permissions.

**Type:** `str | None`

**Modes:**
- `"default"`: Standard permission checks (user approval required)
- `"acceptEdits"`: Auto-approve file edits (Read/Write/Edit)
- `"plan"`: Planning mode, no execution (not yet supported)
- `"bypassPermissions"`: Skip all permission checks (⚠️ use cautiously)

**Example:**
```python
# Auto-approve file edits for automation
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Edit"],
    permission_mode="acceptEdits"
)
```

---

#### `mcp_servers`
Configure MCP (Model Context Protocol) servers.

**Type:** `dict[str, McpServerConfig] | str | Path | None`

**External MCP Server (stdio):**
```python
mcp_servers = {
    "stock-analyzer": {
        "type": "stdio",
        "command": "uv",
        "args": ["run", "python", "-m", "src.stock_mcp.server", "stdio"],
        "env": {
            "API_KEY": "${API_KEY}"  # Environment variable reference
        }
    }
}
```

**SDK MCP Server (in-process):**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("add", "Add two numbers", {"a": int, "b": int})
async def add(args):
    result = args["a"] + args["b"]
    return {"content": [{"type": "text", "text": str(result)}]}

calculator = create_sdk_mcp_server(
    name="calculator",
    version="1.0.0",
    tools=[add]
)

mcp_servers = {"calculator": calculator}
```

**Mixed Configuration:**
```python
mcp_servers = {
    "internal": sdk_server,      # In-process
    "external": {                # External subprocess
        "type": "stdio",
        "command": "external-server"
    }
}
```

---

#### `agents`
Define programmatic subagents for parallel execution.

**Type:** `dict[str, AgentDefinition] | None`

**⚠️ CRITICAL:** This parameter currently has bugs in Python SDK (see PROGRAMMATIC-AGENTS-NOT-WORKING.md)

**Recommended:** Use Markdown file agents instead (`.claude/agents/*.md`)

**Example (for reference - not working in v1.5.8):**
```python
# ❌ Currently causes "'method' object is not iterable" error
agents = {
    "fundamental-analyst": {
        "description": "Analyze company fundamentals",
        "prompt": "You are a fundamental analysis expert",
        "tools": ["mcp__company-research__*"],
        "model": "sonnet"
    },
    "technical-analyst": {
        "description": "Analyze price patterns",
        "prompt": "You are a technical analysis expert",
        "tools": ["mcp__stock-analyzer__*"],
        "model": "haiku"
    }
}

# ✅ Use Markdown files instead
# Create .claude/agents/fundamental-analyst.md
```

---

#### `setting_sources`
Control which filesystem settings to load.

**Type:** `list[str] | None`

**Options:**
- `"user"`: Load from `~/.claude/`
- `"project"`: Load from `.claude/` in project

**Example:**
```python
# Load project-level agents only (ignore user settings)
options = ClaudeAgentOptions(
    setting_sources=["project"]
)

# Load both user and project settings
options = ClaudeAgentOptions(
    setting_sources=["user", "project"]
)
```

**Default:** Both user and project settings are loaded if not specified

---

#### `add_dirs`
Additional directories to search for agents/commands.

**Type:** `list[Path] | None`

**Example:**
```python
from pathlib import Path

options = ClaudeAgentOptions(
    add_dirs=[
        Path(".claude"),           # Project .claude directory
        Path("/shared/agents")     # Shared agent library
    ]
)
```

---

#### `hooks`
Define event-based hooks for intercepting and modifying behavior.

**Type:** `dict[str, list[HookMatcher]] | None`

**Hook Events:**
- `"PreToolUse"`: Before tool execution
- `"PostToolUse"`: After tool execution
- `"UserPromptSubmit"`: Before user prompt is sent
- `"Stop"`: When conversation stops
- `"SubagentStop"`: When subagent completes
- `"PreCompact"`: Before context compaction

**Hook Signature:**
```python
async def hook_function(
    input_data: dict,
    tool_use_id: str,
    context: dict
) -> dict
```

**Example - PreToolUse Hook:**
```python
from claude_agent_sdk import HookMatcher

async def check_bash_command(input_data, tool_use_id, context):
    """Block dangerous bash commands"""
    if input_data.get("tool_name") != "Bash":
        return {}  # Allow non-Bash tools

    command = input_data.get("tool_input", {}).get("command", "")

    # Block dangerous patterns
    dangerous = ["rm -rf", "dd if=", "mkfs"]
    for pattern in dangerous:
        if pattern in command:
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"Blocked: {pattern}"
                }
            }

    return {}  # Allow safe commands

options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(matcher="Bash", hooks=[check_bash_command])
        ]
    }
)
```

**Example - PostToolUse Hook (Caching):**
```python
async def cache_tool_result(input_data, tool_use_id, context):
    """Cache MCP tool results to reduce API calls"""
    tool_name = input_data.get("tool_name")
    tool_input = input_data.get("tool_input")
    result = input_data.get("result")

    if tool_name.startswith("mcp__"):
        cache_key = f"{tool_name}:{hash(str(tool_input))}"
        self.cache[cache_key] = result

    return {}

options = ClaudeAgentOptions(
    hooks={
        "PostToolUse": [
            HookMatcher(matcher="mcp__*", hooks=[cache_tool_result])
        ]
    }
)
```

**HookMatcher Parameters:**
- `matcher`: Tool name pattern (supports `*` wildcard)
- `hooks`: List of hook functions to execute

---

## Custom Tools (SDK MCP Servers)

### Creating Tools with `@tool` Decorator

**Signature:**
```python
@tool(name: str, description: str, input_schema: dict | type)
async def tool_function(args: dict) -> dict
```

**Parameters:**
- `name`: Tool identifier (used as `mcp__<server>__<name>`)
- `description`: What the tool does (shown to Claude)
- `input_schema`: Parameter types (dict or Python types)

**Return Format:**
```python
{
    "content": [
        {"type": "text", "text": "Result message"},
        {"type": "image", "data": "base64..."}  # Optional
    ],
    "isError": False  # Optional, default False
}
```

**Example - Simple Calculator:**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("add", "Add two numbers", {"a": int, "b": int})
async def add_numbers(args):
    result = args["a"] + args["b"]
    return {
        "content": [{"type": "text", "text": f"Sum: {result}"}]
    }

@tool("multiply", "Multiply two numbers", {"a": int, "b": int})
async def multiply_numbers(args):
    result = args["a"] * args["b"]
    return {
        "content": [{"type": "text", "text": f"Product: {result}"}]
    }

# Create server
calculator = create_sdk_mcp_server(
    name="calculator",
    version="1.0.0",
    tools=[add_numbers, multiply_numbers]
)

# Use with Claude
options = ClaudeAgentOptions(
    mcp_servers={"calc": calculator},
    allowed_tools=["mcp__calc__*"]
)
```

**Example - Complex Input Schema:**
```python
@tool(
    "search_stocks",
    "Search for stocks by criteria",
    {
        "sector": str,
        "min_price": float,
        "max_price": float,
        "limit": int
    }
)
async def search_stocks(args):
    # Access validated parameters
    sector = args["sector"]
    min_price = args["min_price"]
    max_price = args["max_price"]
    limit = args["limit"]

    # Fetch data
    results = await stock_api.search(
        sector=sector,
        price_range=(min_price, max_price),
        limit=limit
    )

    return {
        "content": [
            {"type": "text", "text": f"Found {len(results)} stocks"},
            {"type": "text", "text": str(results)}
        ]
    }
```

---

### `create_sdk_mcp_server()` Function

**Signature:**
```python
def create_sdk_mcp_server(
    name: str,
    version: str = "1.0.0",
    tools: list[callable] = []
) -> McpServer
```

**Parameters:**
- `name`: Server identifier
- `version`: Server version (default "1.0.0")
- `tools`: List of `@tool` decorated functions

**Returns:** McpServer instance for use in `mcp_servers` config

---

## Message Types

### `AssistantMessage`
Claude's response message.

**Attributes:**
```python
class AssistantMessage:
    role: str  # "assistant"
    content: list[ContentBlock]  # Text, tool use, etc.
    usage: UsageInfo | None  # Token usage and cost
    stop_reason: str | None  # Why generation stopped
```

**Example:**
```python
if isinstance(message, AssistantMessage):
    for block in message.content:
        if isinstance(block, TextBlock):
            print(f"Claude: {block.text}")
        elif isinstance(block, ToolUseBlock):
            print(f"Tool used: {block.name}")
```

---

### `UserMessage`
User input message.

**Attributes:**
```python
class UserMessage:
    role: str  # "user"
    content: list[ContentBlock]
```

---

### `ResultMessage`
Tool execution result.

**Attributes:**
```python
class ResultMessage:
    role: str  # "result"
    content: list[ToolResultBlock]
```

---

### Content Blocks

#### `TextBlock`
```python
class TextBlock:
    type: str  # "text"
    text: str
```

#### `ToolUseBlock`
```python
class ToolUseBlock:
    type: str  # "tool_use"
    id: str
    name: str
    input: dict
```

#### `ToolResultBlock`
```python
class ToolResultBlock:
    type: str  # "tool_result"
    tool_use_id: str
    content: list[ContentBlock]
    is_error: bool
```

---

### `UsageInfo`
Token usage and cost tracking.

**Attributes:**
```python
class UsageInfo:
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int | None
    cache_read_input_tokens: int | None
    total_cost_usd: float | None
```

**Example - Cost Tracking:**
```python
total_cost = 0.0
cache_savings = 0.0

async for message in client.receive_response():
    if isinstance(message, AssistantMessage) and message.usage:
        step_cost = message.usage.total_cost_usd or 0.0
        total_cost += step_cost

        # Calculate cache savings
        if message.usage.cache_read_input_tokens:
            # Cached tokens cost ~10% of regular tokens
            cache_hits = message.usage.cache_read_input_tokens
            savings = cache_hits * 0.00015 * 0.9  # Approximate
            cache_savings += savings

print(f"Total cost: ${total_cost:.4f}")
print(f"Cache savings: ${cache_savings:.4f}")
```

---

## Error Handling

### Exception Hierarchy

```python
ClaudeSDKError              # Base exception
├── CLINotFoundError        # Claude Code not installed
├── CLIConnectionError      # Connection issues
├── ProcessError            # Process failed
│   └── exit_code: int     # Process exit code
└── CLIJSONDecodeError      # JSON parsing error
```

### Example

```python
from claude_agent_sdk import (
    ClaudeSDKError,
    CLINotFoundError,
    CLIConnectionError,
    ProcessError,
    CLIJSONDecodeError
)

try:
    async with ClaudeSDKClient(options=options) as client:
        await client.query("Hello")
        async for msg in client.receive_response():
            print(msg)

except CLINotFoundError:
    print("Please install Claude Code: npm install -g @anthropic-ai/claude-code")

except CLIConnectionError as e:
    print(f"Connection failed: {e}")

except ProcessError as e:
    print(f"Process failed with exit code {e.exit_code}")
    print(f"Output: {e}")

except CLIJSONDecodeError as e:
    print(f"Failed to parse response: {e}")

except ClaudeSDKError as e:
    print(f"SDK error: {e}")
```

---

## Best Practices

### 1. Use Context Managers

```python
# ✅ Good: Automatic cleanup
async with ClaudeSDKClient(options=options) as client:
    await client.query("Hello")

# ❌ Bad: Manual cleanup required
client = ClaudeSDKClient(options=options)
await client.connect()
# ... work ...
await client.disconnect()  # Easy to forget!
```

---

### 2. Handle Message Types

```python
async for message in client.receive_response():
    if isinstance(message, AssistantMessage):
        # Process assistant response
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text)

    elif isinstance(message, ResultMessage):
        # Process tool results
        for block in message.content:
            if block.is_error:
                print(f"Tool error: {block.content}")
```

---

### 3. Track Costs

```python
total_cost = 0.0

async for message in client.receive_response():
    if isinstance(message, AssistantMessage) and message.usage:
        total_cost += message.usage.total_cost_usd or 0.0

        if total_cost > MAX_BUDGET:
            await client.interrupt()
            raise BudgetExceededError()
```

---

### 4. Use Hooks for Cross-Cutting Concerns

```python
# Caching, logging, monitoring via hooks
async def log_tool_use(input_data, tool_use_id, context):
    logger.info(f"Tool: {input_data.get('tool_name')}")
    return {}

async def cache_results(input_data, tool_use_id, context):
    # Implement caching logic
    return {}

options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [HookMatcher(matcher="*", hooks=[log_tool_use])],
        "PostToolUse": [HookMatcher(matcher="mcp__*", hooks=[cache_results])]
    }
)
```

---

### 5. Prefer SDK MCP Servers for Custom Tools

```python
# ✅ Good: In-process, no subprocess overhead
calculator = create_sdk_mcp_server(name="calc", tools=[add, subtract])

# ❌ Okay but slower: External subprocess
mcp_servers = {
    "calculator": {
        "type": "stdio",
        "command": "python",
        "args": ["-m", "calculator_server"]
    }
}
```

---

## Complete Working Example

```python
import asyncio
from pathlib import Path
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
    tool,
    create_sdk_mcp_server,
    HookMatcher
)

# Define custom tool
@tool("get_weather", "Get weather for a city", {"city": str})
async def get_weather(args):
    # Mock weather data
    weather = f"Sunny, 72°F in {args['city']}"
    return {
        "content": [{"type": "text", "text": weather}]
    }

# Create SDK MCP server
weather_server = create_sdk_mcp_server(
    name="weather",
    version="1.0.0",
    tools=[get_weather]
)

# Define hook
async def log_tools(input_data, tool_use_id, context):
    print(f"[Hook] Using tool: {input_data.get('tool_name')}")
    return {}

# Configure options
options = ClaudeAgentOptions(
    system_prompt="You are a helpful weather assistant",
    allowed_tools=["mcp__weather__*"],
    mcp_servers={"weather": weather_server},
    permission_mode="acceptEdits",
    max_turns=3,
    hooks={
        "PreToolUse": [
            HookMatcher(matcher="*", hooks=[log_tools])
        ]
    }
)

async def main():
    async with ClaudeSDKClient(options=options) as client:
        # Send query
        await client.query("What's the weather in San Francisco?")

        # Receive response
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Claude: {block.text}")

                # Track costs
                if message.usage:
                    print(f"Cost: ${message.usage.total_cost_usd:.4f}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## References

- **Official Docs**: https://docs.claude.com/en/api/agent-sdk/python.md
- **GitHub**: https://github.com/anthropics/claude-agent-sdk-python
- **MCP Specification**: https://spec.modelcontextprotocol.io
- **Claude Code Hooks**: https://docs.anthropic.com/en/docs/claude-code/hooks

---

## Version History

- **1.0.0** (2025-01): Initial Agent SDK release
- **0.1.0** (2024): Claude Code SDK (predecessor)

---

*Last Updated: 2025-10-03*
