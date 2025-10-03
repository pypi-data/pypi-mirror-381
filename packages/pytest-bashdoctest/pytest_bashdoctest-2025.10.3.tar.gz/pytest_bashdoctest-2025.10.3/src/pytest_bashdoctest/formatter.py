"""Format failure messages with highlighting."""

from pytest_bashdoctest.executor import CommandResult
from pytest_bashdoctest.matcher import MatchResult
from pytest_bashdoctest.parser import BashExample


def format_failure(example: BashExample, result: CommandResult, match_result: MatchResult) -> str:
    """Format failure message with full output + highlighting.

    Structure:
    1. Header: FAILED: Bash example at line X
    2. Command: The actual command that ran
    3. Expected segment: What we were looking for
    4. Actual output: Full output with arrows pointing to mismatch

    Args:
        example: The bash example that failed
        result: The command execution result
        match_result: The match result with failure details

    Returns:
        Multiline string for pytest to display
    """
    lines = [
        f"FAILED: Bash example at line {example.line_number}",
        "",
        "Command:",
        f"  $ {example.command}",
        "",
    ]

    if match_result.failed_segment:
        lines.extend(
            [
                "Expected segment not found:",
                *[f"  {line}" for line in match_result.failed_segment],
                "",
            ]
        )

    lines.extend(
        [
            "Full actual output:",
            *_highlight_output(result.stdout, match_result),
        ]
    )

    return "\n".join(lines)


def _highlight_output(output: str, match_result: MatchResult) -> list[str]:
    """Add arrows pointing to mismatch location.

    Args:
        output: The actual command output
        match_result: The match result with position info

    Returns:
        List of formatted output lines with highlighting
    """
    lines = output.split("\n")
    result = []

    for i, line in enumerate(lines):
        if i == match_result.position:
            result.append(f"  {line}  <- Mismatch here")
        else:
            result.append(f"  {line}")

    return result
