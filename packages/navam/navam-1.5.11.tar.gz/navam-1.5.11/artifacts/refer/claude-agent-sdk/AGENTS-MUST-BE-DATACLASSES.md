# CRITICAL: Agents Must Be AgentDefinition Dataclass Instances

**Date**: 2025-10-03
**Issue**: `asdict() should be called on dataclass instances`
**Versions Affected**: v1.5.5, v1.5.6
**Fixed In**: v1.5.7

---

## The Problem

When configuring parallel subagents, using plain dictionaries causes this runtime error:

```
Chat error: asdict() should be called on dataclass instances
Connection will be reset on next interaction
```

## Root Cause

The `agents` parameter in `ClaudeAgentOptions` expects:
```python
agents: dict[str, claude_agent_sdk.types.AgentDefinition] | None = None
```

**Key point**: `AgentDefinition` is a **dataclass**, not a plain dictionary.

## Wrong Approach (v1.5.5, v1.5.6)

```python
# ❌ WRONG - Plain dictionaries cause asdict() error
INVESTMENT_RESEARCH_AGENTS = {
    "fundamental-analyst": {
        "description": "Analyze company financials",
        "prompt": "You are a fundamental analyst...",
        "tools": ["mcp__company-research__*"],
        "model": "claude-sonnet-4-20250514"
    }
}

# This will fail at runtime!
options = ClaudeAgentOptions(agents=INVESTMENT_RESEARCH_AGENTS)
```

## Correct Approach (v1.5.7+)

```python
from claude_agent_sdk.types import AgentDefinition

# ✅ CORRECT - AgentDefinition dataclass instances
INVESTMENT_RESEARCH_AGENTS = {
    "fundamental-analyst": AgentDefinition(
        description="Analyze company financials",
        prompt="You are a fundamental analyst...",
        tools=["mcp__company-research__*"],
        model="sonnet"  # Use SDK model alias
    )
}

# This works correctly
options = ClaudeAgentOptions(agents=INVESTMENT_RESEARCH_AGENTS)
```

## AgentDefinition Fields

```python
@dataclass
class AgentDefinition:
    description: str
    prompt: str
    tools: list[str] | None = None
    model: Literal['sonnet', 'opus', 'haiku', 'inherit'] | None = None
```

### Field Details

**Required:**
- `description` (str): Brief description of agent's purpose
- `prompt` (str): System prompt/instructions for the agent

**Optional:**
- `tools` (list[str] | None): List of tool names agent can access
- `model` (Literal | None): Model to use - `"sonnet"`, `"opus"`, `"haiku"`, or `"inherit"`

### Model Aliases

Use SDK model aliases, **not** full model IDs:

```python
# ✅ CORRECT
model="sonnet"
model="haiku"
model="opus"
model="inherit"  # Use parent's model

# ❌ WRONG
model="claude-sonnet-4-20250514"
model="claude-haiku-4-20250611"
```

## Complete Working Example

```python
from typing import Dict
from claude_agent_sdk import ClaudeAgentOptions
from claude_agent_sdk.types import AgentDefinition

# Define agents as AgentDefinition instances
INVESTMENT_RESEARCH_AGENTS: Dict[str, AgentDefinition] = {
    "fundamental-analyst": AgentDefinition(
        description="Analyze company financials and fundamentals",
        prompt="""You are a fundamental analysis specialist. Focus on:
- Financial statements and ratios
- Company valuation metrics
- Earnings and revenue trends
- Competitive positioning

Provide data-driven analysis highlighting key strengths and risks.""",
        tools=[
            "mcp__company-research__get_company_profile",
            "mcp__company-research__get_company_financials",
            "mcp__company-research__get_analyst_ratings",
        ],
        model="sonnet"
    ),

    "technical-analyst": AgentDefinition(
        description="Analyze price patterns and technical indicators",
        prompt="""You are a technical analysis specialist. Focus on:
- Price trends and momentum
- Technical indicators (RSI, MACD, MA)
- Support/resistance levels
- Trading volume patterns

Provide objective technical assessment based on data.""",
        tools=[
            "mcp__stock-analyzer__analyze_stock",
            "mcp__stock-analyzer__get_moving_averages",
        ],
        model="sonnet"
    ),

    "news-analyst": AgentDefinition(
        description="Analyze news sentiment and market narrative",
        prompt="""You are a news and sentiment specialist. Focus on:
- Recent company news and events
- Market sentiment trends
- Risk events and catalysts
- Competitive landscape

Synthesize news into actionable insights.""",
        tools=[
            "mcp__news-analyzer__get_company_news",
            "mcp__news-analyzer__analyze_sentiment",
        ],
        model="haiku"  # Faster/cheaper for news analysis
    ),
}

# Use in ClaudeAgentOptions
options = ClaudeAgentOptions(
    system_prompt="You are an investment research orchestrator",
    agents=INVESTMENT_RESEARCH_AGENTS,
    hooks={
        'pre_tool_use': pre_tool_hook,
        'post_tool_use': post_tool_hook
    }
)
```

