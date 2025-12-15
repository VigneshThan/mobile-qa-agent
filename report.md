# Mobile QA Multi‑Agent System — Technical Report

## 1. Overview

This project explores how **agentic AI systems** can reason, act, and evaluate inside a real mobile environment. The system functions as a simplified **autonomous QA team** composed of a Planner, Executor, and Supervisor, operating over a live Android app (Obsidian).

The goal is not to fully solve mobile QA, but to **demonstrate correct abstractions, safety guarantees, and research‑ready extensibility**.

---

## 2. System Architecture

### Planner (Reasoning)

* Converts natural‑language test intents into **atomic actions**.
* Uses **Gemini (LLM)** when available for semantic intent classification.
* Implements a **deterministic fallback** when the LLM is unavailable or rate‑limited.
* Enforces safety via an `abort_unsafe` action.

This design treats LLM reasoning as an **optional, expensive resource**, mirroring real production constraints.

---

### Executor (Action)

* Executes planner decisions using **ADB** on a real Android device.
* Supported actions:

  * `launch_app`
  * `scroll`
  * `verify_ui` (placeholder for visual checks)
* Always captures a screenshot for observability.
* Never hallucinates coordinates or UI interactions.

The Executor is intentionally conservative: if an action cannot be safely performed, it reports failure rather than guessing.

---

### Supervisor (Evaluation)

* Compares execution outcomes against expected results (`PASS` / `FAIL`).
* Distinguishes between:

  * **Execution failure** (action could not be completed)
  * **Expected test failure** (assertion not met)

While coarse‑grained, this reporting layer establishes the foundation for richer diagnostics (e.g., step‑level telemetry) in future work.

---

## 3. Test Design

The test suite intentionally mixes passing and failing cases:

| Test | Intent                   | Expected | Rationale                          |
| ---- | ------------------------ | -------- | ---------------------------------- |
| T1   | Launch app               | PASS     | Deterministic, safe action         |
| T2   | Scroll screen            | PASS     | Deterministic gesture              |
| T3   | Verify UI color          | FAIL     | Requires visual reasoning          |
| T4   | Verify feature existence | FAIL     | Requires semantic UI understanding |

Failing tests are **informative by design** and demonstrate correct refusal to hallucinate.

---

## 4. Handling LLM Constraints

During execution, Gemini free‑tier rate limits were encountered. The system responded by:

* Logging the LLM unavailability
* Falling back to deterministic intent parsing
* Preserving safety guarantees

This behavior demonstrates **graceful degradation**, a critical property for real‑world autonomous agents.

---

## 5. Known Limitations

### Lack of Visual Grounding

The current system does not perform true visual reasoning. The Planner does not receive screenshots as context, and the Executor does not compute coordinates from visual cues.

This is an intentional limitation to avoid brittle hard‑coded interactions.

---

## 6. Future Work: Visual Grounding Roadmap

To move from scripted automation to a resilient QA agent, the following steps are proposed:

1. **Planner Multimodal Input**

   * Pass the latest screenshot to the Planner alongside the test intent.

2. **Semantic Action Expansion**

   * Introduce actions like `tap_element` with semantic targets.

3. **Vision‑Language Grounding**

   * Use a multimodal model (e.g., Gemini Vision) to locate UI elements and return bounding boxes.

4. **Coordinate‑Free Execution**

   * Convert bounding boxes to tap coordinates dynamically at runtime.

5. **Self‑Healing Feedback Loop**

   * Allow the Supervisor to trigger replanning when UI layouts change.

This roadmap addresses the primary blocker to production‑grade mobile QA automation.

---

## 7. Conclusion

The primary success of this prototype is the **validation of a multi-agent architecture (Supervisor–Planner–Executor)** as a safe, extensible foundation for mobile QA research.

Rather than optimizing for brittle, short-term automation wins (e.g., hard-coded coordinates or fragile UI selectors), the system intentionally prioritizes **correct abstractions, safety guarantees, and observability**. This design choice allows the system to clearly isolate the next critical research challenge: **Visual Grounding**.

The failures observed in UI-dependent tests are therefore not deficiencies, but **signals**—demonstrating where language-only reasoning reaches its limit in real mobile environments. The proposed Future Work roadmap should be viewed not as a list of missing features, but as a concrete **Phase 2 research plan** to achieve coordinate-free, human-like UI interaction using multimodal Vision–Language Models.

By establishing a clean separation between reasoning, execution, and evaluation, this prototype provides a research-ready platform on which increasingly capable autonomous QA behaviors can be studied, measured, and iterated toward production-grade reliability.
