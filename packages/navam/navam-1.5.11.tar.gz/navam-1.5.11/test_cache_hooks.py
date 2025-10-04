#!/usr/bin/env python3
"""
Test script to verify cache hooks are working correctly.

This script tests:
1. Cache key generation for MCP tool calls
2. Pre-tool hook checking cache before execution
3. Post-tool hook storing results after execution
4. Cache hit on duplicate calls
"""

import sys
import asyncio
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from navam.cache_manager import SessionCache


def test_cache_key_generation():
    """Test that cache keys are generated consistently"""
    print("🧪 Testing cache key generation...")

    cache = SessionCache()

    # Test 1: Same tool and input should generate same key
    key1 = cache._make_key("mcp__stock-analyzer__analyze_stock", {"symbol": "AAPL"})
    key2 = cache._make_key("mcp__stock-analyzer__analyze_stock", {"symbol": "AAPL"})

    assert key1 == key2, f"Keys should match: {key1} != {key2}"
    print(f"  ✅ Same tool+input generates same key: {key1}")

    # Test 2: Different input should generate different key
    key3 = cache._make_key("mcp__stock-analyzer__analyze_stock", {"symbol": "TSLA"})

    assert key1 != key3, f"Keys should differ: {key1} == {key3}"
    print(f"  ✅ Different input generates different key: {key3}")

    # Test 3: Different tool should generate different key
    key4 = cache._make_key("mcp__company-research__get_company_profile", {"symbol": "AAPL"})

    assert key1 != key4, f"Keys should differ: {key1} == {key4}"
    print(f"  ✅ Different tool generates different key: {key4}")

    print()


def test_cache_storage_retrieval():
    """Test that cache stores and retrieves data correctly"""
    print("🧪 Testing cache storage and retrieval...")

    cache = SessionCache(ttl_seconds=300)

    tool_name = "mcp__stock-analyzer__analyze_stock"
    tool_input = {"symbol": "AAPL"}
    result = {"price": 150.0, "volume": 1000000}

    # Test 1: Store data
    cache.set(tool_name, tool_input, result)
    print(f"  ✅ Stored result in cache")

    # Test 2: Retrieve data
    cached = cache.get(tool_name, tool_input)

    assert cached == result, f"Retrieved data should match: {cached} != {result}"
    print(f"  ✅ Retrieved correct result from cache: {cached}")

    # Test 3: Different input should not hit cache
    cached2 = cache.get(tool_name, {"symbol": "TSLA"})

    assert cached2 is None, f"Should return None for cache miss: {cached2}"
    print(f"  ✅ Cache miss for different input returns None")

    # Test 4: Check cache statistics
    stats = cache.get_stats()
    print(f"  📊 Cache stats: {stats['cache_size']}/{stats['max_size']} entries, {stats['hit_rate']} hit rate")
    print()


async def test_hook_integration():
    """Test that hooks are properly integrated with cache"""
    print("🧪 Testing hook integration...")

    from navam.chat import InteractiveChat

    # Create chat instance (but don't start full session)
    chat = InteractiveChat()

    # Test 1: Verify hooks are registered
    if hasattr(chat, 'claude_options') and chat.claude_options:
        hooks = chat.claude_options.hooks
        if hooks:
            print(f"  ✅ Hooks registered: {list(hooks.keys())}")
        else:
            print(f"  ❌ No hooks found in claude_options")
            return False
    else:
        print(f"  ⚠️  Claude options not initialized (expected in constructor)")

    # Test 2: Test pre-tool hook logic
    result = await chat._pre_tool_use_hook("mcp__test_tool", {"param": "value"})
    print(f"  ✅ Pre-tool hook returns: {result}")
    assert result.get("behavior") == "allow", "First call should allow execution"

    # Test 3: Store result in cache via post-tool hook
    await chat._post_tool_use_hook("mcp__test_tool", {"param": "value"}, {"data": "test"})
    print(f"  ✅ Post-tool hook stored result")

    # Test 4: Second call should hit cache
    result2 = await chat._pre_tool_use_hook("mcp__test_tool", {"param": "value"})
    print(f"  ✅ Second pre-tool hook returns: {result2}")
    assert result2.get("behavior") == "deny", "Second call should deny (cache hit)"
    assert result2.get("result") == {"data": "test"}, "Should return cached result"

    # Test 5: Check cache statistics
    stats = chat.session_cache.get_stats()
    print(f"  📊 Final cache stats: {stats['cache_size']}/{stats['max_size']} entries")
    print()

    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("Cache Hooks Integration Test")
    print("=" * 60)
    print()

    try:
        # Run synchronous tests
        test_cache_key_generation()
        test_cache_storage_retrieval()

        # Run async tests
        asyncio.run(test_hook_integration())

        print("=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Test with actual MCP tool call")
        print("2. Verify /cache command shows entries")
        print("3. Run production test with /invest:research-stock")

        return 0

    except Exception as e:
        print()
        print("=" * 60)
        print(f"❌ TEST FAILED: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
