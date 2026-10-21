"""Regression checks for profile version synchronization.

Version 1.0.0
"""
import unittest

from sync_project_versions import PROJECTS, badge, declared_version, replace_version_labels


def profile_fixture() -> str:
    return """## PC

### [Gmail Unsubscriber](https://github.com/HaytamElbouhmidi/gmail-unsubscriber)
![Version](https://img.shields.io/badge/VERSION-3.1.3-123447?style=flat-square)

### [Flat File Collector](https://github.com/HaytamElbouhmidi/flat-file-collector)
![Version](https://img.shields.io/badge/VERSION-1.0.0-123447?style=flat-square)

### [ROG Slash Battery Gauge](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge)
![Version](https://img.shields.io/badge/VERSION-UNVERSIONED-929292?style=flat-square)

## Mobile

### [AeroDrive](https://github.com/HaytamElbouhmidi/AeroDrive)
![Version](https://img.shields.io/badge/VERSION-0.2.1--dev-123447?style=flat-square)

## Version numbering

| Active development or prerelease build | **DEV** | `0.2.1-dev` |
"""


class ProfileVersionSyncTests(unittest.TestCase):
    def test_current_profile_layout(self) -> None:
        versions = {
            "Gmail Unsubscriber": "3.2.0",
            "Flat File Collector": "1.0.1",
            "ROG Slash Battery Gauge": "Unversioned",
            "AeroDrive": "0.2.2-dev",
        }
        result = replace_version_labels(profile_fixture(), versions)
        for version in versions.values():
            self.assertIn(badge(version, development=version.endswith("-dev")), result)
        self.assertIn("| Active development or prerelease build | **DEV** | `0.2.1-dev` |", result)
        self.assertEqual(replace_version_labels(result, versions), result)

    def test_missing_badge_fails(self) -> None:
        fixture = profile_fixture().replace(
            "![Version](https://img.shields.io/badge/VERSION-1.0.0-123447?style=flat-square)",
            "",
        )
        with self.assertRaisesRegex(ValueError, "Flat File Collector, found 0"):
            replace_version_labels(fixture, {"Flat File Collector": "1.0.1"})

    def test_duplicate_badge_fails(self) -> None:
        fixture = profile_fixture().replace(
            "![Version](https://img.shields.io/badge/VERSION-3.1.3-123447?style=flat-square)",
            "![Version](https://img.shields.io/badge/VERSION-3.1.3-123447?style=flat-square)\n"
            "![Version](https://img.shields.io/badge/VERSION-3.1.3-123447?style=flat-square)",
        )
        with self.assertRaisesRegex(ValueError, "Gmail Unsubscriber, found 2"):
            replace_version_labels(fixture, {"Gmail Unsubscriber": "3.2.0"})

    def test_declared_versions(self) -> None:
        self.assertEqual(declared_version('__version__ = "1.2.3"', "python"), "1.2.3")
        self.assertEqual(declared_version('        versionName = "0.2.1-dev"', "android"), "0.2.1-dev")
        self.assertEqual(declared_version('print("hello")', "python"), "Unversioned")
        self.assertEqual(len(PROJECTS), 4)


if __name__ == "__main__":
    unittest.main()
