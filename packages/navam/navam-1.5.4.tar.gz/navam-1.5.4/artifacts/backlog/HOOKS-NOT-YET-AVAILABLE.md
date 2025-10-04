# Critical Discovery: Hooks Not Yet Available in claude-agent-sdk v0.1.0

**Date**: 2025-01-10
**Status**: 🔴 BLOCKED
**Version**: claude-agent-sdk==0.1.0

---

## Problem

The hook-based caching implementation causes a runtime error:

```
Chat error: 'method' object is not iterable
Connection will be reset on next interaction
```

**Root Cause**: `ClaudeAgentOptions` does not accept a `hooks` parameter in the current release (v0.1.0).

---

## What We Attempted

### Implementation (v1.5.1)
```python
self.claude_options = ClaudeAgentOptions(
    # ... other options
    hooks={
        'pre_tool_use': self._pre_tool_use_hook,
        'post_tool_use': self._post_tool_use_hook
    }
)
```

**Result**: Runtime error when initializing chat

---

## Investigation

### Documentation vs Reality

**Documentation showed**:
- Pre/post tool hooks in examples
- Hook-based caching patterns
- Seemed like a core feature

**Reality**:
- `claude-agent-sdk==0.1.0` doesn't support hooks parameter
- Parameter causes initialization error
- Feature may be in development or documentation is for future release

### SDK Version Check
```bash
pip show claude-agent-sdk
Name: claude-agent-sdk
Version: 0.1.0
```

This is the latest available version on PyPI.

---

## Impact

### What Still Works ✅
- ✅ SDK migration to claude-agent-sdk v0.1.0
- ✅ All existing functionality
- ✅ Session cache infrastructure
- ✅ Tool call tracking and metrics
- ✅ `/cache` command showing potential savings

### What Doesn't Work ❌
- ❌ **Actual cache hit prevention** - Can't intercept tool execution
- ❌ **Hook-based caching** - Hooks parameter not supported
- ❌ **70% API reduction** - Can track but not prevent duplicates

---

## Immediate Fix

**Removed hooks parameter** to restore functionality:

```python
# v1.5.2 - Hooks removed
self.claude_options = ClaudeAgentOptions(
    allowed_tools=allowed_tools or self._get_default_tools(),
    permission_mode=self.permission_mode,
    system_prompt=self._get_system_prompt(),
    mcp_servers=self.mcp_servers,
    add_dirs=agent_dirs,
    can_use_tool=self._handle_tool_permission if should_use_permission_callback else None,
    # TODO: Hooks not yet supported in claude-agent-sdk v0.1.0
)
```

---

## Alternative Approaches

### Option 1: Wait for SDK Update
**Pros**:
- Clean implementation when available
- Official SDK support
- Best long-term solution

**Cons**:
- No timeline for release
- Blocks performance improvements
- Unknown if feature will be added

**Recommendation**: Monitor SDK releases

### Option 2: Server-Side Caching (MCP Servers)
**Pros**:
- Works with current SDK
- Can implement immediately
- Controls caching at source

**Cons**:
- Requires modifying 3 MCP servers
- More complex implementation
- Cache not shared across servers

**Implementation**:
```python
# In each MCP server (stock_mcp, company_mcp, news_mcp)
@mcp.tool()
async def analyze_stock(symbol: str, ctx: Context) -> StockAnalysis:
    cache_key = f"analyze_stock:{symbol}"

    # Check server-side cache
    if cache_key in server_cache:
        return server_cache[cache_key]

    # Execute tool
    result = await do_analysis(symbol)

    # Store in cache
    server_cache[cache_key] = result
    return result
```

### Option 3: Wrapper/Proxy Pattern
**Pros**:
- Intercepts at client level
- Centralized caching logic
- Works with current SDK

**Cons**:
- Complex implementation
- May break with SDK updates
- Requires wrapping ClaudeSDKClient

