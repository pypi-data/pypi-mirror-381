#!/usr/bin/env python3
"""Crackerjack integration tools for session-mgmt-mcp.

Following crackerjack architecture patterns for quality monitoring,
code analysis, and development workflow integration.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from session_mgmt_mcp.crackerjack_integration import CrackerjackResult

logger = logging.getLogger(__name__)


def _format_execution_status(result: CrackerjackResult) -> str:
    """Format execution status for output."""
    if result.exit_code == 0:
        return "✅ **Status**: Success\n"
    return f"❌ **Status**: Failed (exit code: {result.exit_code})\n"


def _format_output_sections(result: CrackerjackResult) -> str:
    """Format stdout and stderr sections."""
    output = ""
    if result.stdout.strip():
        output += f"\n**Output**:\n```\n{result.stdout}\n```\n"
    if result.stderr.strip():
        output += f"\n**Errors**:\n```\n{result.stderr}\n```\n"
    return output


def _format_metrics_section(result: CrackerjackResult) -> str:
    """Format metrics and insights sections."""
    output = "\n📊 **Metrics**:\n"
    output += f"- Execution time: {result.execution_time:.2f}s\n"
    output += f"- Exit code: {result.exit_code}\n"

    if result.quality_metrics:
        output += "\n📈 **Quality Metrics**:\n"
        for metric, value in result.quality_metrics.items():
            output += f"- {metric.replace('_', ' ').title()}: {value:.1f}\n"

    if result.memory_insights:
        output += "\n🧠 **Insights**:\n"
        for insight in result.memory_insights[:5]:  # Limit to top 5
            output += f"- {insight}\n"

    return output


# Implementation functions (extracted from registration function)
async def _execute_crackerjack_command_impl(
    command: str,
    args: str = "",
    working_directory: str = ".",
    timeout: int = 300,
    ai_agent_mode: bool = False,
) -> str:
    """Execute a Crackerjack command with enhanced AI integration."""
    try:
        from session_mgmt_mcp.crackerjack_integration import CrackerjackIntegration

        integration = CrackerjackIntegration()
        result = await integration.execute_crackerjack_command(
            command,
            args.split() if args else None,
            working_directory,
            timeout,
            ai_agent_mode,
        )

        # Format response
        output = f"🔧 **Crackerjack {command}** executed\n\n"
        output += _format_execution_status(result)
        output += _format_output_sections(result)
        output += _format_metrics_section(result)

        return output

    except ImportError:
        logger.warning("Crackerjack integration not available")
        return "❌ Crackerjack integration not available. Install crackerjack package."
    except Exception as e:
        logger.exception(f"Crackerjack execution failed: {e}")
        return f"❌ Crackerjack execution failed: {e!s}"


async def _crackerjack_run_impl(
    command: str,
    args: str = "",
    working_directory: str = ".",
    timeout: int = 300,
    ai_agent_mode: bool = False,
) -> str:
    """Run crackerjack with enhanced analytics (replaces /crackerjack:run)."""
    try:
        from session_mgmt_mcp.crackerjack_integration import CrackerjackIntegration

        # Use the enhanced execution method
        integration = CrackerjackIntegration()
        result = await integration.execute_crackerjack_command(
            command,
            args.split() if args else None,
            working_directory,
            timeout,
            ai_agent_mode,
        )

        # Format response similar to execute_crackerjack_command
        formatted_result = f"🔧 **Crackerjack {command}** executed\n\n"

        if result.exit_code == 0:
            formatted_result += "✅ **Status**: Success\n"
        else:
            formatted_result += (
                f"❌ **Status**: Failed (exit code: {result.exit_code})\n"
            )

        if result.stdout.strip():
            formatted_result += f"\n**Output**:\n```\n{result.stdout}\n```\n"

        if result.stderr.strip():
            formatted_result += f"\n**Errors**:\n```\n{result.stderr}\n```\n"

        # Add session management integration
        output = f"🔧 **Enhanced Crackerjack Run**\n\n{formatted_result}\n"

        # Store execution in history
        try:
            from session_mgmt_mcp.reflection_tools import ReflectionDatabase

            # Store in reflection database for future reference
            db = ReflectionDatabase()
            async with db:
                await db.store_conversation(
                    content=f"Crackerjack {command} execution: {formatted_result[:500]}...",
                    metadata={"project": Path(working_directory).name},
                )

            output += "📝 Execution stored in session history\n"

        except Exception as e:
            logger.debug(f"Failed to store crackerjack execution: {e}")

        return output

    except Exception as e:
        logger.exception(f"Enhanced crackerjack run failed: {e}")
        return f"❌ Enhanced crackerjack run failed: {e!s}"


def _extract_crackerjack_commands(
    results: list[dict[str, Any]],
) -> dict[str, list[Any]]:
    """Extract crackerjack commands from results."""
    commands: dict[str, list[Any]] = {}

    for result in results:
        content = result.get("content", "")
        if "crackerjack" in content.lower():
            # Extract command from content

            # Use validated pattern for command extraction
            from session_mgmt_mcp.utils.regex_patterns import SAFE_PATTERNS

            crackerjack_cmd_pattern = SAFE_PATTERNS["crackerjack_command"]
            match = crackerjack_cmd_pattern.search(content.lower())
            cmd = match.group(1) if match else "unknown"

            if cmd not in commands:
                commands[cmd] = []
            commands[cmd].append(result)

    return commands


def _format_recent_executions(results: list[dict[str, Any]]) -> str:
    """Format recent executions for output."""
    output = "**Recent Executions**:\n"

    for i, result in enumerate(results[:10], 1):
        timestamp = result.get("timestamp", "Unknown")
        content = result.get("content", "")[:100]
        output += f"{i}. ({timestamp}) {content}...\n"

    return output


async def _crackerjack_history_impl(
    command_filter: str = "",
    days: int = 7,
    working_directory: str = ".",
) -> str:
    """View crackerjack execution history with trends and patterns."""
    try:
        from datetime import datetime, timedelta

        from session_mgmt_mcp.reflection_tools import ReflectionDatabase

        db = ReflectionDatabase()
        async with db:
            # Search for crackerjack executions
            end_date = datetime.now()
            end_date - timedelta(days=days)

            results = await db.search_conversations(
                query=f"crackerjack {command_filter}".strip(),
                project=Path(working_directory).name,
                limit=50,
            )

            if not results:
                return f"📊 No crackerjack executions found in last {days} days"

            output = f"📊 **Crackerjack History** (last {days} days)\n\n"

            # Group by command
            commands = _extract_crackerjack_commands(results)

            # Display summary
            output += f"**Total Executions**: {len(results)}\n"
            output += f"**Commands Used**: {', '.join(commands.keys())}\n\n"

            # Show recent executions
            output += _format_recent_executions(results)

            return output

    except Exception as e:
        logger.exception(f"Crackerjack history failed: {e}")
        return f"❌ History retrieval failed: {e!s}"


def _calculate_execution_summary(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate basic execution summary statistics."""
    success_count = sum(1 for r in results if "success" in r.get("content", "").lower())
    failure_count = len(results) - success_count
    return {
        "total": len(results),
        "success": success_count,
        "failure": failure_count,
        "success_rate": (success_count / len(results) * 100) if results else 0,
    }


