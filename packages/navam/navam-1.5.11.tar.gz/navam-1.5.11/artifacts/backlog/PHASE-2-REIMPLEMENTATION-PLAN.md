# Phase 2: Parallel Subagents - Reimplementation Plan

**Created**: 2025-10-03
**Status**: 🔴 CRITICAL - Needs Implementation
**Previous Attempts**: v1.5.5-v1.5.10 (all failed, rolled back in v1.5.11)

---

## Executive Summary

**Goal**: Achieve 3-4x speed improvement (8min → 2-3min) for investment research workflows through parallel subagent execution.

**Problem**: Python SDK's `agents` parameter is broken - causes `'method' object is not iterable` error.

**Solution**: Use Markdown file agents (already working) + investigate Task tool or prompt engineering for parallel execution.

---

## What We Know (From Documentation Review)

### ✅ What Works
1. **Markdown File Agents** - 18 agents already bundled in `src/navam/.claude/agents/`
2. **Agent Auto-Loading** - SDK loads agents via `add_dirs=[Path(".claude")]`
3. **Hook-Based Caching** - 70% API call reduction (v1.5.4)
4. **MCP Servers** - 3 servers providing 25+ financial tools

### ❌ What Doesn't Work
1. **Programmatic `agents` parameter** - Python SDK bug
2. **AgentDefinition instances** - Causes iteration errors at module load time
3. **All attempts v1.5.5-v1.5.10** - Same error regardless of approach

### ❓ What's Unclear
1. **How does Claude actually USE Markdown agents in parallel?**
2. **Is there a Task tool for launching subagents programmatically?**
3. **Does Claude auto-parallelize when it sees multiple agents available?**
4. **Do we need special prompt instructions to trigger parallel execution?**

---

## Research Questions (MUST ANSWER BEFORE IMPLEMENTING)

### Q1: How are Markdown agents invoked?
**Investigation needed**:
- Does Claude Code CLI have a Task tool?
- Do we prompt Claude to "use the fundamental-analyst agent"?
- Does Claude auto-select agents based on task?
- Is there a tool like `Task(agent="fundamental-analyst", prompt="...")`?

**Test Plan**:
```bash
# Test 1: Check available tools
navam chat
> /perf  # Look for Task or Agent-related tools

# Test 2: Try prompting for agent use
> "Use the fundamental-analyst agent to analyze AAPL"

# Test 3: Check agent discovery
> "What agents are available?"
```

### Q2: Does parallelization happen automatically?
**Investigation needed**:
- If we prompt "research AAPL using fundamental, technical, and news analysts", does Claude parallelize?
- Or do we need to explicitly launch agents in parallel?
- What does "subagents run in parallel automatically" mean in practice?

**Test Plan**:
```python
# Test workflow with timing
prompt = """
Research AAPL stock using these specialist agents:
1. fundamental-analyst - Analyze financials and fundamentals
2. technical-analyst - Analyze price patterns and indicators
3. news-analyst - Analyze recent news and sentiment

Coordinate their work and compile a comprehensive report.
"""

# Monitor: Do agents run in parallel or sequential?
```

### Q3: What's the actual API for subagent invocation?
**Investigation needed**:
- Check Claude Code docs for Task tool
- Look at TypeScript SDK examples (they work!)
- Search for "parallel" or "subagent" in SDK source code

**Resources to check**:
- https://docs.claude.com/en/api/agent-sdk/subagents
- TypeScript SDK examples
- Claude Code CLI `--help` output

---

## Implementation Options

### Option 1: Task Tool Approach (IF IT EXISTS)
```python
# Hypothetical - need to verify this exists
prompt = """
Launch these three tasks in parallel:

Task 1 (fundamental-analyst):
- Get company profile for AAPL
- Get financials
- Analyze fundamentals

Task 2 (technical-analyst):
- Analyze stock technical indicators
- Get moving averages
- Identify trends

Task 3 (news-analyst):
- Get company news
- Analyze sentiment
- Identify catalysts

Compile results into comprehensive report.
"""
```

**Pros**:
- Direct control over parallelization
- Clear separation of concerns
- Easy to test/debug

**Cons**:
- Requires Task tool to exist
- May not be supported in Python SDK

### Option 2: Prompt Engineering Approach
```python
# Use system prompt to enable parallel thinking
system_prompt = """
You have access to specialist agents in .claude/agents/:
- fundamental-analyst: Company financials and fundamentals
- technical-analyst: Price patterns and indicators
- news-analyst: News sentiment and catalysts

When asked to research a stock, coordinate these agents to work IN PARALLEL:
1. Launch all three agents simultaneously with their respective tasks
2. Wait for all agents to complete
3. Synthesize their findings into a comprehensive report

CRITICAL: Agents must run in parallel, not sequential.
"""
```

**Pros**:
- No new tools required
- Works with existing Markdown agents
- Relies on Claude's built-in capabilities

**Cons**:
- Less explicit control
- Unclear if Claude actually parallelizes
- Hard to measure/verify parallel execution

