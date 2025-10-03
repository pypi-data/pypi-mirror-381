"""Tests for ELLIPSIS matching module."""

from pytest_bashdoctest.matcher import MatchResult, match_line, match_output, normalize_line


class TestNormalizeLine:
    """Tests for normalize_line function."""

    def test_strip_trailing_whitespace(self):
        """Trailing whitespace should be removed."""
        assert normalize_line("hello  \t  ") == "hello"

    def test_preserve_leading_whitespace(self):
        """Leading whitespace (JSON indentation) must be preserved."""
        assert normalize_line("  hello") == "  hello"

    def test_no_whitespace(self):
        """Lines with no whitespace stay unchanged."""
        assert normalize_line("hello") == "hello"

    def test_empty_line(self):
        """Empty lines become empty strings."""
        assert normalize_line("") == ""

    def test_only_whitespace(self):
        """Lines with only whitespace become empty."""
        assert normalize_line("   \t  ") == ""


class TestMatchLine:
    """Tests for string-level ELLIPSIS matching."""

    def test_exact_match_no_ellipsis(self):
        """Lines without ... must match exactly."""
        assert match_line('"username": "johndoe"', '"username": "johndoe"')
        assert not match_line('"username": "johndoe"', '"username": "different"')

    def test_string_ellipsis_in_url(self):
        """Test ELLIPSIS inside URL values."""
        expected = '"url": "https://.../path/....pdf"'
        actual = '"url": "https://example.com/path/file.pdf"'
        assert match_line(expected, actual)

    def test_string_ellipsis_partial_uuid(self):
        """Test partial UUID matching."""
        expected = '"id": "a665de5d-..."'
        actual = '"id": "a665de5d-d60c-4f95-8a99-920aa1095bfd"'
        assert match_line(expected, actual)

    def test_string_ellipsis_timestamp(self):
        """Test timestamp format validation."""
        expected = '"created_at": "2025-...-02T...Z"'  # Must match month-day
        actual = '"created_at": "2025-10-02T14:30:00Z"'
        assert match_line(expected, actual)

    def test_multiple_ellipsis_in_line(self):
        """Multiple ... in same line should work."""
        expected = '"url": "https://.../api/.../avatar.jpg"'
        actual = '"url": "https://example.com/api/v1/users/avatar.jpg"'
        assert match_line(expected, actual)

    def test_ellipsis_at_start(self):
        """Ellipsis at start of value."""
        expected = '"name": "...Doe"'
        actual = '"name": "John Doe"'
        assert match_line(expected, actual)

    def test_ellipsis_at_end(self):
        """Ellipsis at end of value."""
        expected = '"name": "John..."'
        actual = '"name": "John Doe"'
        assert match_line(expected, actual)

    def test_failed_match_wrong_start(self):
        """Match should fail if start doesn't match."""
        expected = '"url": "https://.../path"'
        actual = '"url": "http://example.com/path"'  # http vs https
        assert not match_line(expected, actual)

    def test_failed_match_wrong_end(self):
        """Match should fail if end doesn't match."""
        expected = '"file": "....pdf"'
        actual = '"file": "document.txt"'  # .txt vs .pdf
        assert not match_line(expected, actual)

    def test_order_matters(self):
        """Segments must appear in order."""
        expected = '"path": "/a/.../b/.../c"'
        actual = '"path": "/c/extra/b/more/a"'  # c-b-a instead of a-b-c
        assert not match_line(expected, actual)

        # Correct order should work
        actual_correct = '"path": "/a/extra/b/more/c"'
        assert match_line(expected, actual_correct)

    def test_object_ellipsis_simple(self):
        """Test {...} matches any object literal."""
        expected = '"impacts": {...}'
        actual = '"impacts": {"GWP_Total": {"A1-A3": 60.4}}'
        assert match_line(expected, actual)

    def test_object_ellipsis_nested(self):
        """Test {...} in nested structure."""
        expected = '"data": {"meta": {...}, "value": 123}'
        actual = '"data": {"meta": {"created": "2025-01-01", "author": "test"}, "value": 123}'
        assert match_line(expected, actual)

    def test_array_ellipsis_simple(self):
        """Test [...] matches any array literal."""
        expected = '"stages": [...]'
        actual = '"stages": ["A1-A3", "A4", "A5", "C1", "C2"]'
        assert match_line(expected, actual)

    def test_mixed_collection_ellipsis(self):
        """Test mixing {...} and [...] patterns."""
        expected = '"response": {"items": [...], "meta": {...}}'
        actual = '"response": {"items": ["a", "b", "c"], "meta": {"count": 3}}'
        assert match_line(expected, actual)

    def test_object_ellipsis_must_be_object(self):
        """Test {...} should not match non-objects."""
        expected = '"value": {...}'
        actual = '"value": "string"'
        assert not match_line(expected, actual)

        actual_number = '"value": 123'
        assert not match_line(expected, actual_number)

        actual_array = '"value": [1, 2, 3]'
        assert not match_line(expected, actual_array)

    def test_array_ellipsis_must_be_array(self):
        """Test [...] should not match non-arrays."""
        expected = '"items": [...]'
        actual = '"items": {"a": 1}'
        assert not match_line(expected, actual)