## Testing Your Configuration

Verify agents are properly configured:

```python
from claude_agent_sdk.types import AgentDefinition

# Check all agents are AgentDefinition instances
for name, agent in INVESTMENT_RESEARCH_AGENTS.items():
    assert isinstance(agent, AgentDefinition), f"{name} must be AgentDefinition"
    assert agent.description, f"{name} missing description"
    assert agent.prompt, f"{name} missing prompt"
    print(f"✅ {name}: Valid AgentDefinition")

# Test ClaudeAgentOptions creation
try:
    options = ClaudeAgentOptions(
        system_prompt="Test",
        agents=INVESTMENT_RESEARCH_AGENTS
    )
    print("✅ ClaudeAgentOptions created successfully")
except Exception as e:
    print(f"❌ Error: {e}")
```

## Common Mistakes to Avoid

### 1. Using Plain Dictionaries
```python
# ❌ WRONG
agents = {
    "analyst": {"description": "...", "prompt": "..."}
}
```

### 2. Using Full Model IDs
```python
# ❌ WRONG
AgentDefinition(
    model="claude-sonnet-4-20250514"
)

# ✅ CORRECT
AgentDefinition(
    model="sonnet"
)
```

### 3. Accessing Agent Config Like Dict
```python
agent = INVESTMENT_RESEARCH_AGENTS["fundamental-analyst"]

# ❌ WRONG
tools = agent["tools"]

# ✅ CORRECT
tools = agent.tools
```

### 4. Mixing Dict and Dataclass Patterns
```python
# ❌ WRONG - Inconsistent
AGENTS = {
    "agent1": AgentDefinition(...),  # Dataclass
    "agent2": {"description": "..."}  # Dict
}

# ✅ CORRECT - All dataclasses
AGENTS = {
    "agent1": AgentDefinition(...),
    "agent2": AgentDefinition(...)
}
```

## Error Messages and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `asdict() should be called on dataclass instances` | Using plain dict instead of AgentDefinition | Convert to `AgentDefinition(...)` |
| `'dict' object is not subscriptable` | Trying to access AgentDefinition with dict syntax | Use attribute access: `agent.tools` not `agent["tools"]` |
| `TypeError: 'AgentDefinition' object is not subscriptable` | Using `agent[key]` instead of `agent.attribute` | Use dot notation: `agent.tools` |
| Model validation error | Using full model ID instead of alias | Use `"sonnet"`, `"haiku"`, `"opus"` |

## Key Takeaways

1. **Always use `AgentDefinition` dataclass** - Never plain dictionaries
2. **Import from types**: `from claude_agent_sdk.types import AgentDefinition`
3. **Use model aliases** - `"sonnet"`, `"haiku"`, `"opus"`, not full IDs
4. **Access via attributes** - `agent.tools`, not `agent["tools"]`
5. **Type hint correctly** - `Dict[str, AgentDefinition]` not `Dict[str, Dict]`

## References

- **Fixed in**: Navam v1.5.7
- **Commit**: ca3c89c - "fix: Convert agent dicts to AgentDefinition dataclass instances"
- **Issue**: Discovered when attempting GOOG stock research
- **Documentation**: This file created 2025-10-03

---

**MEMORIZE**: Agents parameter requires AgentDefinition dataclass instances, NOT plain dictionaries!
