#!/usr/bin/env python3
"""Keep the profile's project version labels aligned with application source.

Version 1.0.0
"""
from __future__ import annotations

import argparse
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote

VERSION = "1.0.0"
OWNER = "HaytamElbouhmidi"
PROJECTS = {
    "Gmail Unsubscriber": ("gmail-unsubscriber", "gmail_unsubscriber.py", "python"),
    "ROG Slash Battery Gauge": ("rog-slash-battery-gauge", "slash-battery.py", "python"),
    "AeroDrive": ("AeroDrive", "app/build.gradle.kts", "android"),
}


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


def replace_version_labels(source: str, versions: dict[str, str]) -> str:
    lines = source.splitlines(keepends=True)
    in_section = ""
    table_updates = {name: 0 for name in PROJECTS}
    badge_updates = {name: 0 for name in PROJECTS}
    for index, line in enumerate(lines):
        if line.startswith("## "):
            in_section = line.strip()[3:]
        if line.startswith("| **[") and "[Source ZIP]" in line:
            cells = line.split("|")
            for name in PROJECTS:
                if f"**[{name}](" in cells[1]:
                    if len(cells) < 8:
                        raise ValueError(f"Invalid project overview row for {name}")
                    cells[5] = f" `{versions[name]}` "
                    lines[index] = "|".join(cells)
                    table_updates[name] += 1
        if line.startswith("### "):
            heading = line[4:].strip()
            if heading == "Gmail Unsubscriber for Linux":
                heading = "Gmail Unsubscriber"
            if heading in PROJECTS:
                in_section = heading
        if line.startswith("![Version]") or line.startswith("![Development version]"):
            if in_section in PROJECTS:
                end = "\n" if line.endswith("\n") else ""
                lines[index] = badge(versions[in_section], development=(in_section == "AeroDrive")) + end
                badge_updates[in_section] += 1

    for name in PROJECTS:
        required_badges = 2 if name == "Gmail Unsubscriber" else 1
        if table_updates[name] != 1 or badge_updates[name] != required_badges:
            raise ValueError(f"Could not locate exact version labels for {name}: "
                             f"table={table_updates[name]}, badges={badge_updates[name]}")
    return "".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize my GitHub profile project versions")
    parser.add_argument("--readme", type=Path, default=Path(__file__).resolve().parents[1] / "README.md")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    versions = {name: declared_version(read_remote(repo, path), kind)
                for name, (repo, path, kind) in PROJECTS.items()}
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