def _extract_quality_keywords(results: list[dict[str, Any]]) -> dict[str, int]:
    """Extract quality keyword counts from results."""
    quality_keywords = ["lint", "test", "security", "complexity", "coverage"]
    keyword_counts: dict[str, int] = {}

    for result in results:
        content = result.get("content", "").lower()
        for keyword in quality_keywords:
            if keyword in content:
                keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1

    return keyword_counts


def _format_quality_metrics_output(
    days: int, summary: dict[str, Any], keywords: dict[str, int]
) -> str:
    """Format quality metrics output."""
    output = f"📊 **Crackerjack Quality Metrics** (last {days} days)\n\n"
    output += "**Execution Summary**:\n"
    output += f"- Total runs: {summary['total']}\n"
    output += f"- Successful: {summary['success']}\n"
    output += f"- Failed: {summary['failure']}\n"
    output += f"- Success rate: {summary['success_rate']:.1f}%\n\n"

    if keywords:
        output += "**Quality Focus Areas**:\n"
        for keyword, count in sorted(
            keywords.items(), key=lambda x: x[1], reverse=True
        ):
            output += f"- {keyword.title()}: {count} mentions\n"

    output += "\n💡 Use `crackerjack analyze` for detailed quality analysis"
    return output


async def _crackerjack_metrics_impl(
    working_directory: str = ".", days: int = 30
) -> str:
    """Get quality metrics trends from crackerjack execution history."""
    try:
        from session_mgmt_mcp.reflection_tools import ReflectionDatabase

        db = ReflectionDatabase()
        async with db:
            results = await db.search_conversations(
                query="crackerjack metrics quality",
                project=Path(working_directory).name,
                limit=100,
            )

            if not results:
                return f"📊 **Crackerjack Quality Metrics** (last {days} days)\n\nNo quality metrics data available\n💡 Run `crackerjack analyze` to generate metrics\n"

            summary = _calculate_execution_summary(results)
            keywords = _extract_quality_keywords(results)
            return _format_quality_metrics_output(days, summary, keywords)

    except Exception as e:
        logger.exception(f"Metrics analysis failed: {e}")
        return f"❌ Metrics analysis failed: {e!s}"


