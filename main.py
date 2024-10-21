import os
import subprocess
import requests
import json

def get_latest_frida_version():
    url = "https://api.github.com/repos/frida/frida/releases/latest"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['tag_name']

def get_device_arch():
    result = subprocess.run(["adb", "shell", "getprop", "ro.product.cpu.abi"], capture_output=True, text=True)
    arch = result.stdout.strip()
    if 'arm64' in arch:
        return 'arm64'
    elif 'arm' in arch:
        return 'arm'
    elif 'x86_64' in arch:
        return 'x86_64'
    elif 'x86' in arch:
        return 'x86'
    else:
        raise ValueError(f"Unsupported architecture: {arch}")

def download_frida(version, arch):
    url = f"https://github.com/frida/frida/releases/download/{version}/frida-server-{version}-android-{arch}.xz"
    response = requests.get(url)
    with open("frida-server.xz", "wb") as f:
        f.write(response.content)
    os.system("xz -d frida-server.xz")

def upload_frida():
    subprocess.run(["adb", "push", "frida-server", "/data/local/tmp/"])
    subprocess.run(["adb", "shell", "chmod", "755", "/data/local/tmp/frida-server"])

def main():
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device" not in result.stdout:
            print("No device connected. Please connect an Android device.")
            return

        version = get_latest_frida_version()
        arch = get_device_arch()
        print(f"Latest Frida version: {version}")
        print(f"Device architecture: {arch}")
        print("Downloading Frida...")
        download_frida(version, arch)
        print("Uploading Frida to device...")
        upload_frida()
        print("Frida has been successfully uploaded to the device.")
        print("You can now start Frida server on the device with:")
        print("adb shell '/data/local/tmp/frida-server &'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if os.path.exists("frida-server"):
            os.remove("frida-server")

if __name__ == "__main__":
    main()
