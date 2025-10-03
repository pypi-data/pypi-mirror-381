"""ELLIPSIS matching for bash output.

Implements multi-level ELLIPSIS matching:
1. Line-level: Standalone '...' lines skip blocks of output
2. String-level: '...' within strings matches partial content
3. Collection-level: '{...}' matches any JSON object, '[...]' matches any JSON array

Examples:
    Line-level:
        {
          "field1": "value1",
          ...
          "field999": "value999"
        }

    String-level:
        "url": "https://.../path/....pdf"

    Collection-level:
        "impacts": {...}
        "stages": [...]
"""

from dataclasses import dataclass


@dataclass
class MatchResult:
    """Result of output matching.

    Attributes:
        success: Whether the match succeeded
        failed_segment: The expected segment that failed to match (if any)
        position: Position in actual output where matching failed
        message: Optional error message
    """

    success: bool
    failed_segment: list[str] | None = None
    position: int = 0
    message: str | None = None


def normalize_line(line: str) -> str:
    """Strip trailing whitespace only.

    We use minimal normalization because jq -S produces deterministic output.
    Trailing whitespace is invisible and irrelevant, but leading whitespace
    shows JSON nesting structure and must be preserved.
    """
    return line.rstrip()


def match_line(expected: str, actual: str) -> bool:
    """Match single line with string-level ELLIPSIS support.

    Examples:
        expected: "url": "https://.../files/....pdf"
        actual:   "url": "https://example.com/files/doc-123.pdf"
        -> True

        expected: "username": "johndoe"
        actual:   "username": "johndoe"
        -> True

    Algorithm:
    1. Normalize both lines (rstrip)
    2. If no '...' in expected, must be exact match
    3. Split expected by '...' to get segments
    4. Check each segment appears in actual in order
    """
    expected = normalize_line(expected)
    actual = normalize_line(actual)

    if "..." not in expected:
        return expected == actual

    # Split expected by '...'
    parts = expected.split("...")
    pos = 0
    for part in parts:
        idx = actual.find(part, pos)
        if idx == -1:
            return False
        pos = idx + len(part)
    return True


def match_output(expected: list[str], actual: list[str]) -> MatchResult:
    """Match output with line-level ELLIPSIS support.

    Algorithm:
    1. Split expected into segments separated by '...' lines
    2. For each segment, find it in actual (in order)
    3. Use match_line() for each line within segment
    4. Return success + details on failure

    Returns:
        MatchResult with success status and failure details
    """
    # Split expected by standalone '...' lines
    segments = []
    current = []
    for line in expected:
        if line.strip() == "...":
            if current:
                segments.append(current)
                current = []
        else:
            current.append(line)
    if current:
        segments.append(current)

    # Match each segment sequentially
    actual_pos = 0
    for segment in segments:
        # Find this segment starting from actual_pos
        found_at = _find_segment(actual, segment, actual_pos)
        if found_at == -1:
            return MatchResult(
                success=False,
                failed_segment=segment,
                position=actual_pos,
                message=f"Segment not found: {segment}",
            )
        actual_pos = found_at + len(segment)

    return MatchResult(success=True)


def _find_segment(actual: list[str], segment: list[str], start: int) -> int:
    """Find segment in actual output starting from position start.

    Handles both regular line matching and multi-line collection patterns ({...}, [...]).

    Returns:
        Position where segment was found, or -1 if not found
    """
    # Try to match segment at each position
    for i in range(start, len(actual) - len(segment) + 1):
        pos = i
        for j, expected_line in enumerate(segment):
            if pos >= len(actual):
                break

            # Try regular single-line match first
            if match_line(expected_line, actual[pos]):
                pos += 1
            # If single-line fails and pattern has collection markers, try multi-line matching
            elif "{...}" in expected_line or "[...]" in expected_line:
                match_result = _match_collection_pattern(actual, expected_line, pos)
                if match_result == -1:
                    break  # Pattern didn't match, try next position
                pos = match_result  # Update position to after the matched collection
            else:
                # No match
                break
        else:
            # All lines in segment matched
            return i
    return -1


def _match_collection_pattern(actual: list[str], expected: str, start: int) -> int:
    """Match a collection pattern ({...} or [...]) against multi-line JSON.

    Args:
        actual: List of actual output lines
        expected: Expected line containing {...} or [...] pattern
        start: Starting position in actual

    Returns:
        Position after the matched collection, or -1 if no match
    """
    # Determine pattern type and split expected line
    if "{...}" in expected:
        pattern_start, pattern_end = "{", "}"
        parts = expected.split("{...}")
    elif "[...]" in expected:
        pattern_start, pattern_end = "[", "]"
        parts = expected.split("[...]")
    else:
        return -1

    if len(parts) != 2:
        return -1  # Invalid pattern (multiple {/[ in line)

    prefix = parts[0]
    suffix = parts[1]

    # Find line with prefix
    if start >= len(actual):
        return -1

    first_line = normalize_line(actual[start])
    prefix_norm = normalize_line(prefix)

    # Check if prefix matches the beginning of the line
    if not first_line.startswith(prefix_norm):
        return -1

    # Find where the opening bracket is in the actual line
    remaining = first_line[len(prefix_norm) :]
    if not remaining.lstrip().startswith(pattern_start):
        return -1

    # Track bracket depth to find matching closing bracket
    depth = 1
    pos = start + 1

    # Scan remaining part of first line for bracket balance
    for char in remaining[remaining.index(pattern_start) + 1 :]:
        if char == pattern_start:
            depth += 1
        elif char == pattern_end:
            depth -= 1
            if depth == 0:
                # Found closing bracket on same line - check suffix
                idx = first_line.rindex(pattern_end)
                line_suffix = first_line[idx + 1 :]
                if normalize_line(line_suffix) == normalize_line(suffix):
                    return start + 1
                return -1

    # Continue scanning subsequent lines
    while pos < len(actual) and depth > 0:
        line = normalize_line(actual[pos])
        for char in line:
            if char == pattern_start:
                depth += 1
            elif char == pattern_end:
                depth -= 1
                if depth == 0:
                    # Found closing bracket - check suffix
                    idx = line.rindex(pattern_end)
                    line_suffix = line[idx + 1 :]
                    if normalize_line(line_suffix) == normalize_line(suffix):
                        return pos + 1
                    return -1
        pos += 1

    # Unbalanced or not found
    return -1
