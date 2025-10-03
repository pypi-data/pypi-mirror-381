"""Integration tests for the bash doctest plugin.

These tests use pytest's pytester fixture to test the plugin in isolation.
They verify the full pipeline: markdown → parse → execute → match → report.
"""

import textwrap


def test_requires_flag_to_collect(pytester):
    """Plugin should NOT collect markdown without --bashdoctest flag."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "hello"
            hello
            ```
            """
        ),
    )

    # Run WITHOUT --bashdoctest flag
    result = pytester.runpytest("--collect-only", "-v")

    # Should NOT find bash examples
    assert "DEMO.md" not in result.stdout.str()
    result.assert_outcomes()  # Should have no items collected


def test_collects_with_flag(pytester):
    """Plugin SHOULD collect markdown WITH --bashdoctest flag."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "hello"
            hello
            ```
            """
        ),
    )

    # Run WITH --bashdoctest flag
    result = pytester.runpytest("--bashdoctest", "--collect-only", "-v")

    # Should find bash example
    result.stdout.fnmatch_lines(["*DEMO.md*", "*line_*"])


def test_plugin_collects_bash_examples(pytester):
    """Plugin should collect bash code blocks from markdown files."""
    # Create a markdown file with bash examples
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            # Test Documentation

            ```bash
            $ echo "hello"
            hello
            ```
            """
        ),
    )

    # Run pytest with --bashdoctest flag
    result = pytester.runpytest("--bashdoctest", "--collect-only")

    # Should find the bash example
    result.stdout.fnmatch_lines(["*DEMO.md*"])


def test_simple_bash_example_passes(pytester):
    """Simple bash example that matches should pass."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "test"
            test
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should pass
    result.assert_outcomes(passed=1)


def test_bash_example_with_ellipsis_passes(pytester):
    """Bash example with ELLIPSIS should match correctly."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo '{"aaa": "first", "bbb": "middle", "zzz": "last"}' | jq -S
            {
              "aaa": "first",
              ...
              "zzz": "last"
            }
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should pass with ELLIPSIS matching
    result.assert_outcomes(passed=1)


def test_bash_example_mismatch_fails(pytester):
    """Bash example with wrong expected output should fail."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "actual"
            expected
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should fail
    result.assert_outcomes(failed=1)
    # Should show helpful error message
    result.stdout.fnmatch_lines(["*FAILED*DEMO.md*"])


def test_multiple_bash_examples(pytester):
    """Multiple bash examples in same file should all be tested."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            # Example 1

            ```bash
            $ echo "first"
            first
            ```

            # Example 2

            ```bash
            $ echo "second"
            second
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Both should pass
    result.assert_outcomes(passed=2)


def test_environment_variables_passed_to_commands(pytester):
    """Environment variables from bashdoctest_env fixture should be available in commands."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "$TEST_VAR"
            hello_from_fixture
            ```
            """
        ),
    )

    # User provides bashdoctest_env fixture with custom values
    pytester.makeconftest(
        """
        import pytest

        @pytest.fixture(scope="session")
        def bashdoctest_env():
            return {"TEST_VAR": "hello_from_fixture"}
        """
    )

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should pass with env var substitution
    result.assert_outcomes(passed=1)


def test_multiline_command_with_backslash(pytester):
    """Multi-line commands with backslash continuations should work."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            r"""
            ```bash
            $ echo "line1" \
              "line2" \
              "line3"
            line1 line2 line3
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should pass
    result.assert_outcomes(passed=1)


def test_string_level_ellipsis_in_urls(pytester):
    """String-level ELLIPSIS should work for partial URL matching."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo '{"url": "https://example.com/path/to/file.pdf"}' | jq -S
            {
              "url": "https://.../file.pdf"
            }
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should pass with string-level ELLIPSIS
    result.assert_outcomes(passed=1)


def test_collects_markdown_files_explicitly(pytester):
    """Plugin collects markdown files when explicitly specified."""
    # Create two markdown files
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "demo"
            demo
            ```
            """
        ),
    )

    pytester.makefile(
        ".md",
        README=textwrap.dedent(
            """
            ```bash
            $ echo "readme"
            readme
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    # Test explicit file collection
    result = pytester.runpytest("--bashdoctest", "DEMO.md", "-v")
    result.assert_outcomes(passed=1)
    result.stdout.fnmatch_lines(["*DEMO.md*"])

    # Test that README.md can also be collected when specified
    result = pytester.runpytest("--bashdoctest", "README.md", "-v")
    result.assert_outcomes(passed=1)
    result.stdout.fnmatch_lines(["*README.md*"])


def test_collects_markdown_via_testpaths_config(pytester):
    """Plugin collects markdown files via testpaths configuration."""
    # Create a markdown file
    pytester.makefile(
        ".md",
        API=textwrap.dedent(
            """
            ```bash
            $ echo "api docs"
            api docs
            ```
            """
        ),
    )

    # Create pyproject.toml with testpaths configuration
    pytester.makepyprojecttoml(
        """
        [tool.pytest.ini_options]
        testpaths = ["API.md"]
        """
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    # Run pytest without path arguments - should use testpaths
    # But still need --bashdoctest flag!
    result = pytester.runpytest("--bashdoctest", "-v")
    result.assert_outcomes(passed=1)
    result.stdout.fnmatch_lines(["*API.md*"])


def test_multiple_commands_share_environment(pytester):
    """Multiple $ commands should execute in sequence with shared environment."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ export TEST_VAR="hello"
            $ export TEST_VAR2="world"
            $ echo "$TEST_VAR $TEST_VAR2"
            hello world
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")
    result.assert_outcomes(passed=1)


def test_failure_message_shows_command_and_output(pytester):
    """Failed tests should show helpful error messages with command and output."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo "actual_output"
            expected_output
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should fail with descriptive message
    result.assert_outcomes(failed=1)
    result.stdout.fnmatch_lines(
        [
            "*FAILED*",
            "*Command:*",
            '*echo "actual_output"*',
            "*Expected segment not found:*",
            "*expected_output*",
            "*Full actual output:*",
            "*actual_output*",
        ]
    )


def test_object_and_array_ellipsis_in_json(pytester):
    """Test {...} and [...] patterns match JSON collections on single lines."""
    pytester.makefile(
        ".md",
        DEMO=textwrap.dedent(
            """
            ```bash
            $ echo '"meta": {"created": "2025-01-01", "author": "test"}, "items": ["a", "b"]'
            "meta": {...}, "items": [...]
            ```
            """
        ),
    )

    # Default bashdoctest_env fixture (empty) is provided by plugin

    result = pytester.runpytest("--bashdoctest", "-v")

    # Should pass with collection ELLIPSIS
    result.assert_outcomes(passed=1)
