## Chosen Framework
For this assignment, I chose **Google Agent Development Kit (ADK)** as the framework for
implementing the mobile QA multi-agent system.
## Why Google ADK Fits This Problem
Google ADK is well suited for this task because it naturally supports a multi-agent architecture
with clearly separated responsibilities. The assignment requires three distinct agents - Planner,
Executor, and Supervisor, and ADK provides a clean way to define these roles and manage
their interactions. LLM configuration is centralized through ADK, allowing the underlying model to be swapped without modifying agent logic.

The Planner agent benefits from ADK’s structured reasoning and JSON-based outputs, which
makes it easier to translate natural language test cases into concrete UI actions such as taps,
swipes, and text input. The Executor agent can reliably invoke external tools (ADB commands)
through ADK’s tool-calling mechanism, ensuring a clear separation between decision-making
and action execution.

The Supervisor agent aligns well with ADK’s evaluation-oriented design, allowing it to analyze
screenshots and action results to determine whether a step failed due to execution issues or
assertion mismatches. Overall, ADK enables a modular, readable, and extensible design that
closely matches the requirements of the assignment.

## Alternatives Considered
An alternative approach would be to build a fully custom lightweight agent system using direct
LLM calls and Python orchestration. While this approach offers full control, it requires additional
effort to manage agent coordination, tool invocation, and structured outputs.
Google ADK was preferred because it reduces boilerplate code, enforces clearer agent
boundaries, and provides better support for structured multi-agent workflows.
## Limitations and Risks
One limitation of using Google ADK is the dependency on the framework’s abstractions, which
may reduce flexibility compared to a fully custom implementation. Additionally, performance may
be affected by repeated LLM calls when evaluating screenshots and UI states.
However, these trade-offs are acceptable for this assignment, as clarity, correctness, and
maintainability are prioritized over low-level optimization.
