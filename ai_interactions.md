# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | Same model in a separate Copilot chat | Same model in a separate Copilot chat |
| **Prompt** | General request to make `Scheduler.generate_schedule()` more readable. | Specific request to improve readability while preserving behavior, filtering, priority ordering, return types, and the existing project structure. |
| **Response summary** | Suggested adding an `is_eligible()` helper, changing `lower()` to `casefold()`, and using `continue` to skip tasks that do not fit. | Suggested clearer variable names, kept `lower()` unchanged, and used `continue` to skip tasks that do not fit. |
| **What was useful** | The helper could make the eligibility check easier to understand, and `continue` makes the scheduling loop easier to follow. | The requirements kept the response focused on readability while reminding it to preserve existing behavior and structure. |
| **Problems noticed** | It suggested a case-comparison change that was not needed for the readability goal, and adding a helper would expand the changes. | It gave fewer types of suggestions, but they were closely connected to the requested cleanup. |
| **Decision** | Less useful overall because some suggestions went beyond a focused readability change. | More useful: its changes stayed focused and closer to the original code. |

### Comparison

Both responses suggested using `continue` when a task does not fit, which makes that part of the loop clearer. Prompt 1 offered an additional helper, but that meant a broader change; replacing `lower()` with `casefold()` also changed behavior rather than only improving readability. Prompt 2 was clearer about the limits of the task and gave a more complete, targeted response. Its suggestions were useful and easier to evaluate against the existing code.

This was a code-review comparison only. I did not apply or test either set of suggested changes. My final decision is that the detailed prompt was more useful because it kept the changes focused and closer to the original code.
