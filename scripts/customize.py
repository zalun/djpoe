# scripts/customize.py
"""A Script for Rapid Django Project Initialization."""

import logging
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import click

from scripts.logger import logger


@dataclass
class ProjectConfig:
    """Project configuration."""

    project_name: str
    app_name: str
    author_name: str
    author_email: str
    git_repo: str

    def to_str(self: "ProjectConfig") -> str:
        """Return a string representation of the project configuration."""
        return (
            f"Project name: {self.project_name}\nApp name: {self.app_name}\nAuthor name: {self.author_name}\n"
            f"Author email: {self.author_email}\nGit repository: {self.git_repo}"
        )


def remove_git_repo() -> None:
    """Remove the git repository."""
    git_dir = Path(".git")
    if git_dir.is_dir():
        logger.debug("Removing git repository")
        shutil.rmtree(git_dir)


def rename_directories(app_name: str, debug: bool) -> None:
    """Rename the directory djpoe to the app name."""
    logger.debug("Renaming directory djpoe to %s", app_name)
    try:
        Path("djpoe/djpoe").rename(f"djpoe/{app_name}")
        Path("djpoe").rename(app_name)
    except FileNotFoundError as e:
        logger.error("Failed to rename directory: %s", e)
        if debug:
            raise

        sys.exit(1)


def replace_strings(
    project_name: str,
    app_name: str,
    author_name: str,
    author_email: str,
    debug: bool,
) -> None:
    """Replace strings in the specified files based on the project configuration."""
    logger.debug("Replacing strings in the specified files based on the project configuration.")

    # Dictionary mapping old strings to new values
    replace_dict: dict[str, str] = {
        "DJPoe": project_name,
        "djpoe": app_name,
        "Piotr Zalewa": author_name,
        "zaloon@gmail.com": author_email,
    }

    # Find files that contain specific strings and have certain extensions
    files_to_replace = find_files_with_strings(
        ".",
        [".venv", ".git", "scripts", ".mypy_cache", ".pytest_cache", "test_home.py"],
        ["djpoe", "piotr", "zaloon@gmail.com"],
        [".py", ".md", ".ini", ".yml", ".toml", ".yaml"],
        debug,
    )

    # Replace strings in each file
    for file_path in files_to_replace:
        if not file_path.exists():
            logger.warning("File not found: %s", file_path)
            continue

        try:
            content = file_path.read_text(encoding="utf-8")
            for old, new in replace_dict.items():
                content = content.replace(old, new)
            file_path.write_text(content, encoding="utf-8")
            logger.debug("Replaced strings in %s", file_path)
        except OSError as e:
            logger.error("Failed to replace strings in %s: %s", file_path, e)
            if debug:
                raise


def find_files_with_strings(
    directory: str,
    excludes: list[str],
    search_strings: list[str],
    extensions: list[str],
    debug: bool,
) -> list[Path]:
    """Find files with strings in the specified directory."""
    # Compile a regex pattern to search for the specified strings
    pattern = re.compile("|".join(map(re.escape, search_strings)), re.IGNORECASE)
    matching_files = []

    # Recursively search for files in the directory
    for file_path in Path(directory).rglob("*"):
        # Skip directories and files within directories that are in the exclude_dirs list
        if str(file_path).startswith(".github"):
            logger.debug("Skipping directory: %s", file_path)
        if any(exclude in file_path.parts for exclude in excludes):
            continue

        # Check if the file has the desired extension and contains the search pattern
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            try:
                content = file_path.read_text(encoding="utf-8")
                if pattern.search(content):
                    matching_files.append(file_path)
                    logger.debug("Found match in: %s", file_path)
            except OSError as e:
                logger.error("Failed to read %s: %s", file_path, e)
                if debug:
                    logger.exception("Detailed error information:")

    return matching_files


def run_git_command(command: list[str], debug: bool) -> str | None:
    """Run a git command and log the output."""
    logger.debug("> %s", " ".join(command).rstrip("\n"))
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        if result.stdout:
            logger.debug(result.stdout)
    except subprocess.CalledProcessError as e:
        logger.error("Failed to run git command: %s", e)
        if debug:
            raise


def initialize_repository(git_repo: str, debug: bool) -> None:
    """Initialize the git repository."""
    logger.debug("Initializing git repository: %s", git_repo)
    run_git_command(["git", "init"], debug)
    run_git_command(["git", "remote", "add", "origin", git_repo], debug)
    run_git_command(["git", "checkout", "-b", "main"], debug)
    run_git_command(["git", "add", "README.md"], debug)
    run_git_command(["git", "commit", "-m", "README file from DJPoe"], debug)
    run_git_command(["git", "checkout", "-b", "djpoe-init"], debug)
    run_git_command(["git", "add", "."], debug)
    run_git_command(["git", "commit", "-m", "Initial commit from DJPoe"], debug)


def push_to_repository(git_repo: str, debug: bool) -> None:
    """Push to the repository."""
    logger.debug("Pushing to the repository: %s", git_repo)
    run_git_command(["git", "checkout", "main"], debug)
    run_git_command(["git", "push", "-u", "origin", "main", "-f"], debug)
    run_git_command(["git", "checkout", "djpoe-init"], debug)
    run_git_command(["git", "push", "-u", "origin", "djpoe-init"], debug)


@click.command()
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.option("--default", is_flag=True, help="Do not ask for generated names")
@click.option("--yes", is_flag=True, help="Approve all prompts")
@click.option("--project-name", prompt="Enter project name", help="Name of the project")
@click.option("--author-name", prompt="Enter author name", help="Name of the author")
@click.option("--author-email", prompt="Enter author email", help="Email of the author")
@click.option("--git-repo", prompt="Enter git repository URL", help="URL of the git repository")
def customize_project(
    project_name: str, author_name: str, author_email: str, git_repo: str, debug: bool, default: bool, yes: bool
) -> None:
    """Customize the djpoe project and push to a new repository."""
    if debug:
        logger.setLevel(logging.DEBUG)

    # Generate a default app name from the project name
    app_name = re.sub(r"[^a-zA-Z0-9]+", "_", project_name).lower()
    if not default:
        app_name = click.prompt("Enter the main app name", type=str, default=app_name)

    # Create a project configuration object
    config = ProjectConfig(project_name, app_name, author_name, author_email, git_repo)

    logger.debug("Project configuration: %s", config)
    if not yes:
        click.confirm(
            f"\nYou requested to morph DJPoe into the following project:\n{config.to_str()}\nDo you want to proceed?",
            abort=True,
        )

    remove_git_repo()
    rename_directories(app_name, debug)
    replace_strings(project_name, app_name, author_name, author_email, debug)

    if not git_repo:
        print(f"\n{app_name}")
        return

    initialize_repository(git_repo, debug)
    if yes or click.confirm("Do you want to push the changes to the remote repository?"):
        push_to_repository(git_repo, debug)

    print(f"\n{app_name}")


if __name__ == "__main__":
    customize_project()  # pylint: disable=no-value-for-parameter
