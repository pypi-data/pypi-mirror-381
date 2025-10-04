"""
Agent configuration for parallel subagents using Claude Agent SDK.

This module defines specialized agents for investment research that can run in parallel,
enabling 3-4x speed improvements over sequential execution.
"""

from typing import Dict, List, Any


# Investment Research Subagents Configuration
# These agents run in parallel for the /invest:research-stock command
INVESTMENT_RESEARCH_AGENTS: Dict[str, Dict[str, Any]] = {
    "fundamental-analyst": {
        "description": "Analyze company financials, fundamentals, filings, and insider trading",
        "prompt": """You are a fundamental analysis specialist. Focus on:
- Company profile and business model
- Financial statements (income, balance sheet, cash flow)
- Key financial ratios and metrics
- SEC filings and regulatory disclosures
- Insider trading patterns
- Analyst ratings and consensus
- Valuation metrics (P/E, P/B, PEG, etc.)

Provide data-driven analysis without speculation. Highlight key strengths and risks.""",
        "tools": [
            "mcp__company-research__get_company_profile",
            "mcp__company-research__get_company_financials",
            "mcp__company-research__get_company_filings",
            "mcp__company-research__get_insider_trading",
            "mcp__company-research__get_analyst_ratings",
        ],
        "model": "claude-sonnet-4-20250514",  # Sonnet for complex analysis
    },
    "technical-analyst": {
        "description": "Analyze stock price patterns, technical indicators, and market trends",
        "prompt": """You are a technical analysis specialist. Focus on:
- Current price action and trends
- Technical indicators (RSI, MACD, moving averages, etc.)
- Support and resistance levels
- Trading volume patterns
- Price momentum and volatility
- Relative performance vs market
- Chart patterns and signals

Provide objective technical assessment based on data. Identify key levels and trends.""",
        "tools": [
            "mcp__stock-analyzer__analyze_stock",
            "mcp__stock-analyzer__get_moving_averages",
            "mcp__stock-analyzer__compare_stocks",
            "mcp__stock-analyzer__find_trending_stocks",
        ],
        "model": "claude-sonnet-4-20250514",  # Sonnet for pattern recognition
    },
    "news-analyst": {
        "description": "Analyze news sentiment, market trends, and narrative analysis",
        "prompt": """You are a news and sentiment analysis specialist. Focus on:
- Recent company-specific news and events
- Market sentiment and trending topics
- Narrative themes and market perception
- News impact on stock performance
- Sector and industry trends
- Competitive landscape news
- Risk events and catalysts

Synthesize news into actionable insights. Identify sentiment shifts and key catalysts.""",
        "tools": [
            "mcp__news-analyzer__get_company_news",
            "mcp__news-analyzer__search_news",
            "mcp__news-analyzer__analyze_sentiment",
            "mcp__news-analyzer__get_trending_topics",
            "mcp__news-analyzer__summarize_news",
        ],
        "model": "claude-haiku-4-20250611",  # Haiku for speed and cost efficiency
    },
}


# Agent tool access mapping for validation
AGENT_TOOL_MAPPINGS: Dict[str, List[str]] = {
    agent_name: config["tools"]
    for agent_name, config in INVESTMENT_RESEARCH_AGENTS.items()
}


def get_agent_config(agent_name: str) -> Dict[str, Any]:
    """
    Get configuration for a specific agent.

    Args:
        agent_name: Name of the agent (e.g., 'fundamental-analyst')

    Returns:
        Agent configuration dictionary

    Raises:
        KeyError: If agent name not found
    """
    return INVESTMENT_RESEARCH_AGENTS[agent_name]


def get_all_agent_names() -> List[str]:
    """Get list of all configured agent names."""
    return list(INVESTMENT_RESEARCH_AGENTS.keys())


def validate_agent_tools(agent_name: str, available_tools: List[str]) -> bool:
    """
    Validate that an agent has access to all its required tools.

    Args:
        agent_name: Name of the agent
        available_tools: List of available tool names

    Returns:
        True if all required tools are available, False otherwise
    """
    required_tools = AGENT_TOOL_MAPPINGS.get(agent_name, [])
    return all(tool in available_tools for tool in required_tools)


# Default agent configuration for non-parallel workflows
DEFAULT_AGENT_CONFIG: Dict[str, Any] = {
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 8192,
    "temperature": 0.0,  # Deterministic for research
}


def get_agent_options_for_research() -> Dict[str, Any]:
    """
    Get ClaudeAgentOptions configuration for investment research.

    Returns:
        Dictionary suitable for ClaudeAgentOptions initialization
    """
    return {
        "agents": INVESTMENT_RESEARCH_AGENTS,
        "parallel_execution": True,  # Enable parallel subagents
        "stream_results": True,  # Stream results as they complete
    }