def _find_keyword_matches(content: str, keyword: str) -> list[tuple[int, int]]:
    """Find all occurrences of a keyword in content."""
    matches = []
    start_pos = 0
    while True:
        pos = content.find(keyword, start_pos)
        if pos == -1:
            break
        matches.append((pos, pos + len(keyword)))
        start_pos = pos + 1
    return matches


def _extract_context_around_keyword(
    content: str, keyword: str, context_size: int = 30
) -> list[str]:
    """Extract context around keyword occurrences."""
    matches = _find_keyword_matches(content, keyword)
    contexts = []

    for start_pos, end_pos in matches:
        start = max(0, start_pos - context_size)
        end = min(len(content), end_pos + context_size)
        context = content[start:end].strip()
        contexts.append(context)

    return contexts


def _extract_failure_patterns(
    results: list[dict[str, Any]], failure_keywords: list[str]
) -> dict[str, int]:
    """Extract common failure patterns from test results."""
    patterns: dict[str, int] = {}

    for result in results:
        content = result.get("content", "").lower()
        for keyword in failure_keywords:
            if keyword in content:
                contexts = _extract_context_around_keyword(content, keyword)
                for context in contexts:
                    patterns[context] = patterns.get(context, 0) + 1

    return patterns


def _format_failure_patterns(patterns: dict[str, int]) -> str:
    """Format failure patterns for output."""
    output = ""

    if patterns:
        output += "**Common Failure Patterns**:\n"
        sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)

        for i, (pattern, count) in enumerate(sorted_patterns[:10], 1):
            output += f"{i}. ({count}x) {pattern}...\n"

        output += f"\n📊 Total unique patterns: {len(patterns)}\n"
        output += f"📊 Total failure mentions: {sum(patterns.values())}\n"
    else:
        output += "No clear failure patterns identified\n"

    return output


def _get_failure_keywords() -> list[str]:
    """Get list of keywords to identify failure patterns."""
    return [
        "failed",
        "error",
        "exception",
        "assertion",
        "timeout",
    ]


async def _get_failure_pattern_results(
    working_directory: str, limit: int = 50
) -> list[dict[str, Any]]:
    """Get failure pattern results from the reflection database."""
    from session_mgmt_mcp.reflection_tools import ReflectionDatabase

    db = ReflectionDatabase()
    async with db:
        return await db.search_conversations(
            query="test failure error pattern",
            project=Path(working_directory).name,
            limit=limit,
        )


def _format_patterns_header(days: int, results_count: int) -> str:
    """Format the header for the patterns output."""
    output = f"🔍 **Test Failure Patterns** (last {days} days)\n\n"

    if not results_count:
        output += "No test failure patterns found\n"
        output += "✅ This might indicate good code quality!\n"

    return output


async def _crackerjack_patterns_impl(
    days: int = 7, working_directory: str = "."
) -> str:
    """Analyze test failure patterns and trends."""
    try:
        results = await _get_failure_pattern_results(working_directory)

        output = _format_patterns_header(days, len(results))

        if not results:
            return output

        # Extract common failure patterns
        failure_keywords = _get_failure_keywords()
        patterns = _extract_failure_patterns(results, failure_keywords)
        output += _format_failure_patterns(patterns)

        return output

    except Exception as e:
        logger.exception(f"Pattern analysis failed: {e}")
        return f"❌ Pattern analysis failed: {e!s}"


async def _crackerjack_help_impl() -> str:
    """Get comprehensive help for choosing the right crackerjack commands."""
    return """🔧 **Crackerjack Command Guide**

**Quick Quality Checks**:
- `crackerjack` - Fast lint and format
- `crackerjack -t` - Include tests
- `crackerjack --ai-fix -t` - AI-powered autonomous fixing

**Analysis Commands**:
- `crackerjack analyze` - Code quality analysis
- `crackerjack security` - Security scanning
- `crackerjack complexity` - Complexity analysis
- `crackerjack typecheck` - Type checking

**Development Workflow**:
- `crackerjack lint` - Code formatting and linting
- `crackerjack test` - Run test suite
- `crackerjack check` - Comprehensive quality checks
- `crackerjack clean` - Clean temporary files

**Advanced Features**:
- `--ai-fix` - Enable autonomous AI fixing
- `--verbose` - Detailed output
- `--fix` - Automatically fix issues where possible

**MCP Integration**:
- Use `execute_crackerjack_command` for any crackerjack command
- Use `crackerjack_run` for enhanced analytics and history
- Use `crackerjack_metrics` for quality trends

💡 **Pro Tips**:
- Always run `crackerjack -t` before commits
- Use `--ai-fix` for complex quality issues
- Check `crackerjack_history` to learn from past runs
- Monitor trends with `crackerjack_metrics`
"""


