# Haytam Elbouhmidi

**Mechanical Engineer | Systems Integration | Software and Hardware Development**

I build software tools, instrumentation, and hardware integrations. This README is my project directory, with operating-system filters, device platforms, development status, and source downloads in one place.

## Find software by operating system

[![Windows](https://img.shields.io/badge/WINDOWS-1%20PROJECT-123447?style=for-the-badge&logo=windows11&logoColor=white)](#windows)
[![Linux](https://img.shields.io/badge/LINUX-2%20PROJECTS-00843D?style=for-the-badge&logo=linux&logoColor=white)](#linux)
[![Android](https://img.shields.io/badge/ANDROID-1%20PROJECT-167C80?style=for-the-badge&logo=android&logoColor=white)](#android)

### Project status key

![Working](https://img.shields.io/badge/WORKING-Tested%20on%20specified%20hardware-00843D?style=flat-square)
![Testing](https://img.shields.io/badge/TESTING-Validation%20in%20progress-C88A00?style=flat-square)
![Not working](https://img.shields.io/badge/NOT%20WORKING-Confirmed%20issue-B42318?style=flat-square)
![Unverified](https://img.shields.io/badge/UNVERIFIED-No%20test%20evidence-929292?style=flat-square)

The status describes verified operation, not whether every planned feature is complete. Red is reserved for confirmed issues, not projects that simply need more testing.

## Project overview

| Project | Operating system | Platform | Status | Version | Get it |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Gmail Unsubscriber](https://github.com/HaytamElbouhmidi/gmail-unsubscriber)** | Windows, Linux | Desktop | ![Testing](https://img.shields.io/badge/TESTING-C88A00?style=flat-square) | `Unversioned` | [Source ZIP](https://github.com/HaytamElbouhmidi/gmail-unsubscriber/archive/refs/heads/main.zip) |
| **[ROG Slash Battery Gauge](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge)** | Linux | ASUS ROG laptop | ![Working](https://img.shields.io/badge/WORKING-00843D?style=flat-square) | `Unversioned` | [Source ZIP](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge/archive/refs/heads/main.zip) |
| **[AeroDrive](https://github.com/HaytamElbouhmidi/AeroDrive)** | Android | Phone, Android Auto | ![Testing](https://img.shields.io/badge/TESTING-C88A00?style=flat-square) | `0.2.1-dev` | [Source ZIP](https://github.com/HaytamElbouhmidi/AeroDrive/archive/refs/heads/main.zip) |

**Version note:** `Unversioned` means I have not assigned a published software version or GitHub Release. It does not mean the source code is missing. AeroDrive's current Android `versionName` is `0.2.1-dev`, which is a development build, not a stable release.

### Browse by device platform

| Platform | Projects |
| :--- | :--- |
| **Desktop software** | [Gmail Unsubscriber](#gmail-unsubscriber) |
| **ASUS ROG laptop lighting** | [ROG Slash Battery Gauge](#rog-slash-battery-gauge) |
| **Android phone / Android Auto** | [AeroDrive](#aerodrive) |

---

## Windows

[![Windows desktop](https://img.shields.io/badge/WINDOWS-DESKTOP%20APPLICATIONS-123447?style=for-the-badge&logo=windows11&logoColor=white)](#windows)

### Gmail Unsubscriber

![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-UNVERSIONED-929292?style=flat-square)

Scan Gmail mailing lists, choose which senders to unsubscribe from, and export the results. Windows launchers are included. Automated offline tests are documented, but native Windows and live Gmail operations have not been independently verified in the repository's test report.

**Platform:** Windows desktop  
**Requirements:** Python 3.10 or newer, Tkinter, and a Google app password

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber/archive/refs/heads/main.zip)
[![Installation instructions](https://img.shields.io/badge/INSTRUCTIONS-SETUP-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber#setup)
[![Repository](https://img.shields.io/badge/REPOSITORY-VIEW%20CODE-123447?style=flat-square)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber)

---

## Linux

[![Linux tools](https://img.shields.io/badge/LINUX-DESKTOP%20AND%20HARDWARE-00843D?style=for-the-badge&logo=linux&logoColor=white)](#linux)

### Gmail Unsubscriber for Linux

![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-UNVERSIONED-929292?style=flat-square)

The same Gmail desktop utility is available as Python source for Linux. Its interface has been captured on Linux, and the project includes offline tests. Live Gmail behavior still requires validation.

**Platform:** Linux desktop  
**Requirements:** Python 3.10 or newer, Tkinter, and a Google app password

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber/archive/refs/heads/main.zip)
[![Installation instructions](https://img.shields.io/badge/INSTRUCTIONS-SETUP-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/gmail-unsubscriber#setup)

### ROG Slash Battery Gauge

![Working](https://img.shields.io/badge/STATUS-WORKING%20ON%20TESTED%20HARDWARE-00843D?style=flat-square)
![Version](https://img.shields.io/badge/VERSION-UNVERSIONED-929292?style=flat-square)

I use the seven white Slash Lighting segments on the back of my ASUS ROG Zephyrus G16 as a battery gauge. The fill moves from bottom to top, brightness scales with battery percentage, and a systemd service keeps the gauge active.

**Platform:** Linux, tested on CachyOS  
**Verified hardware:** ASUS ROG Zephyrus G16 GU605MY, USB HID `0b05:193b`  
**Requirements:** Python 3.10 or newer, Linux `hidraw`, and systemd for background operation

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge/archive/refs/heads/main.zip)
[![Installation instructions](https://img.shields.io/badge/INSTRUCTIONS-INSTALLATION-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge#installation)
[![Repository](https://img.shields.io/badge/REPOSITORY-VIEW%20CODE-123447?style=flat-square)](https://github.com/HaytamElbouhmidi/rog-slash-battery-gauge)

**Compatibility:** Working status applies to the tested seven-segment controller. Other ROG models and controller IDs are not automatically supported.

---

## Android

[![Android projects](https://img.shields.io/badge/ANDROID-PHONE%20AND%20ANDROID%20AUTO-167C80?style=for-the-badge&logo=android&logoColor=white)](#android)

### AeroDrive

![Testing](https://img.shields.io/badge/STATUS-TESTING-C88A00?style=flat-square)
![Development version](https://img.shields.io/badge/VERSION-0.2.1--dev-123447?style=flat-square)
![CI](https://github.com/HaytamElbouhmidi/AeroDrive/actions/workflows/ci.yml/badge.svg?branch=main)

An Android and Android Auto driving-map prototype with simulated nearby aircraft, a MapLibre map, and an optional development bridge for OpenSky. Routing, authorized live-data use, and ATC audio remain in development.

**Platform:** Android phone and Android Auto  
**Build status:** Debug APK built, linted, and verified in [GitHub Actions on October 16, 2026](https://github.com/HaytamElbouhmidi/AeroDrive/actions/runs/38916734207)  
**Validation remaining:** Physical phone and Android Auto head-unit testing  
**Release status:** No stable GitHub Release

[![Download source](https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-00843D?style=flat-square&logo=github&logoColor=white)](https://github.com/HaytamElbouhmidi/AeroDrive/archive/refs/heads/main.zip)
[![Build instructions](https://img.shields.io/badge/INSTRUCTIONS-BUILD%20AND%20TEST-202522?style=flat-square)](https://github.com/HaytamElbouhmidi/AeroDrive/blob/main/docs/first-build.md)
[![CI build artifact](https://img.shields.io/badge/DEBUG%20APK-GITHUB%20ACTIONS-C88A00?style=flat-square)](https://github.com/HaytamElbouhmidi/AeroDrive/actions/runs/38916734207)
[![Repository](https://img.shields.io/badge/REPOSITORY-VIEW%20CODE-123447?style=flat-square)](https://github.com/HaytamElbouhmidi/AeroDrive)

The debug APK is a **CI artifact for testing**, not a published application release. The automated workflow passes, but this does not establish successful operation on a physical phone or head unit. GitHub Actions artifacts may require sign-in and expire.

---

## Download and version information

- **Source ZIP:** A snapshot of the current `main` branch, not a compiled installer.
- **Working:** Verified in the stated environment or on the stated hardware.
- **Testing:** Implementation exists, but important runtime or release validation remains.
- **Not working:** Reserved for a confirmed functional failure.
- **Unverified:** Insufficient evidence to make a working or broken claim.
- **Version:** A declared application version where available. `Unversioned` indicates no version has been assigned or published.

I update project versions and readiness labels as I validate and release new builds. The AeroDrive CI badge updates automatically as its build workflow runs.

## Support

[![Ko-fi](https://img.shields.io/badge/KO--FI-SUPPORT%20MY%20WORK-00843D?style=flat-square)](https://ko-fi.com/haytamelbouhmidi)
[![Patreon](https://img.shields.io/badge/PATREON-SUPPORT%20MY%20WORK-202522?style=flat-square)](https://www.patreon.com/c/HaytamElbouhmidi)

Support is optional and does not unlock core features.
