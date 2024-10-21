# Frida Installer Script

This script automates the process of downloading the latest Frida server and installing it on a connected Android device. It handles architecture detection and simplifies the setup for Frida-based reverse engineering or instrumentation.

## Prerequisites

* Python 3 installed.
* `adb` in your system's PATH.
* `xz` utility installed.

## Usage
0.  install requrements `pip install -r dep.txt`
1.  Save the script as a Python file (e.g., `frida_installer.py`).
2.  Connect your Android device via USB debugging.
3.  Run the script from your terminal: `python frida_installer.py`

## How it works

1. **Device Detection:** The script checks for a connected device using `adb devices`.  If no device is found, it displays an error message.

2. **Frida Version Retrieval:** It fetches the latest Frida version from the GitHub API.

3. **Architecture Detection:** It determines the device's architecture (arm64, arm, x86_64, x86) using `adb shell getprop ro.product.cpu.abi`.

4. **Frida Download:** Downloads the appropriate Frida server version for the detected architecture from the official GitHub releases. The server is downloaded as an xz compressed file and then decompressed.

5. **Frida Upload:** Uploads `frida-server` to the device's `/data/local/tmp/` directory using `adb push`.

6. **Permissions Setting:** Sets execute permissions for `frida-server` on the device.

## Error
If face any error please open an issue.
