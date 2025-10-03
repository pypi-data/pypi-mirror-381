"""Tests for bash example parser module."""

from pathlib import Path

from pytest_bashdoctest.parser import extract_bash_examples, parse_bash_example


def test_extract_single_bash_block(tmp_path):
    """Test extracting one bash code block."""
    md_file = tmp_path / "test.md"
    md_file.write_text(
        """
# Example

```bash
$ echo "hello"
hello
```
"""
    )

    examples = extract_bash_examples(md_file)
    assert len(examples) == 1
    assert examples[0].command == 'echo "hello"'
    assert examples[0].expected_output == ["hello"]


def test_extract_multiple_bash_blocks(tmp_path):
    """Test extracting multiple bash code blocks."""
    md_file = tmp_path / "test.md"
    md_file.write_text(
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
    )

    examples = extract_bash_examples(md_file)
    assert len(examples) == 2
    assert examples[0].command == 'echo "first"'
    assert examples[1].command == 'echo "second"'


def test_extract_shell_block(tmp_path):
    """Test extracting ```shell blocks (synonym for bash)."""
    md_file = tmp_path / "test.md"
    md_file.write_text(
        """
```shell
$ echo "test"
test
```
"""
    )

    examples = extract_bash_examples(md_file)
    assert len(examples) == 1
    assert examples[0].command == 'echo "test"'


def test_parse_multiline_command():
    """Test backslash continuation for multi-line commands."""
    code_block = """$ curl -s \\
  -H "header" \\
  "url"
output"""

    example = parse_bash_example(code_block, line_number=1)
    assert example.command == 'curl -s -H "header" "url"'
    assert example.expected_output == ["output"]


def test_parse_command_with_multiline_output():
    """Test command with multiple output lines."""
    code_block = """$ echo "line1"
line1
line2
line3"""

    example = parse_bash_example(code_block, line_number=1)
    assert example.command == 'echo "line1"'
    assert example.expected_output == ["line1", "line2", "line3"]


def test_parse_command_with_empty_output():
    """Test command with no output."""
    code_block = """$ command_with_no_output
"""

    example = parse_bash_example(code_block, line_number=1)
    assert example.command == "command_with_no_output"
    assert example.expected_output == []


def test_line_numbers_tracked():
    """Test that line numbers are correctly tracked for error reporting."""
    md_file = Path(__file__).parent / "fixtures" / "test_line_numbers.md"
    md_file.parent.mkdir(exist_ok=True)
    md_file.write_text(
        """Line 1
Line 2
Line 3
```bash
$ echo "test"
test
```
Line 8
"""
    )

    examples = extract_bash_examples(md_file)
    assert len(examples) == 1
    # Line 4 is where ```bash starts
    assert examples[0].line_number == 4

    # Cleanup
    md_file.unlink()


def test_ignore_non_bash_code_blocks(tmp_path):
    """Test that non-bash code blocks are ignored."""
    md_file = tmp_path / "test.md"
    md_file.write_text(
        """
```python
print("not bash")
```

```bash
$ echo "is bash"
is bash
```

```javascript
console.log("not bash");
```
"""
    )

    examples = extract_bash_examples(md_file)
    assert len(examples) == 1
    assert examples[0].command == 'echo "is bash"'


def test_complex_curl_jq_example():
    """Test realistic curl + jq example with pipes and JSON."""
    code_block = """$ curl -s \\
  -H "x-api-key: $API_KEY" \\
  "$API_URL/api/v1/users/USER-1234-5678" \\
  | jq -S
{
  "username": "johndoe",
  ...
  "user_id": "USER-1234-5678"
}"""

    example = parse_bash_example(code_block, line_number=1)
    expected_cmd = (
        'curl -s -H "x-api-key: $API_KEY" ' '"$API_URL/api/v1/users/USER-1234-5678" | jq -S'
    )
    assert example.command == expected_cmd
    assert "{" in example.expected_output[0]
    # Check for ellipsis anywhere in output
    assert any("..." in line for line in example.expected_output)
    assert "}" in example.expected_output[-1]


def test_bash_example_dataclass_fields():
    """Test that BashExample has expected fields."""
    code_block = """$ echo "test"
test"""

    example = parse_bash_example(code_block, line_number=42)

    assert hasattr(example, "line_number")
    assert hasattr(example, "command")
    assert hasattr(example, "expected_output")
    assert hasattr(example, "code_block")

    assert example.line_number == 42
    assert example.command == 'echo "test"'
    assert example.expected_output == ["test"]
    assert example.code_block == code_block
