import os
import google.generativeai as genai

# -----------------------------
# Gemini Configuration
# -----------------------------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-latest")

# -----------------------------
# Planner cache (MUST exist)
# -----------------------------
PLAN_CACHE = {}

# -----------------------------
# Planner
# -----------------------------
def plan(description: str) -> dict:
    """
    Planner with LLM-first reasoning and deterministic fallback.
    Returns: { "action": "<action>" }
    """

    # Cache hit
    if description in PLAN_CACHE:
        return PLAN_CACHE[description]

    # --- Try Gemini first ---
    try:
        prompt = f"""
Decide the safest single action.

Allowed actions:
launch_app
scroll
verify_ui
abort_unsafe

Return ONE word only.

Instruction:
{description}
"""
        response = model.generate_content(prompt)
        text = (response.text or "").strip().lower()

    except Exception as e:
        print(f"[PLANNER] Gemini unavailable, using fallback: {e}")
        text = ""  # force fallback

    # --- Deterministic fallback ---
    desc = description.lower()

    if "launch" in desc or "open" in desc:
        action = "launch_app"
    elif "scroll" in desc or "swipe" in desc:
        action = "scroll"
    elif "verify" in desc or "check" in desc:
        action = "verify_ui"
    else:
        action = "abort_unsafe"

    plan = {"action": action}
    PLAN_CACHE[description] = plan
    return plan