async def _crackerjack_quality_trends_impl(
    days: int = 30,
    working_directory: str = ".",
) -> str:
    """Analyze quality trends over time with actionable insights."""
    try:
        from session_mgmt_mcp.reflection_tools import ReflectionDatabase

        db = ReflectionDatabase()
        async with db:
            results = await db.search_conversations(
                query="crackerjack quality success failed",
                project=Path(working_directory).name,
                limit=200,
            )

            output = f"📈 **Quality Trends Analysis** (last {days} days)\n\n"

            if len(results) < 5:
                return _format_insufficient_trend_data(output)

            success_trend, failure_trend = _analyze_quality_trend_results(results)
            success_rate = _calculate_trend_success_rate(success_trend, failure_trend)

            output += _format_trend_overview(success_trend, failure_trend, success_rate)
            output += _format_trend_quality_insights(success_rate)
            output += _format_trend_recommendations(success_rate)

            return output

    except Exception as e:
        logger.exception(f"Trend analysis failed: {e}")
        return f"❌ Trend analysis failed: {e!s}"


def _format_insufficient_trend_data(output: str) -> str:
    """Format output when insufficient trend data is available."""
    output += "Insufficient data for trend analysis\n"
    output += "💡 Run more crackerjack commands to build trend history\n"
    return output


def _analyze_quality_trend_results(
    results: list[dict[str, Any]],
) -> tuple[list[str], list[str]]:
    """Analyze results to categorize success and failure trends."""
    success_trend = []
    failure_trend = []

    for result in results:
        content = result.get("content", "").lower()
        timestamp = result.get("timestamp", "")

        if "success" in content or "✅" in content:
            success_trend.append(timestamp)
        elif "failed" in content or "error" in content or "❌" in content:
            failure_trend.append(timestamp)

    return success_trend, failure_trend


def _calculate_trend_success_rate(
    success_trend: list[str], failure_trend: list[str]
) -> float:
    """Calculate success rate from trend data."""
    total_runs = len(success_trend) + len(failure_trend)
    return (len(success_trend) / total_runs * 100) if total_runs > 0 else 0


def _format_trend_overview(
    success_trend: list[str], failure_trend: list[str], success_rate: float
) -> str:
    """Format overall trends section."""
    total_runs = len(success_trend) + len(failure_trend)
    output = "**Overall Trends**:\n"
    output += f"- Total quality runs: {total_runs}\n"
    output += f"- Success rate: {success_rate:.1f}%\n"
    output += f"- Success trend: {len(success_trend)} passes\n"
    output += f"- Failure trend: {len(failure_trend)} issues\n\n"
    return output


def _format_trend_quality_insights(success_rate: float) -> str:
    """Format quality insights based on success rate."""
    if success_rate > 80:
        return (
            "🎉 **Excellent quality trend!** Your code quality is consistently high.\n"
        )
    if success_rate > 60:
        return "✅ **Good quality trend.** Room for improvement in consistency.\n"
    return "⚠️ **Quality attention needed.** Consider more frequent quality checks.\n"


def _format_trend_recommendations(success_rate: float) -> str:
    """Format quality recommendations based on success rate."""
    output = "\n**Recommendations**:\n"
    if success_rate < 70:
        output += "- Run `crackerjack --ai-fix -t` for automated fixing\n"
        output += "- Increase frequency of quality checks\n"
        output += "- Focus on test coverage improvement\n"
    else:
        output += "- Maintain current quality practices\n"
        output += "- Consider adding complexity monitoring\n"
    return output


