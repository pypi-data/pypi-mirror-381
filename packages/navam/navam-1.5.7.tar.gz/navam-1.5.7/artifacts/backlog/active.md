# Active Backlog

**Last Updated**: 2025-10-03
**Current Version**: v1.5.5
**Status**: Phase 0, 1 & 2 Complete ✅ | Phase 3 Ready for Implementation

---

## 🎯 Current Focus: Phase 3 Implementation

### Phase 3: Cost Tracking (v1.5.6) - READY TO START
**Timeline**: 1-2 days
**Priority**: 🟡 HIGH
**Expected Impact**: Full visibility into costs and ROI

**Objectives:**
- [ ] Implement CostTracker class in new module `src/navam/cost_tracker.py`
- [ ] Integrate into message processing loop (chat.py)
- [ ] Track costs per step with message ID deduplication
- [ ] Calculate cache savings in USD
- [ ] Update `/perf` command with cost section
- [ ] Add agent-level cost breakdown
- [ ] Test cost calculations accuracy

**Success Metrics:**
- Cost displayed accurately in `/perf` command
- Cache savings measured in USD
- 30% cost reduction from caching + model optimization visible
- Agent-level cost breakdown working (per-agent spend tracking)

**Reference**: `active.md` (Phase 3 section below)

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
- ✅ Phase 1: Hook-Based Caching (v1.5.0-alpha)
- ✅ v1.5.3: Package structure fix (consistent `.claude/` layout)
- ✅ v1.5.4: Cache hooks activation fix
- ✅ Phase 2: Parallel Subagents (v1.5.5)

**Current:**
- 🔄 Phase 3: Cost Tracking (v1.5.6) - READY TO START

**Next:**
- ⏳ Phase 4: Streaming Reports (v1.6.0)

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

## 📋 Phase 2 Completion Summary

**Implemented**: 2025-10-03
**Files Changed**:
- ✅ Created: `src/navam/agent_configs.py` (165 lines)
- ✅ Modified: `src/navam/chat.py` (added agents integration)

**Agents Configured**:
- ✅ fundamental-analyst (Sonnet, 5 company research tools)
- ✅ technical-analyst (Sonnet, 4 stock analysis tools)
- ✅ news-analyst (Haiku, 5 news analysis tools)

**Validation Tests Passed**:
- ✅ Module imports successfully
- ✅ Agent configurations valid
- ✅ ClaudeAgentOptions accepts agents
- ✅ Tool access verified per agent

**Ready for Production Testing**:
- Expected workflow time: 2-3 minutes (down from 8-9 min)
- Expected speedup: 3-4x faster
- Cache hit rate: Maintained at ~70%
- Model optimization: news-analyst uses faster Haiku model

**Reference**: See `PHASE-2-PARALLEL-SUBAGENTS-COMPLETE.md` for detailed implementation notes

---

**Next Action**: Begin Phase 3 implementation (Cost Tracking)
