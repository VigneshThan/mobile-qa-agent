import subprocess
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "screenshots")


def launch_app(package_name: str):
    print("[ADB] Launching app:", package_name)

    subprocess.run(
        [
            "adb",
            "shell",
            "monkey",
            "-p",
            package_name,
            "-c",
            "android.intent.category.LAUNCHER",
            "1",
        ],
        check=True,
    )


def take_screenshot(filename: str):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    full_path = os.path.join(SCREENSHOT_DIR, filename)

    print("[ADB] Saving screenshot:", full_path)

    with open(full_path, "wb") as f:
        subprocess.run(
            ["adb", "exec-out", "screencap", "-p"],
            stdout=f,
            check=True,
        )

    print("[ADB] SCREENSHOT SAVED")

