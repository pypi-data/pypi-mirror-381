# Programmatic Agents Not Working in Python SDK

**Date**: 2025-10-03
**Issue**: `'method' object is not iterable`
**Status**: ⚠️ DISABLED - Waiting for SDK fix or clarification

---

## The Problem

When passing `agents=INVESTMENT_RESEARCH_AGENTS` (with proper `AgentDefinition` instances) to `ClaudeAgentOptions`, the application crashes with:

```
Chat error: 'method' object is not iterable
Connection will be reset on next interaction
```

## What We Tried

### v1.5.5: Plain Dictionaries
```python
AGENTS = {
    "analyst": {
        "description": "...",
        "prompt": "..."
    }
}
```
**Result**: `asdict() should be called on dataclass instances`

### v1.5.6: Added 'prompt' field
Changed `"instructions"` → `"prompt"` in dictionaries
**Result**: Still `asdict()` error

### v1.5.7: AgentDefinition Dataclass
```python
from claude_agent_sdk.types import AgentDefinition

AGENTS = {
    "analyst": AgentDefinition(
        description="...",
        prompt="...",
        tools=[...],
        model="sonnet"
    )
}
```
**Result**: `'method' object is not iterable`

## Official Documentation Findings

### TypeScript SDK (Works)
From https://docs.claude.com/en/api/agent-sdk/subagents:

```typescript
const result = query({
  prompt: "Review authentication module",
  options: {
    agents: {
      'code-reviewer': {
        description: 'Expert code review specialist',
        prompt: 'You are a security-focused code reviewer...',
        tools: ['Read', 'Grep', 'Glob']
      }
    }
  }
});
```

This pattern is DOCUMENTED and SUPPORTED in TypeScript.

### Python SDK (Broken?)
The `agents` parameter EXISTS in Python SDK:
```python
agents: dict[str, claude_agent_sdk.types.AgentDefinition] | None = None
```

But using it causes runtime errors.

## Alternative: Markdown File Subagents

The SDK DOES support subagents via Markdown files:

1. **Create `.claude/agents/code-reviewer.md`**:
```markdown
---
description: Expert code review specialist
---

You are a security-focused code reviewer. Analyze code for:
- Security vulnerabilities
- Best practices violations
- Performance issues
```

2. **Reference in options**:
```python
options = ClaudeAgentOptions(
    add_dirs=[Path(".claude")],  # SDK will auto-load agents from .claude/agents/
    setting_sources=["project"]  # Required to load project-level agents
)
```

3. **Agent is automatically available** - SDK loads all `.md` files from `.claude/agents/`

## Current Workaround (v1.5.8)

**DISABLED programmatic agents** until SDK issue is resolved:

```python
self.claude_options = ClaudeAgentOptions(
    # ... other options ...
    # agents=INVESTMENT_RESEARCH_AGENTS,  # DISABLED - causes 'method' object is not iterable
)
```

**Using Markdown file agents instead** (already present in package):
- `src/navam/.claude/agents/` contains 18 agent definitions
- SDK automatically loads these when `add_dirs` is set
- No programmatic configuration needed

## Hypothesis: Python SDK Bug

**Theory**: The Python SDK's `agents` parameter may not be fully implemented or has a bug in how it processes `AgentDefinition` instances.

**Evidence**:
1. Parameter exists in type signature
2. `AgentDefinition` dataclass exists and is importable
3. TypeScript SDK has working examples
4. Python SDK throws unclear errors regardless of configuration format
5. Error message `'method' object is not iterable` suggests internal SDK code is trying to iterate over a method object instead of calling it

**Possible SDK Bug Location**:
The SDK might be doing something like:
```python
# ❌ WRONG - tries to iterate the .items method itself
for key, value in agents.items:  # Missing ()
    ...

# ✅ CORRECT - calls the method then iterates
for key, value in agents.items():
    ...
```

## Recommended Approach

**For Now (v1.5.8+)**:
1. Use Markdown file agents in `.claude/agents/`
2. Do NOT use programmatic `agents` parameter
3. Rely on SDK's automatic agent loading

**Future**:
1. File issue with Anthropic about Python SDK `agents` parameter
2. Wait for SDK update or clarification
3. Re-enable programmatic agents when SDK is fixed

## Files to Keep

**Keep but don't use**:
- `src/navam/agent_configs.py` - AgentDefinition configurations (for future use)
- `artifacts/refer/claude-agent-sdk/AGENTS-MUST-BE-DATACLASSES.md` - Still accurate for when it works

**Actually used**:
- `src/navam/.claude/agents/*.md` - 18 Markdown agent definitions (working)
- `ClaudeAgentOptions(add_dirs=...)` - Loads agents from filesystem (working)

## Summary

**What Works**:
- ✅ Markdown file agents (`.claude/agents/*.md`)
- ✅ Automatic agent loading via `add_dirs`
- ✅ `AgentDefinition` dataclass can be instantiated
- ✅ TypeScript SDK programmatic agents

**What Doesn't Work**:
- ❌ Python SDK `agents` parameter (any configuration format)
- ❌ Programmatic agent definitions in Python

**Status**: Using Markdown agents until Python SDK issue is resolved.

---

**Last Updated**: 2025-10-03
**Version**: v1.5.8
**Next Steps**: Consider filing SDK bug report with Anthropic
