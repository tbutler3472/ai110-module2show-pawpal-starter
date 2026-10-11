# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## Features

PawPal+ includes these implemented features:

- Owner and pet profile management so a user can add pets and keep them organized.
- Task tracking with title, duration, priority (Medium by default), and optional
  scheduled time.
- Sorting of tasks by scheduled time using `Scheduler.sort_by_time()` so the list is always in chronological order.
- Priority sorting with `Scheduler.sort_by_priority()`, ordering High, Medium,
  then Low priority tasks and sorting scheduled times within each priority.
- Filtering by pet name and completion status using `Owner.get_tasks()`, including case-insensitive pet matching.
- Recurring task support through `Pet.complete_task()`, which creates a new daily or weekly occurrence after a task is marked complete.
- Scheduling conflict detection with `Scheduler.detect_conflicts()`, which warns when multiple tasks share the same date and time.
- Daily schedule generation based on available time and task priority using `Scheduler.generate_schedule()`.
- Streamlit display features that show pet information, tasks, warnings, and generated schedules in a clear dashboard layout.

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

## Demo Walkthrough

The Streamlit app gives a pet owner a simple dashboard for adding pets, adding tasks, filtering the task list, checking conflicts, and generating a daily schedule. The interface keeps the task data organized and makes it easy to see what is scheduled, completed, and still waiting to be done.

1. Add a pet profile. In the app, enter an owner name and pet name, then choose a species and click Add pet. The pet appears in the current pets table.
2. Add care tasks. Choose a pet, enter a task title, duration, priority, and optional scheduled time such as `08:00`. When you click Add task, the task is saved and appears in the task list.
3. Review the task list. The app shows tasks in chronological order using
   `Scheduler.sort_by_time()`. The CLI demo also shows a separate priority sort
   using `Scheduler.sort_by_priority()`. You can filter the list by pet and by
   completed or pending status using `Owner.get_tasks()`.
4. Check for conflicts. When multiple tasks land on the same date and time, the scheduler triggers a warning message with `st.warning()`, so the owner can fix overlaps before generating the plan.
5. Generate a schedule. Set the owner's available time and click Generate schedule. The scheduler prioritizes higher-priority unfinished tasks that fit the available minutes and presents the result neatly in a table.

### CLI Output Formatting

The command-line demo in `main.py` displays recurring tasks, scheduling conflicts, sorted and filtered tasks, and the generated schedule in organized tables. The `print_section()` function separates and labels each section, while `print_table()` adjusts the column widths to keep everything lined up. Status labels like `[COMPLETE]`, `[PENDING]`, `[OK]`, `WARNING:`, and `[INFO]` make it easier to understand the results. These functions only use built-in Python features, so no additional libraries are needed. The CLI demonstrates both chronological and
priority sorting; the Streamlit interface continues to use chronological
sorting.

Sample output from running `python main.py` (dates are based on when the program was run):