### Option 3: Sequential with Streaming (Fallback)
```python
# If parallelization isn't possible, optimize sequential execution
# Use streaming to show progressive results
async for message in client.query(prompt):
    if "fundamental analysis" in message:
        console.print("📊 Fundamentals", message)
    elif "technical analysis" in message:
        console.print("📈 Technical", message)
    elif "news analysis" in message:
        console.print("📰 News", message)
```

**Pros**:
- Guaranteed to work
- Better UX than blocking wait
- Still leverages caching (70% reduction)

**Cons**:
- No speedup from parallelization
- Sequential execution (8min → maybe 6min with caching)
- Doesn't achieve 3-4x target

---

## Recommended Implementation Path

### Phase 2A: Research & Discovery (1 day)
**Goal**: Answer the 3 critical questions above

**Tasks**:
1. ✅ Review all SDK documentation (DONE)
2. ⏳ Test Markdown agent invocation manually
3. ⏳ Check for Task tool in available tools
4. ⏳ Review TypeScript SDK parallel examples
5. ⏳ Test prompt engineering for parallel execution

**Output**:
- Document HOW Markdown agents are actually invoked
- Confirm whether parallelization is possible
- Choose implementation option (1, 2, or 3)

### Phase 2B: Proof of Concept (1 day)
**Goal**: Demonstrate chosen approach works

**Tasks**:
1. Create minimal test case with 2 agents
2. Measure execution time (parallel vs sequential)
3. Verify both agents run (not just one)
4. Confirm caching still works (70% hit rate)

**Success Criteria**:
- Both agents execute successfully
- Combined time < individual times (if parallel)
- Cache hits maintained

### Phase 2C: Production Implementation (1-2 days)
**Goal**: Implement in /invest:research-stock command

**Tasks**:
1. Update investment command prompt with agent coordination
2. Implement progress tracking for multiple agents
3. Add timeout handling (if one agent hangs)
4. Test with real workflow (AAPL, TSLA, NVDA)

**Success Criteria**:
- Workflow time <3 minutes (from 8min)
- All 3 analyses present in report
- No regression in quality
- Cache hit rate maintained ~70%

### Phase 2D: Testing & Optimization (1 day)
**Goal**: Verify production readiness

**Tasks**:
1. Benchmark 10 different stocks
2. Compare: old approach vs new approach vs cached
3. Measure actual parallelization (if any)
4. Document edge cases and limitations

**Success Metrics**:
- Average time: 2-3 minutes
- Success rate: >95%
- Cache effectiveness: 70%+
- User satisfaction: Perceived speed improvement

---

## Risk Mitigation

### Risk 1: Parallelization May Not Be Possible
**Mitigation**: Fall back to Option 3 (sequential + streaming)
**Impact**: Moderate speedup (2x instead of 4x) but still better UX

### Risk 2: Markdown Agents May Not Support Tools List
**Mitigation**: Use general-purpose agents without tool restrictions
**Impact**: Agents might call wrong tools, but caching prevents duplicate costs

### Risk 3: SDK May Have More Bugs
**Mitigation**: Keep rollback plan ready, maintain v1.5.11 as stable
**Impact**: Development time loss, but no production impact

---

## Success Criteria Summary

**Minimum (Must Have)**:
- ✅ No regression from v1.5.11 (stable baseline)
- ✅ Workflow completes successfully
- ✅ Cache hooks still work (70% hit rate)
- ✅ All three analyses in final report

**Target (Should Have)**:
- ⭐ Workflow time <3 minutes (from 8min)
- ⭐ Multiple agents visibly working
- ⭐ Progressive result streaming
- ⭐ Maintained code quality

**Stretch (Nice to Have)**:
- 🚀 True parallel execution verified
- 🚀 Time <2 minutes with caching
- 🚀 Real-time agent status display
- 🚀 Per-agent cost tracking

---

## Next Steps

**Immediate (Today)**:
1. ✅ Rollback to v1.5.11 (DONE)
2. ✅ Update backlog (DONE)
3. ✅ Create this plan (DONE)
4. ⏳ Publish v1.5.11 to PyPI
5. ⏳ Begin Phase 2A research

**This Week**:
1. Complete Phase 2A (research)
2. Make GO/NO-GO decision on approach
3. If GO: Start Phase 2B (proof of concept)
4. If NO-GO: Document findings and explore alternatives

**Next Week**:
1. Complete Phase 2B & 2C if GO decision
2. Test in production
3. Release v1.6.0 with parallel agents (or v1.5.12 with sequential+streaming)

---

## References

- **Current Status**: `PROGRAMMATIC-AGENTS-NOT-WORKING.md`
- **SDK Documentation**: `PYTHON-SDK-API-REFERENCE.md`
- **Original Plan**: `COMPREHENSIVE-AGENT-SDK-MIGRATION-AND-PERFORMANCE-PLAN.md`
- **Insights**: `CRITICAL-INSIGHTS-FOR-NAVAM.md`
- **Backlog**: `artifacts/backlog/active.md`

---

**Last Updated**: 2025-10-03
**Version**: v1.5.11 (stable baseline)
**Next Review**: After Phase 2A research complete