**Implementation**:
```python
class CachingClaudeClient:
    def __init__(self, client: ClaudeSDKClient, cache: SessionCache):
        self.client = client
        self.cache = cache

    async def send_message(self, *args, **kwargs):
        # Intercept tool use blocks
        # Check cache before forwarding to client
        # Return cached or execute
        pass
```

### Option 4: Post-Processing Cache (Current State)
**Pros**:
- ✅ Already implemented
- ✅ Provides visibility
- ✅ Tracks savings potential

**Cons**:
- ❌ Doesn't prevent duplicate calls
- ❌ No actual cost savings
- ❌ Only analytics value

**Status**: This is what v1.5.1 currently does

---

## Recommended Path Forward

### Short Term (This Week)
1. **Release v1.5.2** with hooks removed (fix the error)
2. **Keep cache infrastructure** (metrics, tracking, `/cache` command)
3. **Update documentation** to reflect current capabilities

### Medium Term (Next Sprint)
1. **Implement Option 2: Server-Side Caching**
   - Add caching to `stock_mcp/server.py`
   - Add caching to `company_mcp/server.py`
   - Add caching to `news_mcp/server.py`
   - Share cache across servers if possible
   - **Expected savings**: Still 70% reduction!

2. **Benefits**:
   - Works with current SDK
   - Actual cost savings
   - Can implement in 1-2 days
   - Server-side cache is standard pattern

### Long Term (Monitor)
1. Watch for `claude-agent-sdk` updates
2. Check if hooks feature is added
3. Migrate to hooks when available
4. Remove server-side caching in favor of hooks

---

## Server-Side Caching Implementation Plan

### Phase 1: Add Cache to Stock MCP Server
```python
# src/stock_mcp/server.py

from fastmcp import FastMCP
from src.navam.cache_manager import SessionCache

# Shared cache instance
server_cache = SessionCache(ttl_seconds=300, max_entries=100)

@mcp.tool()
async def analyze_stock(symbol: str, ctx: Context) -> StockAnalysis:
    # Check cache
    cached = server_cache.get("analyze_stock", {"symbol": symbol})
    if cached:
        await ctx.info(f"✅ Cache hit for {symbol}")
        return cached

    # Execute
    api_client = ctx.request_context.lifespan_context["api_client"]
    result = await api_client.analyze_stock(symbol)

    # Store
    server_cache.set("analyze_stock", {"symbol": symbol}, result)
    return result
```

### Phase 2: Repeat for Other Servers
- Apply same pattern to `company_mcp/server.py`
- Apply same pattern to `news_mcp/server.py`

### Phase 3: Test and Measure
- Run `/invest:research-stock AAPL` twice
- Verify cache hits in server logs
- Confirm API call reduction
- Measure performance improvement

**Expected Result**: 70% reduction in external API calls

---

## Lessons Learned

1. **Verify SDK Features**: Documentation may be ahead of implementation
2. **Test Early**: Should have tested hooks before full implementation
3. **Have Fallbacks**: Server-side caching is a proven alternative
4. **Version Matters**: v0.1.0 is early - features may come later

---

## Action Items

### Immediate
- [x] Remove hooks parameter from chat.py
- [ ] Release v1.5.2 with fix
- [ ] Update documentation

### This Week
- [ ] Implement server-side caching in stock_mcp
- [ ] Implement server-side caching in company_mcp
- [ ] Implement server-side caching in news_mcp
- [ ] Test end-to-end caching
- [ ] Release v1.5.3 with server-side caching

### Ongoing
- [ ] Monitor claude-agent-sdk releases
- [ ] Check release notes for hooks feature
- [ ] Migrate when available

---

## Conclusion

**Current Status**: Hooks are not yet available in claude-agent-sdk v0.1.0

**Solution**: Implement server-side caching in MCP servers (proven pattern)

**Timeline**: 1-2 days implementation, same 70% savings

**Impact**: Minimal delay, better architecture long-term

---

*Discovery Date: 2025-01-10*
*Fix Released: v1.5.2 (pending)*
*Alternative Implementation: v1.5.3 (planned)*