```text
[RECURRING] Recurring Task Completion
-------------------------------------
+------------------+------------+------------+
| Task             | Status     | Next due   |
+------------------+------------+------------+
| Daily feeding    | [COMPLETE] | 2026-10-11 |
| Weekly grooming  | [COMPLETE] | 2026-10-17 |
| One-time checkup | [COMPLETE] | No repeat  |
| Brush coat       | [COMPLETE] | No repeat  |
+------------------+------------+------------+

[WARNINGS] Scheduling Conflict Warnings
---------------------------------------
WARNING: Scheduling conflict on 2026-10-10 at 08:00: 'Morning walk' for Mochi, 'Medication' for Luna.

[TASKS] Tasks Sorted by Scheduled Time
--------------------------------------
+-------------+-------+------------------+------------+
| Time        | Pet   | Task             | Status     |
+-------------+-------+------------------+------------+
| 07:00       | Mochi | Breakfast        | [PENDING]  |
| 07:00       | Mochi | Daily feeding    | [COMPLETE] |
| 07:00       | Mochi | Daily feeding    | [PENDING]  |
| 08:00       | Mochi | Morning walk     | [PENDING]  |
| 08:00       | Luna  | Medication       | [PENDING]  |
| 09:30       | Luna  | Playtime         | [PENDING]  |
| 10:00       | Luna  | Brush coat       | [COMPLETE] |
| 10:30       | Mochi | Weekly grooming  | [COMPLETE] |
| 10:30       | Mochi | Weekly grooming  | [PENDING]  |
| Unscheduled | Luna  | One-time checkup | [COMPLETE] |
+-------------+-------+------------------+------------+

[PRIORITY] Tasks Sorted by Priority
-----------------------------------
+----------+-------------+-------+------------------+------------+
| Priority | Time        | Pet   | Task             | Status     |
+----------+-------------+-------+------------------+------------+
| High     | 07:00       | Mochi | Daily feeding    | [COMPLETE] |
| High     | 07:00       | Mochi | Daily feeding    | [PENDING]  |
| High     | 08:00       | Mochi | Morning walk     | [PENDING]  |
| High     | 08:00       | Luna  | Medication       | [PENDING]  |
| High     | 09:30       | Luna  | Playtime         | [PENDING]  |
| Medium   | 07:00       | Mochi | Breakfast        | [PENDING]  |
| Medium   | 10:30       | Mochi | Weekly grooming  | [COMPLETE] |
| Medium   | 10:30       | Mochi | Weekly grooming  | [PENDING]  |
| Low      | 10:00       | Luna  | Brush coat       | [COMPLETE] |
| Low      | Unscheduled | Luna  | One-time checkup | [COMPLETE] |
+----------+-------------+-------+------------------+------------+

[FILTER] Tasks Filtered by Pet (Mochi)
--------------------------------------
+-----------------+------------+
| Task            | Status     |
+-----------------+------------+
| Morning walk    | [PENDING]  |
| Breakfast       | [PENDING]  |
| Daily feeding   | [COMPLETE] |
| Weekly grooming | [COMPLETE] |
| Daily feeding   | [PENDING]  |
| Weekly grooming | [PENDING]  |
+-----------------+------------+

[FILTER] Tasks Filtered by Completion Status (Complete)
-------------------------------------------------------
+-------+------------------+
| Pet   | Task             |
+-------+------------------+
| Mochi | Daily feeding    |
| Mochi | Weekly grooming  |
| Luna  | Brush coat       |
| Luna  | One-time checkup |
+-------+------------------+

[FILTER] Mochi's Incomplete Tasks (Combined Filters)
----------------------------------------------------
+-----------------+-----------+
| Task            | Status    |
+-----------------+-----------+
| Morning walk    | [PENDING] |
| Breakfast       | [PENDING] |
| Daily feeding   | [PENDING] |
| Weekly grooming | [PENDING] |
+-----------------+-----------+

[SCHEDULE] Today's Schedule
---------------------------
+-------+-------+--------------+----------+----------+-----------+
| Time  | Pet   | Task         | Duration | Priority | Status    |
+-------+-------+--------------+----------+----------+-----------+
| 07:00 | Mochi | Breakfast    | 10 min   | Medium   | [PENDING] |
| 08:00 | Mochi | Morning walk | 30 min   | High     | [PENDING] |
| 08:00 | Luna  | Medication   | 5 min    | High     | [PENDING] |
| 09:30 | Luna  | Playtime     | 20 min   | High     | [PENDING] |
+-------+-------+--------------+----------+----------+-----------+
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\tyeso\OneDrive\Documents\pawpal\ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 23 items

tests\test_pawpal.py .......................                             [100%]

============================== 23 passed in 0.18s ==============================
```
Test Coverage: 
The 23 tests cover the main features of the PawPal system, including sorting tasks by time and priority, filtering tasks, and detecting scheduling conflicts. They also check edge cases such as an owner with no tasks, completing tasks, and ensuring tasks fit within the owner's available time.

Confidence Level: 
My confidence level is 4/5 stars because all 23 tests pass and the tested features work as intended. It is not 5/5 because there may still be situations that have not been tested.

## 📐 Smarter Scheduling

PawPal+ includes these scheduling features:

- **Priority sorting — `Scheduler.sort_by_priority()`**: Sorts High, Medium,
  then Low priority tasks. Within each priority, tasks sort by scheduled
  `HH:MM` time, with unscheduled tasks last.
- **Chronological sorting — `Scheduler.sort_by_time()`**: Sorts tasks by their scheduled
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
