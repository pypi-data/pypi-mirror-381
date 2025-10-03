"""Pytest plugin for testing bash examples in markdown documentation.

Provides three-level ELLIPSIS matching:
- Line-level: ... on its own line skips blocks
- String-level: ... inside strings matches partial content
- Collection-level: {...} and [...] match entire objects/arrays

Usage:
    # In pytest conftest.py
    pytest_plugins = ["pytest_bashdoctest.plugin"]

    # In your markdown file
    ```bash
    $ curl ... | jq -S
    {
      "field": "value",
      "nested": {...},
      ...
    }
    ```

    # Run tests
    $ pytest README.md
"""

from pytest_bashdoctest.executor import CommandResult, execute_command
from pytest_bashdoctest.formatter import format_failure
from pytest_bashdoctest.matcher import MatchResult, match_line, match_output
from pytest_bashdoctest.parser import BashExample, extract_bash_examples, parse_bash_example

__version__ = "0.1.0"
__all__ = [
    "extract_bash_examples",
    "parse_bash_example",
    "BashExample",
    "match_output",
    "match_line",
    "MatchResult",
    "execute_command",
    "CommandResult",
    "format_failure",
]
