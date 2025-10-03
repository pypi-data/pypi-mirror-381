"""Extract bash examples from markdown files.

This module parses markdown files to find bash code blocks and extract
commands and expected output for testing.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class BashExample:
    """Represents a single bash example from markdown.

    Attributes:
        line_number: Line number in markdown where the code block starts
        command: Full command to execute (joined if multi-line)
        expected_output: List of expected output lines
        code_block: Original code block content for debugging
    """

    line_number: int
    command: str
    expected_output: list[str]
    code_block: str


def extract_bash_examples(markdown_path: Path) -> list[BashExample]:
    """Extract all bash code blocks from markdown file.

    Looks for code blocks marked as ```bash or ```shell.
    Tracks line numbers for error reporting.

    Args:
        markdown_path: Path to markdown file

    Returns:
        List of BashExample objects
    """
    content = markdown_path.read_text()
    lines = content.split("\n")

    examples = []
    in_code_block = False
    code_block_lines = []
    code_block_start_line = 0
    code_block_type = None

    for line_num, line in enumerate(lines, start=1):
        # Check for code block start
        if line.strip().startswith("```bash") or line.strip().startswith("```shell"):
            in_code_block = True
            code_block_start_line = line_num
            code_block_type = "bash"
            code_block_lines = []
            continue

        # Check for code block end
        if in_code_block and line.strip() == "```":
            in_code_block = False
            if code_block_type == "bash" and code_block_lines:
                code_block = "\n".join(code_block_lines)
                example = parse_bash_example(code_block, code_block_start_line)
                if example:  # Skip blocks without $ commands
                    examples.append(example)
            code_block_lines = []
            code_block_type = None
            continue

        # Collect lines within code block
        if in_code_block:
            code_block_lines.append(line)

    return examples


def parse_bash_example(code_block: str, line_number: int) -> BashExample | None:
    """Parse single bash code block into command + expected output.

    Algorithm:
    1. Split by lines
    2. Lines starting with '$ ' are commands
    3. Join multi-line commands (ending with \\)
    4. Everything else is expected output

    Args:
        code_block: The code block content
        line_number: Line number for error reporting

    Returns:
        BashExample object, or None if no $ commands found
    """
    lines = code_block.split("\n")

    command_groups = []  # List of command groups (each group is one $ command)
    current_group = []
    output_lines = []
    in_command = False

    for line in lines:
        # Start of command
        if line.startswith("$ "):
            # Save previous command group if any
            if current_group:
                command_groups.append(current_group)
                current_group = []

            in_command = True
            command_line = line[2:]  # Strip '$ '

            # Handle continuation
            if command_line.rstrip().endswith("\\"):
                current_group.append(command_line.rstrip()[:-1].strip())
            else:
                current_group.append(command_line)
                command_groups.append(current_group)
                current_group = []
                # Command complete, switch to output mode
                in_command = False

        # Continuation of multi-line command
        elif in_command and line.rstrip().endswith("\\"):
            current_group.append(line.rstrip()[:-1].strip())

        # End of multi-line command
        elif in_command:
            current_group.append(line.strip())
            command_groups.append(current_group)
            current_group = []
            in_command = False

        # Output line
        else:
            output_lines.append(line)

    # Skip blocks without $ commands
    if not command_groups:
        return None

    # Join parts within each group with spaces, then join groups with semicolons
    commands = [" ".join(group) for group in command_groups]
    command = " ; ".join(commands)

    # Remove trailing empty lines from output
    while output_lines and not output_lines[-1].strip():
        output_lines.pop()

    return BashExample(
        line_number=line_number,
        command=command,
        expected_output=output_lines,
        code_block=code_block,
    )