class TestMatchOutput:
    """Tests for line-level ELLIPSIS matching."""

    def test_exact_match_no_ellipsis(self):
        """Output without ... must match exactly."""
        expected = ["line1", "line2", "line3"]
        actual = ["line1", "line2", "line3"]
        result = match_output(expected, actual)
        assert result.success

    def test_line_ellipsis_skip_middle(self):
        """Standalone ... should skip middle content."""
        expected = ["{", '  "field": "value"', "  ...", "}"]
        actual = ["{", '  "field": "value"', '  "other": 123', '  "more": true', "}"]
        result = match_output(expected, actual)
        assert result.success

    def test_line_ellipsis_at_start(self):
        """Ellipsis at start skips beginning."""
        expected = ["  ...", '  "username": "johndoe"', "  ..."]
        actual = [
            "{",
            '  "id": "123"',
            '  "username": "johndoe"',
            '  "user_id": "USER-123"',
            "}",
        ]
        result = match_output(expected, actual)
        assert result.success

    def test_multiple_segments(self):
        """Multiple segments separated by ... should all match."""
        expected = [
            "{",
            '  "profile": {',
            "    ...",
            "  },",
            "  ...",
            '  "user_id": "USER-123"',
            "}",
        ]
        actual = [
            "{",
            '  "profile": {',
            '    "bio": "Software developer",',
            '    "location": "San Francisco"',
            "  },",
            '  "company": "TechCorp"',
            '  "username": "john"',
            '  "user_id": "USER-123"',
            "}",
        ]
        result = match_output(expected, actual)
        assert result.success

    def test_string_and_line_ellipsis_combined(self):
        """Combine string-level and line-level ELLIPSIS."""
        expected = [
            "{",
            '  "url": "https://.../file.pdf"',  # String-level ELLIPSIS
            "  ...",  # Line-level ELLIPSIS
            "}",
        ]
        actual = [
            "{",
            '  "url": "https://example.com/files/file.pdf"',
            '  "other": "data"',
            '  "more": "fields"',
            "}",
        ]
        result = match_output(expected, actual)
        assert result.success

    def test_failed_match_segment_not_found(self):
        """Match should fail if expected segment doesn't exist."""
        expected = ["{", '  "username": "johndoe"', "  ...", "}"]
        actual = ["{", '  "username": "different_user"', '  "other": "field"', "}"]
        result = match_output(expected, actual)
        assert not result.success
        assert result.failed_segment is not None
        # Check failed segment contains expected line
        assert any("username" in line and "johndoe" in line for line in result.failed_segment)

    def test_segments_must_be_sequential(self):
        """Segments must appear in order, not just anywhere."""
        expected = [
            '  "first": 1',
            "  ...",
            '  "second": 2',
            "  ...",
            '  "third": 3',
        ]
        # third appears before second - should fail
        actual = [
            '  "first": 1',
            '  "other": 0',
            '  "third": 3',  # Out of order!
            '  "more": 0',
            '  "second": 2',
        ]
        result = match_output(expected, actual)
        assert not result.success

    def test_empty_expected(self):
        """Empty expected output should match empty actual."""
        result = match_output([], [])
        assert result.success

    def test_just_ellipsis(self):
        """Just ... should match anything."""
        expected = ["..."]
        actual = ["line1", "line2", "line3", "line4"]
        # This creates an empty segments list, which should match
        result = match_output(expected, actual)
        assert result.success

    def test_trailing_whitespace_ignored(self):
        """Trailing whitespace should be ignored in matching."""
        expected = ['  "field": "value"']
        actual = ['  "field": "value"  \t  ']
        result = match_output(expected, actual)
        assert result.success

    def test_leading_whitespace_preserved(self):
        """Leading whitespace (indentation) must match."""
        expected = ['  "field": "value"']  # 2 spaces
        actual = ['    "field": "value"']  # 4 spaces - different!
        result = match_output(expected, actual)
        assert not result.success

    def test_match_result_position(self):
        """Failed match should report position."""
        expected = ["line1", "line2_expected", "line3"]
        actual = ["line1", "line2_different", "line3"]
        result = match_output(expected, actual)
        assert not result.success
        # Position should be around where the first segment starts searching
        assert result.position >= 0

    def test_object_ellipsis_multiline_simple(self):
        """Test {...} matches multi-line JSON object from jq -S."""
        expected = ['  "impacts": {...}']
        actual = ['  "impacts": {', '    "GWP_Total": {', '      "A1-A3": 1.94', "    }", "  }"]
        result = match_output(expected, actual)
        assert result.success

    def test_object_ellipsis_multiline_with_comma(self):
        """Test {...}, pattern with suffix (comma) in multi-line JSON."""
        expected = ['  "ADPE": {...},']
        actual = ['  "ADPE": {', '    "A1-A3": 0.000193,', '    "D": -0.00000524', "  },"]
        result = match_output(expected, actual)
        assert result.success

    def test_array_ellipsis_multiline(self):
        """Test [...] matches multi-line JSON array."""
        expected = ['  "stages": [...]']
        actual = ['  "stages": [', '    "A1-A3",', '    "A4",', '    "A5"', "  ]"]
        result = match_output(expected, actual)
        assert result.success

    def test_nested_collection_ellipsis_multiline(self):
        """Test nested {...} within {...} across multiple lines."""
        expected = ['  "impacts": {', '    "ADPE": {...},', '    "GWP_Total": {...}', "  }"]
        actual = [
            '  "impacts": {',
            '    "ADPE": {',
            '      "A1-A3": 0.000193,',
            '      "D": -0.00000524',
            "    },",
            '    "GWP_Total": {',
            '      "A1-A3": 1.94,',
            '      "D": -0.407',
            "    }",
            "  }",
        ]
        result = match_output(expected, actual)
        assert result.success

    def test_collection_ellipsis_must_balance(self):
        """Test {...} fails if JSON is unbalanced."""
        expected = ['  "data": {...}']
        actual = [
            '  "data": {',
            '    "incomplete": {',
            '      "missing_close": true',
            # Missing closing braces - unbalanced!
        ]
        result = match_output(expected, actual)
        assert not result.success


class TestMatchResultDataclass:
    """Tests for MatchResult dataclass."""

    def test_success_result(self):
        """Successful match has success=True."""
        result = MatchResult(success=True)
        assert result.success
        assert result.failed_segment is None
        assert result.position == 0

    def test_failure_result(self):
        """Failed match has details."""
        failed_seg = ['"field": "value"']
        result = MatchResult(
            success=False, failed_segment=failed_seg, position=5, message="Not found"
        )
        assert not result.success
        assert result.failed_segment == failed_seg
        assert result.position == 5
        assert "Not found" in result.message
