"""Pytest plugin for testing bash examples in markdown documentation.

This is the ONLY module in pytest_bashdoctest that imports pytest.
All other modules (parser, matcher, executor, formatter) are pure Python
for maximum extractability.
"""

from pathlib import Path

import pytest

from pytest_bashdoctest.executor import execute_command
from pytest_bashdoctest.formatter import format_failure
from pytest_bashdoctest.matcher import match_output
from pytest_bashdoctest.parser import BashExample, extract_bash_examples


def pytest_addoption(parser):
    """Add command-line options for bash doctest plugin."""
    group = parser.getgroup("bashdoctest")
    group.addoption(
        "--bashdoctest",
        action="store_true",
        default=False,
        help="Enable bash doctest collection from markdown files",
    )


@pytest.fixture(scope="session")
def bashdoctest_env():
    """Default environment for bash examples.

    Returns empty dict - commands inherit os.environ by default.
    Users can override this fixture in conftest.py to provide custom
    environment variables for bash examples.

    Example:
        # In conftest.py
        @pytest.fixture(scope="session")
        def bashdoctest_env():
            return {
                "API_KEY": "test-key-12345",
                "API_URL": "https://test.api.com"
            }
    """
    return {}


def pytest_runtest_setup(item):
    """Setup hook to inject bashdoctest_env fixture into BashDocItem.

    This is called before runtest() for each item. For BashDocItem instances,
    we get the bashdoctest_env fixture value and store it on the item.

    Note: We call the fixture function directly for simplicity. This works
    because the fixture is session-scoped with no dependencies. When multiple
    fixtures with the same name exist, we take the last one (highest priority),
    which allows conftest.py to override the plugin's default.
    """
    if isinstance(item, BashDocItem):
        # Get the fixture definitions for bashdoctest_env
        fixturedefs = item.session._fixturemanager._arg2fixturedefs.get("bashdoctest_env")
        if fixturedefs:
            # Take the LAST one (highest priority - conftest.py overrides plugin)
            fixture_def = fixturedefs[-1]
            # Call the fixture function directly (works for simple session fixtures)
            env_fixture = fixture_def.func()
            item._bashdoctest_env = env_fixture
        else:
            item._bashdoctest_env = {}


class BashExampleFailedError(Exception):
    """Exception raised when a bash example fails to match expected output."""

    pass


class BashDocFile(pytest.File):
    """Pytest file collector for bash documentation files.

    Creates test items for each bash example found in markdown files.
    """

    def __init__(self, *args, examples=None, **kwargs):
        """Initialize with optional cached examples to avoid double-parsing."""
        super().__init__(*args, **kwargs)
        self._examples = examples

    def collect(self):
        """Extract bash examples and create test items."""
        # Use cached examples if available (from pytest_collect_file)
        if self._examples is None:
            self._examples = extract_bash_examples(Path(self.path))

        for i, example in enumerate(self._examples):
            yield BashDocItem.from_parent(
                self,
                name=f"line_{example.line_number}",
                example=example,
            )


class BashDocItem(pytest.Item):
    """Individual bash example test item.

    Executes the command, matches output against expected, and reports failures.
    """

    def __init__(self, name, parent, example: BashExample):
        super().__init__(name, parent)
        self.example = example
        self._bashdoctest_env = None  # Set by pytest_runtest_setup hook

    def runtest(self):
        """Execute test: run command, match output."""
        # Get environment additions (set by pytest_runtest_setup hook)
        env_additions = self._bashdoctest_env or {}

        # Execute command (executor merges env with os.environ)
        result = execute_command(self.example.command, env_additions)

        # Check exit code
        if result.returncode != 0:
            raise BashExampleFailedError(
                f"Command failed with exit code {result.returncode}\n" f"stderr: {result.stderr}"
            )

        # Match output
        actual_lines = result.stdout.split("\n")
        match_result = match_output(self.example.expected_output, actual_lines)

        if not match_result.success:
            raise BashExampleFailedError(format_failure(self.example, result, match_result))

    def repr_failure(self, excinfo):
        """Custom failure representation."""
        if isinstance(excinfo.value, BashExampleFailedError):
            return str(excinfo.value)
        return super().repr_failure(excinfo)

    def reportinfo(self):
        """Return representation of test location."""
        return (
            self.path,
            self.example.line_number,
            f"bash example at line {self.example.line_number}",
        )


def pytest_collect_file(parent, file_path: Path) -> BashDocFile | None:
    """Pytest hook to collect markdown files with bash examples.

    Only collects markdown files when:
    1. --bashdoctest flag is provided
    2. File actually contains bash code blocks

    This prevents conflicts with other markdown testing plugins and
    avoids claiming files that don't have bash examples.

    Args:
        parent: The parent collector
        file_path: Path to the file being considered

    Returns:
        BashDocFile if this is a markdown file with bash examples, None otherwise
    """
    # Must have --bashdoctest flag
    if not parent.config.getoption("--bashdoctest", default=False):
        return None

    # Only collect markdown files
    if file_path.suffix != ".md":
        return None

    # Parse file and check if it has bash examples
    examples = extract_bash_examples(file_path)
    if not examples:
        return None

    # Create collector with cached examples (avoid double-parsing)
    return BashDocFile.from_parent(parent, path=file_path, examples=examples)
