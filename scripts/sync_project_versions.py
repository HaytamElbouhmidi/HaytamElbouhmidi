#!/usr/bin/env python3
"""Keep the profile's project version labels aligned with application source.

Version 1.1.1
"""
from __future__ import annotations

import argparse
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote

VERSION = "1.1.1"
OWNER = "HaytamElbouhmidi"
PROJECTS = {
    "Gmail Unsubscriber": ("gmail-unsubscriber", "gmail_unsubscriber.py", "python"),
    "Flat File Collector": ("flat-file-collector", "flatten_files.py", "python"),
    "ROG Slash Battery Gauge": ("rog-slash-battery-gauge", "slash-battery.py", "python"),
    "AeroDrive": ("AeroDrive", "app/build.gradle.kts", "android"),
}

VERSION_BADGE = re.compile(
    r"^!\[(?:Version|Development version)\]"
    r"\(https://img\.shields\.io/badge/VERSION-[^)]+\)$"
)


def read_remote(repo: str, path: str) -> str:
    url = f"https://raw.githubusercontent.com/{OWNER}/{repo}/main/{path}"
    request = urllib.request.Request(url, headers={"User-Agent": f"github-profile-version-sync/{VERSION}"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read(2 * 1024 * 1024).decode("utf-8")


def declared_version(source: str, kind: str) -> str:
    if kind == "android":
        pattern = r'^\s*versionName\s*=\s*["\']([^"\']+)["\']'
    else:
        pattern = r'^(?:APP_VERSION|VERSION|__version__)\s*=\s*["\']([^"\']+)["\']'
    match = re.search(pattern, source, re.MULTILINE)
    value = match.group(1) if match else "Unversioned"
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,39}", value):
        raise ValueError(f"Invalid version string: {value!r}")
    return value


def badge(value: str, *, development: bool = False) -> str:
    encoded = quote(("UNVERSIONED" if value == "Unversioned" else value).replace("-", "--"), safe="._")
    color = "929292" if value == "Unversioned" else "123447"
    label = "Development version" if development else "Version"
    return (f"![{label}](https://img.shields.io/badge/"
            f"VERSION-{encoded}-{color}?style=flat-square)")


def project_from_heading(heading: str) -> str | None:
    match = re.fullmatch(
        rf"\[[^\]]+\]\(https://github\.com/{re.escape(OWNER)}/([^/)]+)\)",
        heading,
    )
    if match:
        repository = match.group(1).casefold()
        for name, (repo, _, _) in PROJECTS.items():
            if repo.casefold() == repository:
                return name
        return None
    if heading == "Gmail Unsubscriber for Linux":
        return "Gmail Unsubscriber"
    return heading if heading in PROJECTS else None


def replace_version_labels(source: str, versions: dict[str, str]) -> str:
    lines = source.splitlines(keepends=True)
    current_project = None
    badge_counts = {name: 0 for name in versions}

    for index, line in enumerate(lines):
        if line.startswith("## "):
            current_project = None
        elif line.startswith("### "):
            current_project = project_from_heading(line[4:].strip())

        if current_project not in versions or not VERSION_BADGE.fullmatch(line.strip()):
            continue

        version = versions[current_project]
        ending = "\n" if line.endswith("\n") else ""
        lines[index] = badge(version, development=version.endswith("-dev")) + ending
        badge_counts[current_project] += 1

    for name, count in badge_counts.items():
        if count != 1:
            raise ValueError(f"Expected one version badge for {name}, found {count}. "
                             "Check the profile project heading and version badge.")
    return "".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize my GitHub profile project versions")
    parser.add_argument("--readme", type=Path, default=Path(__file__).resolve().parents[1] / "README.md")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--gmail-version", help="Use a verified local Gmail Unsubscriber version")
    args = parser.parse_args()
    versions = ({"Gmail Unsubscriber": args.gmail_version} if args.gmail_version else
                {name: declared_version(read_remote(repo, path), kind)
                 for name, (repo, path, kind) in PROJECTS.items()})
    for value in versions.values():
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,39}", value):
            raise ValueError(f"Invalid application version: {value!r}")
    original = args.readme.read_text(encoding="utf-8")
    updated = replace_version_labels(original, versions)
    print("Source versions: " + ", ".join(f"{name}={version}" for name, version in versions.items()))
    if updated != original:
        if not args.dry_run:
            args.readme.write_text(updated, encoding="utf-8")
        print("Profile README has version changes." if not args.dry_run else "Profile README needs an update.")
    else:
        print("Profile README version labels already match the applications.")


if __name__ == "__main__":
    main()
