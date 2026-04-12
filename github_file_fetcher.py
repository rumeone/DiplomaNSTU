"""Fetch file contents from GitHub at a specific commit (base_commit).

Used to provide the LLM with the EXACT source code it needs to patch,
so that generated diff hunk line numbers are correct.
"""
from __future__ import annotations

import re
import urllib.request
from typing import Optional


def fetch_file_at_commit(
    repo: str,
    filepath: str,
    commit: str,
    timeout: int = 15,
) -> Optional[str]:
    """
    Fetch raw content of a file from GitHub at a specific commit.

    Parameters
    ----------
    repo : str
        GitHub repo in format "owner/repo" (e.g. "astropy/astropy").
    filepath : str
        Path to file inside the repo (e.g. "astropy/modeling/separable.py").
    commit : str
        Full or short commit SHA.
    timeout : int
        HTTP timeout in seconds.

    Returns
    -------
    str or None
        File content as string, or None if fetch failed.
    """
    url = f"https://raw.githubusercontent.com/{repo}/{commit}/{filepath}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "swebench-diploma"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception:
        return None


def extract_files_from_patch(patch: str) -> list[str]:
    """
    Extract list of file paths touched by a ground-truth patch.
    Parses lines like: `--- a/path/to/file.py`
    """
    files: list[str] = []
    for line in patch.splitlines():
        m = re.match(r'^---\s+a/(.+)', line)
        if m:
            path = m.group(1).strip()
            if path not in files:
                files.append(path)
    return files


def fetch_task_file_contents(
    repo: str,
    base_commit: str,
    patch: Optional[str],
    max_files: int = 3,
    max_file_lines: int = 500,
) -> dict[str, str]:
    """
    Fetch the actual source code of files that need to be changed.

    Uses the ground-truth patch to identify which files to fetch,
    then retrieves each file at base_commit from GitHub.

    Parameters
    ----------
    repo : str
        GitHub repo (e.g. "astropy/astropy").
    base_commit : str
        Commit SHA at which the issue exists.
    patch : str or None
        Ground-truth patch (used only to identify file paths, not leaked to model).
    max_files : int
        Maximum number of files to fetch.
    max_file_lines : int
        Truncate files longer than this to avoid exceeding context window.

    Returns
    -------
    dict[str, str]
        {filepath: content} for each successfully fetched file.
    """
    if not patch or not base_commit:
        return {}

    filepaths = extract_files_from_patch(patch)[:max_files]
    result: dict[str, str] = {}

    for filepath in filepaths:
        content = fetch_file_at_commit(repo, filepath, base_commit)
        if content is None:
            continue
        lines = content.splitlines()
        if len(lines) > max_file_lines:
            content = "\n".join(lines[:max_file_lines])
            content += f"\n... (truncated at {max_file_lines} lines)"
        result[filepath] = content

    return result