async def _crackerjack_health_check_impl() -> str:
    """Check Crackerjack integration health and provide diagnostics."""
    output = "🔧 **Crackerjack Health Check**\n\n"

    try:
        # Check if crackerjack is available
        import subprocess

        result = subprocess.run(
            ["python", "-m", "crackerjack", "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode == 0:
            output += "✅ **Crackerjack Installation**: Available\n"
            output += f"   Version: {result.stdout.strip()}\n"
        else:
            output += "❌ **Crackerjack Installation**: Not working properly\n"
            output += f"   Error: {result.stderr}\n"

    except subprocess.TimeoutExpired:
        output += "⏰ **Crackerjack Installation**: Timeout (slow system?)\n"
    except FileNotFoundError:
        output += "❌ **Crackerjack Installation**: Not found\n"
        output += "   💡 Install with: `uv add crackerjack`\n"
    except Exception as e:
        output += f"❌ **Crackerjack Installation**: Error - {e!s}\n"

    # Check integration components
    try:
        # CrackerjackIntegration will be imported when needed
        import session_mgmt_mcp.crackerjack_integration  # noqa: F401

        output += "✅ **Integration Module**: Available\n"
    except ImportError:
        output += "❌ **Integration Module**: Not available\n"

    # Check reflection database for history
    try:
        from session_mgmt_mcp.reflection_tools import ReflectionDatabase

        db = ReflectionDatabase()
        async with db:
            # Quick test
            stats = await db.get_stats()
            output += "✅ **History Storage**: Available\n"
            output += f"   Conversations: {stats.get('conversation_count', 0)}\n"
    except Exception as e:
        output += f"⚠️ **History Storage**: Limited - {e!s}\n"

    output += "\n**Recommendations**:\n"
    output += "- Run `crackerjack -t` to test full functionality\n"
    output += "- Use `crackerjack_run` for enhanced analytics\n"
    output += "- Check `crackerjack_history` for execution patterns\n"

    return output


def register_crackerjack_tools(mcp: Any) -> None:
    """Register all crackerjack integration MCP tools.

    Args:
        mcp: FastMCP server instance

    """

    @mcp.tool()  # type: ignore[misc]
    async def execute_crackerjack_command(
        command: str,
        args: str = "",
        working_directory: str = ".",
        timeout: int = 300,
        ai_agent_mode: bool = False,
    ) -> str:
        """Execute a Crackerjack command with enhanced AI integration."""
        return await _execute_crackerjack_command_impl(
            command, args, working_directory, timeout, ai_agent_mode
        )

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_run(
        command: str,
        args: str = "",
        working_directory: str = ".",
        timeout: int = 300,
        ai_agent_mode: bool = False,
    ) -> str:
        """Run crackerjack with enhanced analytics (replaces /crackerjack:run)."""
        return await _crackerjack_run_impl(
            command, args, working_directory, timeout, ai_agent_mode
        )

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_history(
        command_filter: str = "",
        days: int = 7,
        working_directory: str = ".",
    ) -> str:
        """View crackerjack execution history with trends and patterns."""
        return await _crackerjack_history_impl(command_filter, days, working_directory)

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_metrics(working_directory: str = ".", days: int = 30) -> str:
        """Get quality metrics trends from crackerjack execution history."""
        return await _crackerjack_metrics_impl(working_directory, days)

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_patterns(days: int = 7, working_directory: str = ".") -> str:
        """Analyze test failure patterns and trends."""
        return await _crackerjack_patterns_impl(days, working_directory)

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_help() -> str:
        """Get comprehensive help for choosing the right crackerjack commands."""
        return await _crackerjack_help_impl()

    @mcp.tool()  # type: ignore[misc]
    async def get_crackerjack_results_history(
        command_filter: str = "",
        days: int = 7,
        working_directory: str = ".",
    ) -> str:
        """Get recent Crackerjack command execution history."""
        return await _crackerjack_history_impl(command_filter, days, working_directory)

    @mcp.tool()  # type: ignore[misc]
    async def get_crackerjack_quality_metrics(
        days: int = 30,
        working_directory: str = ".",
    ) -> str:
        """Get quality metrics trends from Crackerjack execution history."""
        return await _crackerjack_metrics_impl(working_directory, days)

    @mcp.tool()  # type: ignore[misc]
    async def analyze_crackerjack_test_patterns(
        days: int = 7,
        working_directory: str = ".",
    ) -> str:
        """Analyze test failure patterns and trends for debugging insights."""
        return await _crackerjack_patterns_impl(days, working_directory)

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_quality_trends(
        days: int = 30,
        working_directory: str = ".",
    ) -> str:
        """Analyze quality trends over time with actionable insights."""
        return await _crackerjack_quality_trends_impl(days, working_directory)

    @mcp.tool()  # type: ignore[misc]
    async def crackerjack_health_check() -> str:
        """Check Crackerjack integration health and provide diagnostics."""
        return await _crackerjack_health_check_impl()

    # Alias for backward compatibility
    @mcp.tool()  # type: ignore[misc]
    async def quality_monitor() -> str:
        """Phase 3: Proactive quality monitoring with early warning system."""
        return await _crackerjack_health_check_impl()
