"""Common library code for repo_structure."""

import os
import re
from dataclasses import dataclass, field
from os import DirEntry
from typing import Callable, Final, Literal

BUILTIN_DIRECTORY_RULES: Final = ["ignore"]


class ConfigurationParseError(Exception):
    """Raised when the configuration file is invalid."""


class StructureRuleError(Exception):
    """Raised when the structure rules are invalid."""


class TemplateError(Exception):
    """Raised when a template is invalid."""


@dataclass
class RepoEntry:
    """Wrapper for entries in the directory structure, that store the path
    as a string together with the entry type."""

    path: re.Pattern
    is_dir: bool
    is_required: bool
    is_forbidden: bool
    use_rule: str = ""
    if_exists: list["RepoEntry"] = field(default_factory=list)
    count: int = 0


@dataclass
class Entry:
    """Internal representation of a directory entry."""

    path: str
    rel_dir: str
    is_dir: bool
    is_symlink: bool


@dataclass
class Flags:
    """Flags for common parsing config settings."""

    follow_symlinks: bool = False
    include_hidden: bool = True
    verbose: bool = False


DirectoryMap = dict[str, list[str]]
StructureRuleList = list[RepoEntry]
StructureRuleMap = dict[str, StructureRuleList]


def normalize_path(path: str) -> str:
    """Normalize path separators for cross-platform compatibility.

    Converts all path separators to forward slashes for consistent
    internal representation across Windows, macOS, and Linux.
    """
    return path.replace(os.sep, "/") if path else path


def join_path_normalized(*parts: str) -> str:
    """Join path parts and normalize separators for cross-platform compatibility.

    Equivalent to os.path.join but ensures forward slashes in the result.
    """
    if not parts:
        return ""
    joined = os.path.join(*parts)
    return normalize_path(joined)


def rel_dir_to_map_dir(rel_dir: str):
    """Convert a relative directory path to a mapped directory path.

    This function ensures that a given relative directory path conforms to
    a specific format required for mapping. It enforces that the path starts
    and ends with a '/' character.
    """
    if not rel_dir or rel_dir == "/":
        return "/"

    if not rel_dir.startswith("/"):
        rel_dir = "/" + rel_dir
    if not rel_dir.endswith("/"):
        rel_dir = rel_dir + "/"

    return rel_dir


def map_dir_to_rel_dir(map_dir: str) -> str:
    """Convert a mapped directory path to a relative directory path.

    This function takes a mapped directory path and converts it back to
    a relative directory path by removing the leading and trailing '/'
    characters if they exist. If the input is the root directory or empty,
    it returns an empty string.
    """
    if not map_dir or map_dir == "/":
        return ""

    return map_dir[1:-1]


def skip_entry(
    entry: Entry,
    directory_map: DirectoryMap,
    config_file_name: str,
    git_ignore: Callable[[str], bool] | None = None,
    flags: Flags = Flags(),
) -> bool:
    """Return True if the entry should be skipped/ignored."""
    skip_conditions = [
        (not flags.follow_symlinks and entry.is_symlink),
        (not flags.include_hidden and entry.path.startswith(".")),
        (entry.path == ".gitignore" and not entry.is_dir),
        (entry.path == ".git" and entry.is_dir),
        (git_ignore and git_ignore(entry.path)),
        (
            entry.is_dir
            and rel_dir_to_map_dir(join_path_normalized(entry.rel_dir, entry.path))
            in directory_map
        ),
        (entry.path == config_file_name),
    ]

    for condition in skip_conditions:
        if condition:
            if flags.verbose:
                print(f"Skipping {entry.path}")
            return True

    return False


def to_entry(os_entry: DirEntry[str], rel_dir: str) -> Entry:
    """Convert an os.DirEntry to an internal Entry representation."""
    return Entry(
        path=os_entry.name,
        rel_dir=rel_dir,
        is_dir=os_entry.is_dir(),
        is_symlink=os_entry.is_symlink(),
    )


def expand_use_rule(
    use_rule: str,
    structure_rules: StructureRuleMap,
    flags: Flags,
    rel_path: str,
):
    """Expand the use_rule into a list of RepoEntry items."""
    if use_rule:
        if flags.verbose:
            print(f"use_rule found for rel path '{rel_path}'")
        return _build_active_entry_backlog(
            [use_rule],
            structure_rules,
        )
    return None


def expand_if_exists(backlog_entry: RepoEntry, flags: Flags):
    """Expand to the entry in `if_exists` or None."""
    if backlog_entry.if_exists:
        if flags.verbose:
            print(f"if_exists found for rel path '{backlog_entry.path.pattern}'")
        return backlog_entry.if_exists
    # the following line can not be reached given a directory entry must be
    # either `use_rule`, or `if_exists`
    return None  # pragma: no cover


def map_dir_to_entry_backlog(
    directory_map: DirectoryMap,
    structure_rules: StructureRuleMap,
    map_dir: str,
) -> StructureRuleList:
    """Get the active entry backlog for a given mapped directory."""

    def _get_use_rules_for_directory(
        directory_map: DirectoryMap, directory: str
    ) -> list[str]:
        d = rel_dir_to_map_dir(directory)
        return directory_map[d]

    use_rules = _get_use_rules_for_directory(directory_map, map_dir)
    return _build_active_entry_backlog(use_rules, structure_rules)


def _build_active_entry_backlog(
    active_use_rules: list[str], structure_rules: StructureRuleMap
) -> StructureRuleList:
    result: StructureRuleList = []
    for rule in active_use_rules:
        if rule == "ignore":
            continue
        result += structure_rules[rule]
    return result


@dataclass
class ScanIssue:
    """Represents a single finding from a scan.

    severity: "error" or "warning"
    code: short machine-consumable code (e.g., "unused_structure_rule")
    message: human-readable description
    path: optional path context for the issue
    """

    severity: Literal["error", "warning"]
    code: str
    message: str
    path: str | None = None


@dataclass
class MatchResult:
    """Result of attempting to match an entry against backlog rules."""

    success: bool
    index: int | None = None
    issue: ScanIssue | None = None


def get_matching_item_index(
    backlog: StructureRuleList,
    entry_path: str,
    is_dir: bool,
    verbose: bool = False,
) -> MatchResult:
    """Get matching item index without raising exceptions, return result with potential issues."""
    for i, v in enumerate(backlog):
        if v.path.fullmatch(entry_path) and v.is_dir == is_dir:
            if v.is_forbidden:
                return MatchResult(
                    success=False,
                    issue=ScanIssue(
                        severity="error",
                        code="forbidden_entry",
                        message=f"Found forbidden entry: {entry_path}",
                        path=entry_path,
                    ),
                )
            if verbose:
                print(f"  Found match at index {i}: '{v.path.pattern}'")
            return MatchResult(success=True, index=i)

    display_path = entry_path + "/" if is_dir else entry_path
    return MatchResult(
        success=False,
        issue=ScanIssue(
            severity="error",
            code="unspecified_entry",
            message=f"Found unspecified entry: '{display_path}'",
            path=entry_path,
        ),
    )
