from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Optional


def add_worktree(
    repo_root: Path,
    path: Path,
    *,
    branch: Optional[str],
    ref: Optional[str],
    use_existing_branch: bool = False,
) -> None:
    """Create a git worktree.

    If `use_existing_branch` is True and `branch` is provided, checks out the existing branch
    in the new worktree: `git worktree add <path> <branch>`.

    If `use_existing_branch` is False and `branch` is provided, creates a new branch:
    `git worktree add -b <branch> <path> <ref or HEAD>`.

    Otherwise, uses `git worktree add <path> <ref or HEAD>`.
    """

    if branch and use_existing_branch:
        # Check out an existing branch in the new worktree
        cmd = ["git", "worktree", "add", str(path), branch]
    elif branch:
        # Create a new branch in the new worktree
        base_ref = ref or "HEAD"
        cmd = [
            "git",
            "worktree",
            "add",
            "-b",
            branch,
            str(path),
            base_ref,
        ]
    else:
        base_ref = ref or "HEAD"
        cmd = ["git", "worktree", "add", str(path), base_ref]

    subprocess.run(cmd, cwd=repo_root, check=True)


def remove_worktree(repo_root: Path, path: Path, *, force: bool) -> None:
    """Remove a git worktree from the repository metadata.

    Runs `git worktree remove [--force] <path>`. This may fail if the worktree has
    uncommitted changes unless `force=True`.
    """

    cmd = ["git", "worktree", "remove"]
    if force:
        cmd.append("--force")
    cmd.append(str(path))
    subprocess.run(cmd, cwd=repo_root, check=True)


def get_current_branch(cwd: Path) -> str:
    """Get the name of the current branch.

    Raises subprocess.CalledProcessError if HEAD is detached or not in a git repo.
    """
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )
    branch = result.stdout.strip()
    if branch == "HEAD":
        raise ValueError("HEAD is detached (not on a branch)")
    return branch


def checkout_branch(repo_root: Path, branch: str) -> None:
    """Checkout a branch in the current worktree.

    Runs `git checkout <branch>`.
    """
    subprocess.run(["git", "checkout", branch], cwd=repo_root, check=True)
