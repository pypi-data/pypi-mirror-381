# Active Backlog

**Last Updated**: 2025-10-03
**Current Version**: v1.5.11 (ROLLBACK TO STABLE)
**Status**: Phase 0 & 1 Complete ✅ | Phase 2 Needs Reimplementation

---

## 🎯 Current Focus: Phase 2 Reimplementation (CRITICAL)

### Phase 2: Parallel Subagents (v1.6.0) - NEEDS REIMPLEMENTATION
**Timeline**: 2-3 days
**Priority**: 🔴 CRITICAL
**Status**: ⚠️ BLOCKED - Programmatic agents not working in Python SDK
**Expected Impact**: 3-4x speed improvement

**Objectives:**
- [ ] Research alternative to programmatic `agents` parameter (NOT working in Python SDK)
- [ ] Evaluate options: file-based agents, Task tool with subagents, or wait for SDK fix
- [ ] Design architecture for parallel agent execution
- [ ] Implement selected approach with proper error handling
- [ ] Test with investment research workflow
- [ ] Measure actual speedup achieved

**Success Metrics:**
- Workflow time reduced from 8+ min to 2-3 min (3-4x faster)
- Parallel execution working correctly
- No regression in cache hit rate (maintain ~70%)
- All 18 Markdown agents continue working

**Blockers:**
- Python SDK `agents` parameter causes `'method' object is not iterable` error
- Issue traced to AgentDefinition.tools being a method instead of attribute
- TypeScript SDK has working programmatic agents, Python does not

**Reference**: See `PROGRAMMATIC-AGENTS-NOT-WORKING.md` and `PYTHON-SDK-API-REFERENCE.md`

---

## 📋 Upcoming Phases

### Phase 4: Streaming Reports (v1.6.0)
**Timeline**: 2-3 days
**Priority**: 🟢 MEDIUM
**Expected Impact**: 5x faster perceived speed, better UX

**Tasks:**
- [ ] Break report generation into sections (executive summary, fundamentals, technical, news, synthesis)
- [ ] Implement section-by-section streaming
- [ ] Display progressive results as each section completes
- [ ] Update progress indicators
- [ ] Test user experience

**Success Metrics:**
- Time to first section <30 seconds
- Progressive section display working
- Total time <2 minutes
- User sees results incrementally

**Reference**: `artifacts/backlog/COMPREHENSIVE-AGENT-SDK-MIGRATION-AND-PERFORMANCE-PLAN.md` (Lines 723-741)

---

## 🔍 Issues Under Investigation

### File Write Operations Slow (v1.4.7)
**Severity**: Medium
**Impact**: Report generation workflows
**Status**: 🔍 INVESTIGATING

**Problem:**
- Write to `/tmp/` directory: instant ✅
- Write to `reports/` directory: 2m 45s delay ❌
- Inconsistent behavior between different paths

**Next Steps:**
- [ ] Run production workflow with new timing logs enabled
- [ ] Capture exact timing: tool start → tool result received
- [ ] Check if DEBUG warning appears (permission handler called)
- [ ] Profile Claude Code SDK Write tool internals

**Reference**: `artifacts/backlog/performance-improvements.md` (Lines 436-509)

---

## 📚 Reference Documents

### Master Plan
- `COMPREHENSIVE-AGENT-SDK-MIGRATION-AND-PERFORMANCE-PLAN.md` - Complete implementation roadmap

### Analysis & Summaries
- `AGENT-SDK-ANALYSIS-SUMMARY.md` - Executive summary of discoveries
- `performance-improvements.md` - Ongoing performance tracking

### Completed Work (See archive-002.md and PHASE-2-PARALLEL-SUBAGENTS-COMPLETE.md)
- Phase 0: Migration to claude-agent-sdk v0.1.0 ✅
- Phase 1: Hook-based caching implementation ✅
- v1.5.3: Claude Code dependency fix ✅
- v1.5.4: Cache hooks activation fix ✅
- Phase 2: Parallel subagents implementation ✅

---

## 🎯 Overall Progress

**Completed:**
- ✅ Phase 0: SDK Migration (v1.5.0-alpha)
- ✅ Phase 1: Hook-Based Caching (v1.5.4)
- ✅ v1.5.3: Package structure fix (consistent `.claude/` layout)
- ✅ v1.5.11: Rollback to stable release (removed broken programmatic agents)

**Current:**
- 🔄 Phase 2: Parallel Subagents - BLOCKED, needs reimplementation

**Next:**
- ⏳ Phase 3: Cost Tracking (after Phase 2 complete)
- ⏳ Phase 4: Streaming Reports (after Phase 3 complete)

---

## 💡 Key Metrics (Current vs Target)

| Metric | v1.4.8 (Before) | v1.5.5 (Current) | v1.6.0 (Target) | Improvement |
|--------|-----------------|------------------|-----------------|-------------|
| Workflow Time | 8.3 min | 2-3 min* | 1.7 min | 70-65% faster |
| API Calls Saved | 0% | 70% | 70% | ✅ Achieved |
| Cost per Query | $1.32 | $0.40* | $0.30 | 70%+ cheaper |
| Cache Hit Rate | 0% | 70% | 70% | ✅ Achieved |
| Parallel Agents | No | Yes (3x) | Yes (3x) | ✅ Achieved |
| User Feedback | Blocking | Progressive | Streaming | Better |

*Estimated based on v1.5.5 implementation - needs production validation

---

## 🚨 Critical Workflow

**Before Building Package:**
```bash
# 1. ALWAYS sync development files to package
uv run python src/navam/sync.py

# 2. Verify sync succeeded
ls -la src/navam/.claude/agents/      # Should show 18 agents
ls -la src/navam/.claude/commands/invest/  # Should show 8 commands

# 3. Build package
uv run python -m build
```

**Why This Matters:**
- Package uses **consistent `.claude/` structure** for all resources
- Agents: `src/navam/.claude/agents/` (18 files)
- Commands: `src/navam/.claude/commands/invest/` (8 files)
- Development keeps everything in `.claude/` for Claude Code integration
- Sync script bridges the two without disturbing development setup
- **Without sync, package fails with "agents not found" errors**

---

## 📋 Phase 2 Implementation Attempts (Failed)

**Attempted**: 2025-10-03
**Status**: ❌ ROLLED BACK in v1.5.11

**What We Tried**:
- Created `src/navam/agent_configs.py` with programmatic AgentDefinition instances
- Passed `agents` parameter to ClaudeAgentOptions
- Configured 3 specialized agents (fundamental, technical, news)

**Why It Failed**:
- Python SDK `agents` parameter causes `'method' object is not iterable` error
- AgentDefinition.tools appears to be a method instead of attribute in Python SDK
- TypeScript SDK works, but Python SDK has bugs
- Multiple attempts (v1.5.5-v1.5.10) all failed with same error
- Error occurs at module load time in agent_configs.py

**Lessons Learned**:
- Programmatic agents NOT currently supported in Python SDK
- Need alternative approach for parallel execution
- Markdown file agents work reliably (18 agents in `.claude/agents/`)

**Reference**: See `PROGRAMMATIC-AGENTS-NOT-WORKING.md` for technical details

---

**Next Action**: Research alternative parallel execution approaches
