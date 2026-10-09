# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
========================================================================
Pet          Task                     Duration     Priority
------------------------------------------------------------------------
Mochi        Morning walk              30 min       High
Luna         Playtime                  20 min       High
Mochi        Breakfast                 10 min       Medium
Luna         Brush coat                15 min       Low
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

PawPal+ includes these scheduling features:

- **Sorting — `Scheduler.sort_by_time()`**: Sorts tasks by their scheduled
  `HH:MM` time. Tasks without a scheduled time appear last.
- **Filtering — `Owner.get_tasks()`**: Returns all tasks or filters them by pet
  name, completion status, or both. Pet-name matching ignores letter case.
- **Recurring tasks — `Pet.complete_task()`**: Completing a daily or weekly task
  creates a new incomplete occurrence due one or seven days later. One-time tasks
  are not repeated, and completing the same task again does not create another
  occurrence.
- **Conflict detection — `Scheduler.detect_conflicts()`**: Returns warning
  messages when tasks share an exact scheduled time and due date, including
  tasks belonging to different pets. Tasks without a scheduled time are ignored.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
