"""Execute bash commands with environment variables."""

import os
import subprocess
from dataclasses import dataclass


@dataclass
class CommandResult:
    """Result of command execution.

    Attributes:
        stdout: Standard output from command
        stderr: Standard error from command
        returncode: Exit code from command
        command: The command that was executed
    """

    stdout: str
    stderr: str
    returncode: int
    command: str


def execute_command(command: str, env: dict[str, str]) -> CommandResult:
    """Execute bash command with environment variables.

    Algorithm:
    1. Merge env dict with os.environ
    2. Run command via subprocess.run()
    3. Capture stdout/stderr
    4. Return CommandResult

    Environment variables:
    - API_KEY: From pytest fixture
    - API_URL: From pytest fixture or default

    Security:
    - Commands are from trusted source (your documentation)
    - Shell=True is safe because commands come from your own markdown files

    Args:
        command: The bash command to execute
        env: Environment variables to merge with os.environ

    Returns:
        CommandResult with stdout, stderr, and returncode
    """
    full_env = {**os.environ, **env}

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        env=full_env,
        timeout=30,  # Prevent hanging
    )

    return CommandResult(
        stdout=result.stdout,
        stderr=result.stderr,
        returncode=result.returncode,
        command=command,
    )
