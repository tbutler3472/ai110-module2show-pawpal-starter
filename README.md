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
- Task tracking with title, duration, priority, and optional scheduled time.
- Sorting of tasks by scheduled time using `Scheduler.sort_by_time()` so the list is always in chronological order.
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
3. Review the task list. The app shows tasks in chronological order using `Scheduler.sort_by_time()`. You can also filter the list by pet and by completed or pending status using `Owner.get_tasks()`.
4. Check for conflicts. When multiple tasks land on the same date and time, the scheduler triggers a warning message with `st.warning()`, so the owner can fix overlaps before generating the plan.
5. Generate a schedule. Set the owner's available time and click Generate schedule. The scheduler prioritizes higher-priority unfinished tasks that fit the available minutes and presents the result neatly in a table.

The following sample output shows the command-line behavior of `python main.py`, including recurring task completion, conflict warnings, chronological sorting, filtering, and the generated schedule:

```text
Recurring Task Completion
- Daily feeding: completed; next due 2026-10-10
- Weekly grooming: completed; next due 2026-10-16
- One-time checkup: completed; no repeat created
- Brush coat: completed; no repeat created

Scheduling Conflict Warnings
- Scheduling conflict on 2026-10-09 at 08:00: 'Morning walk' for Mochi, 'Medication' for Luna.
Tasks Sorted by Scheduled Time
========================================================================
Time       Pet          Task                     Status
------------------------------------------------------------------------
07:00      Mochi        Breakfast                Pending
07:00      Mochi        Daily feeding            Complete
07:00      Mochi        Daily feeding            Pending
08:00      Mochi        Morning walk             Pending
08:00      Luna         Medication               Pending
09:30      Luna         Playtime                 Pending
10:00      Luna         Brush coat               Complete
10:30      Mochi        Weekly grooming          Complete
10:30      Mochi        Weekly grooming          Pending
Unscheduled Luna         One-time checkup         Complete

Tasks Filtered by Pet (Mochi)
- Morning walk
- Breakfast
- Daily feeding
- Weekly grooming
- Daily feeding
- Weekly grooming

Tasks Filtered by Completion Status (Complete)
- Daily feeding
- Weekly grooming
- Brush coat
- One-time checkup

Mochi's Incomplete Tasks (Combined Filters)
- Morning walk
- Breakfast
- Daily feeding
- Weekly grooming
Today's Schedule
========================================================================
Time       Pet          Task                     Duration     Priority
------------------------------------------------------------------------
07:00      Mochi        Breakfast                 10 min       Medium
08:00      Mochi        Morning walk              30 min       High
08:00      Luna         Medication                 5 min       High
09:30      Luna         Playtime                  20 min       High
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
==================================== test session starts ====================================
platform win32 -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\tyeso\OneDrive\Documents\pawpal\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 19 items                                                                           

tests\test_pawpal.py ...................                                               [100%]

==================================== 19 passed in 0.20s =====================================
```
Test Coverage: 
The 19 test cover the main features of the PawPal system which includes sorting task by time, filtering task, detecting scheduling conflicts and more. The test not only cover the main features but they also check edge cases like having no task, completing task, making sure they fit with the owners availble time.

Confidence Level: 
My confidence level is a 4/5 stars because all 19 of the test pass and all the main features tested work how they are intended to work. The reason it's not 5 stars however is because I believe there are still situations that weren't tested so more testing would help increase the confidence score to 5 stars. 

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

