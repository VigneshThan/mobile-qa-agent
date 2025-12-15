import subprocess
import time
from tools.adb_tools import launch_app, take_screenshot


def execute(plan, test_id):
    print("[EXECUTOR] Running test:", test_id)
    print("[EXECUTOR] Plan:", plan)

    action = plan.get("action")

    # -------- SAFE ABORT (RESEARCH-GRADE BEHAVIOR) --------
    if action == "abort_unsafe":
        print("[EXECUTOR] Aborting unsafe action")
        take_screenshot(f"{test_id}.png")
        return {
            "success": False,
            "observation": "Action deemed unsafe to automate"
        }

    # -------- LAUNCH APP --------
    if action == "launch_app":
        launch_app("md.obsidian")
        take_screenshot(f"{test_id}.png")
        return {
            "success": True,
            "observation": "App launched successfully"
        }

    # -------- SCROLL --------
    if action == "scroll":
        subprocess.run(
            ["adb", "shell", "input", "swipe", "540", "2000", "540", "800", "500"],
            check=True
        )
        take_screenshot(f"{test_id}.png")
        return {
            "success": True,
            "observation": "Screen scrolled"
        }

    # -------- VERIFY UI (OBSERVATION ONLY) --------
    if action == "verify_ui":
        take_screenshot(f"{test_id}.png")
        return {
            "success": False,
            "observation": "UI verification requires visual reasoning"
        }

    # -------- FALLBACK --------
    print("[EXECUTOR] Unknown action")
    take_screenshot(f"{test_id}.png")
    return {
        "success": False,
        "observation": "Unknown action"
    }

