# Mobile QA Multi‑Agent System

A research prototype of an **autonomous mobile QA agent** that uses an LLM‑driven Planner, a deterministic Executor (ADB), and a Supervisor to evaluate outcomes. The system demonstrates how natural‑language test intents can be translated into real actions on an Android device while prioritizing safety and graceful degradation.

> **Target app used for demonstration:** Obsidian (Android)

---

## High‑Level Architecture

```
User Test Intent
      │
      ▼
┌──────────┐      ┌──────────┐      ┌────────────┐
│ Planner  │ ───▶ │ Executor │ ───▶ │ Supervisor │
│ (LLM)    │      │ (ADB)    │      │ (Assertions)│
└──────────┘      └──────────┘      └────────────┘
```

* **Planner**: Uses Gemini (when available) to reason over natural‑language test descriptions and decide a safe, atomic action. Includes a deterministic fallback when the LLM is unavailable.
* **Executor**: Executes actions on a real Android device via ADB (launch, scroll, screenshot). Never hallucinates UI interactions.
* **Supervisor**: Evaluates execution results against expected outcomes (PASS/FAIL) and reports verdicts.

---

## Repository Structure

```
mobile_qa_agent/
├── agents/
│   ├── planner.py        # LLM reasoning + deterministic fallback
│   ├── executor.py       # ADB-backed action execution
│   └── supervisor.py     # PASS/FAIL evaluation logic
├── tools/
│   └── adb_tools.py      # ADB helpers (launch app, screenshot)
├── tests/
│   └── qa_tests.json     # Natural-language test intents
├── screenshots/          # Runtime screenshots (auto-generated)
├── main.py               # Orchestration entry point
├── requirements.txt      # Minimal Python deps
├── README.md
└── report.md             # Technical report
```

---

## Setup

### Prerequisites

* Android device or emulator connected via ADB
* Python 3.10+
* (Optional) Gemini API key

### Install dependencies

```bash
pip install -r requirements.txt
```

### (Optional) Configure Gemini

```bash
export GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

If the API key is not set or rate‑limited, the system **automatically falls back** to a deterministic planner.

---

## Run

```bash
python3 main.py
```

* Screenshots are saved to `screenshots/` for every test.
* PASS/FAIL results are printed to stdout by the Supervisor.

---

## Test Philosophy

* **PASS tests** validate deterministic, safe actions (launching the app, scrolling).
* **FAIL tests** intentionally require visual reasoning (UI color, feature existence) and demonstrate the system’s refusal to hallucinate.

This design highlights the **limits of non‑visual automation** and motivates future work.

---

## Notes on Design Decisions

* No hard‑coded coordinates are used.
* No fragile UI selectors are assumed.
* Visual grounding is explicitly left as future work (see `report.md`).

---

## License

Research prototype — provided for evaluation purposes only.
