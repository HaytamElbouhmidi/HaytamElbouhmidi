# Haytam Elbouhmidi

**Mechanical Engineer | Systems Integration | Software and Hardware Development**

I build software tools, instrumentation, and hardware integrations. This is my project directory. Each repository appears once, grouped by device type, with a description, operating-system compatibility, current version, validation status, and setup or download links.

## Browse projects

[![PC](https://img.shields.io/badge/PC-4%20PROJECTS-123447?style=for-the-badge)](#pc)
[![Mobile](https://img.shields.io/badge/MOBILE-1%20PROJECT-00843D?style=for-the-badge)](#mobile)

### Status key

![Working](https://img.shields.io/badge/WORKING-Tested%20on%20specified%20hardware-00843D?style=flat-square)
![Testing](https://img.shields.io/badge/TESTING-Validation%20in%20progress-C88A00?style=flat-square)
![Not working](https://img.shields.io/badge/NOT%20WORKING-Confirmed%20issue-B42318?style=flat-square)
![Unverified](https://img.shields.io/badge/UNVERIFIED-No%20test%20evidence-929292?style=flat-square)

Status describes test evidence rather than feature completeness. An OS badge indicates an intended platform, not a guarantee that every configuration has been tested.

---

## PC

Desktop utilities and laptop hardware integrations. Multi-OS projects are listed only once.

### [Gmail Unsubscriber](https://github.com/HaytamElbouhmidi/gmail-unsubscriber)

![Windows](https://img.shields.io/badge/WINDOWS-123447?style=flat-square&logo=windows11&logoColor=white)
![Linux](https://img.shields.io/badge/LINUX-00843D?style=flat-square&logo=linux&logoColor=white)
![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-3.1.3-123447?style=flat-square)

A lightweight desktop tool for finding mailing-list messages in Gmail and managing unsubscribe requests. It supports optional Inbox and Spam scans, automatic or manual unsubscribe actions, resumable scans, and searchable results.

**Operating systems:** Windows and Linux desktop  
**Requirements:** Python 3.10+, Tkinter, and a Google app password  
**Validation:** Offline tests are available. Live Gmail acceptance and native Windows operation still need verification.

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber/archive/refs/heads/main.zip)
[![Setup](https://img.shields.io/badge/INSTRUCTIONS-SETUP-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber#setup)

---

### [Flat File Collector](https://github.com/HaytamElbouhmidi/flat-file-collector)

![Windows](https://img.shields.io/badge/WINDOWS-123447?style=flat-square&logo=windows11&logoColor=white)
![Linux](https://img.shields.io/badge/LINUX-00843D?style=flat-square&logo=linux&logoColor=white)
![macOS](https://img.shields.io/badge/MACOS-UNVERIFIED-929292?style=flat-square&logo=apple&logoColor=white)
![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-1.0.0-123447?style=flat-square)

A Python utility that collects files from a selected folder, all subfolders, and nested ZIP archives into one directory. It handles duplicate filenames, includes a dry-run preview, and leaves the originals untouched.

**Operating systems:** Windows, Linux (including CachyOS), and macOS  
**Requirements:** Python 3.10+. Tkinter is optional for graphical folder selection  
**Validation:** Automated tests passed on Linux. Native Windows testing remains pending. macOS compatibility is intended but unverified.

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/flat-file-collector/archive/refs/heads/main.zip)
[![Usage](https://img.shields.io/badge/INSTRUCTIONS-USAGE-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/flat-file-collector#run)

---

### [ROG Slash Battery Gauge](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge)

![Linux](https://img.shields.io/badge/LINUX-00843D?style=flat-square&logo=linux&logoColor=white)
![Working](https://img.shields.io/badge/STATUS-WORKING%20ON%20TESTED%20HARDWARE-00843D?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-UNVERSIONED-929292?style=flat-square)

Turns the seven-segment Slash Lighting bar on a compatible ASUS ROG laptop into a battery gauge. Segments fill from bottom to top, brightness tracks battery charge, and a systemd service maintains the display.

**Operating system:** Linux, tested on CachyOS  
**Verified hardware:** ASUS ROG Zephyrus G16 GU605MY, USB HID `0b05:193b`  
**Requirements:** Python 3.10+, Linux `hidraw`, and systemd for background operation  
**Validation:** Working on the tested seven-segment controller. Other ROG hardware is not automatically supported.

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge/archive/refs/heads/main.zip)
[![Installation](https://img.shields.io/badge/INSTRUCTIONS-INSTALLATION-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge#installation)

---

### SmartTar

![Linux](https://img.shields.io/badge/LINUX-00843D?style=flat-square&logo=linux&logoColor=white)
![KDE Plasma](https://img.shields.io/badge/KDE%20PLASMA%20%2F%20DEsk-123447?style=flat-square)
![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-0.2.0-123447?style=flat-square)

A lightweight archive inspector and user-level installer for supported Linux applications distributed as `.tar.gz` or `.tgz` files. It uses native KDE dialogs, recognizes Android Studio bundles, and creates application launchers after confirmation. There is no background service or bundled runtime.

**Operating system:** Linux, targeting CachyOS with KDE Plasma and DEsk  
**Requirements:** Python 3.10+, KDialog, and xdg-utils  
**Validation:** Automated Linux archive and integration tests are included. Native CachyOS/KDE/DEsk and the downloaded Android Studio bundle still need laptop verification.  
**Repository:** Publication pending. The v0.2.0 laptop test build is in testing.

---

## Mobile

### [AeroDrive](https://github.com/HaytamElbouhmidi/AeroDrive)

![Android](https://img.shields.io/badge/ANDROID-167C80?style=flat-square&logo=android&logoColor=white)
![Android Auto](https://img.shields.io/badge/ANDROID%20AUTO-167C80?style=flat-square)
![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Development version](https://img.shields.io/badge/VERSION-0.2.1--dev-123447?style=flat-square)
![CI](https://github.com/HaytamElbouhmidi/AeroDrive/actions/workflows/ci.yml/badge.svg?branch=main)

An open-source Android and Android Auto driving-map prototype that uses MapLibre to display a map and simulated nearby aircraft. It includes an optional development bridge for OpenSky aircraft data. Routing, authorized live-data use, and ATC audio remain in development.

**Operating systems:** Android phone and Android Auto  
**Requirements:** See the repository's Android build and test instructions  
**Validation:** The [October 16, 2026 CI build](https://github.com/HaytamElbouhmidi/AeroDrive/actions/runs/38916734207) passed. Physical phone and Android Auto head-unit testing remains pending. No stable release has been published.

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/AeroDrive/archive/refs/heads/main.zip)
[![Build guide](https://img.shields.io/badge/INSTRUCTIONS-BUILD%20AND%20TEST-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/AeroDrive/blob/main/docs/first-build.md)
[![CI artifact](https://img.shields.io/badge/DEBUG%20APK-CI%20ARTIFACT-C88A00?style=flat-square)](https://github.com/HaytamElbouhmidi/AeroDrive/actions/runs/38916734207)

The debug APK is a test artifact, not a public app release. GitHub Actions artifacts may require sign-in and can expire.

---

## Download and version information

- **Source ZIP:** A snapshot of the current `main` branch, not a compiled installer.
- **Working:** Verified in the stated environment or on the stated hardware.
- **Testing:** Implementation exists, but important runtime or release validation remains.
- **Not working:** Reserved for a confirmed functional failure.
- **Unverified:** Insufficient evidence to make a working or broken claim.
- **Version:** A declared application version where available. `Unversioned` indicates no version has been assigned or published.

I update each project's source version, README, and this directory together when I release changes. Status labels reflect testing evidence. The AeroDrive CI badge updates automatically as its build workflow runs.

## Version numbering

| Change | Version increment | Example |
| :--- | :--- | :--- |
| Breaking change to an established public interface, configuration, or behavior | **MAJOR** | `3.1.3` → `4.0.0` |
| New backward-compatible feature or meaningful capability | **MINOR** | `3.1.3` → `3.2.0` |
| Backward-compatible bug fix, security fix, or reliability improvement | **PATCH** | `3.1.3` → `3.1.4` |
| Documentation, comments, metadata, or CI-only maintenance with no application change | **No version change** | `3.1.3` stays `3.1.3` |
| Active development or prerelease build | **DEV** | `0.2.1-dev` |
| Application has no declared version | **Unversioned** | `Unversioned` |

---

## Support

[![Ko-fi](https://img.shields.io/badge/KO--FI-SUPPORT%20MY%20WORK-00843D?style=flat-square)](https://ko-fi.com/haytamelbouhmidi)
[![Patreon](https://img.shields.io/badge/PATREON-SUPPORT%20MY%20WORK-202522?style=flat-square)](https://www.patreon.com/c/HaytamElbouhmidi)

Support is optional and does not unlock core features.
