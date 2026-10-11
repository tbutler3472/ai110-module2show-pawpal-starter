from datetime import datetime

from pawpal_system import Owner, Pet, Scheduler, Task


def print_section(title: str, marker: str) -> None:
    """Print a consistently formatted section heading."""
    heading = f"[{marker}] {title}"
    print(f"\n{heading}")
    print("-" * len(heading))


def print_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """Print rows as a readable, dependency-free CLI table."""
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]
    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    print(border)
    print(
        "| "
        + " | ".join(
            header.ljust(width) for header, width in zip(headers, widths)
        )
        + " |"
    )
    print(border)
    for row in rows:
        print(
            "| "
            + " | ".join(value.ljust(width) for value, width in zip(row, widths))
            + " |"
        )
    print(border)


owner = Owner("Jordan", available_minutes=90)
today = datetime.now()

mochi = Pet("Mochi", "dog")
mochi.add_task(
    Task("Morning walk", 30, "high", scheduled_time="08:00", due_date=today)
)
mochi.add_task(Task("Breakfast", 10, "medium", scheduled_time="07:00"))

luna = Pet("Luna", "cat")
luna.add_task(Task("Playtime", 20, "high", scheduled_time="09:30"))
luna.add_task(
    Task("Medication", 5, "high", scheduled_time="08:00", due_date=today)
)
brush_coat = Task("Brush coat", 15, "low", scheduled_time="10:00")
luna.add_task(brush_coat)

daily_task = Task(
    "Daily feeding",
    5,
    "high",
    frequency="daily",
    scheduled_time="07:00",
    due_date=today,
)
weekly_task = Task(
    "Weekly grooming",
    15,
    "medium",
    frequency="weekly",
    scheduled_time="10:30",
    due_date=today,
)
one_time_task = Task("One-time checkup", 25, "low", due_date=today)
mochi.add_task(daily_task)
mochi.add_task(weekly_task)
luna.add_task(one_time_task)

owner.add_pet(mochi)
owner.add_pet(luna)

print_section("Recurring Task Completion", "RECURRING")
completion_rows = []
for pet, task in (
    (mochi, daily_task),
    (mochi, weekly_task),
    (luna, one_time_task),
    (luna, brush_coat),
):
    next_task = pet.complete_task(task)
    if next_task is None:
        outcome = "[COMPLETE]"
        next_due = "No repeat"
    else:
        outcome = "[COMPLETE]"
        next_due = f"{next_task.due_date:%Y-%m-%d}"
    completion_rows.append((task.title, outcome, next_due))
print_table(("Task", "Status", "Next due"), completion_rows)

scheduler = Scheduler()
print_section("Scheduling Conflict Warnings", "WARNINGS")
conflict_warnings = scheduler.detect_conflicts(owner)
if conflict_warnings:
    for warning in conflict_warnings:
        print(f"WARNING: {warning}")
else:
    print("[OK] No scheduling conflicts.")

pet_names_by_task_id = {
    id(task): pet.name
    for pet in owner.pets
    for task in pet.tasks
}

print_section("Tasks Sorted by Scheduled Time", "TASKS")
sorted_task_rows = []
for task in scheduler.sort_by_time(owner.get_tasks()):
    pet_name = pet_names_by_task_id[id(task)]
    scheduled_time = task.scheduled_time or "Unscheduled"
    status = "[COMPLETE]" if task.completed else "[PENDING]"
    sorted_task_rows.append((scheduled_time, pet_name, task.title, status))
print_table(("Time", "Pet", "Task", "Status"), sorted_task_rows)

print_section("Tasks Sorted by Priority", "PRIORITY")
priority_task_rows = []
for task in scheduler.sort_by_priority(owner.get_tasks()):
    pet_name = pet_names_by_task_id[id(task)]
    priority_task_rows.append(
        (
            task.priority.title(),
            task.scheduled_time or "Unscheduled",
            pet_name,
            task.title,
            "[COMPLETE]" if task.completed else "[PENDING]",
        )
    )
print_table(
    ("Priority", "Time", "Pet", "Task", "Status"),
    priority_task_rows,
)

print_section("Tasks Filtered by Pet (Mochi)", "FILTER")
mochi_tasks = owner.get_tasks(pet_name="Mochi")
print_table(("Task", "Status"), [
    (task.title, "[COMPLETE]" if task.completed else "[PENDING]")
    for task in mochi_tasks
])

print_section("Tasks Filtered by Completion Status (Complete)", "FILTER")
completed_tasks = owner.get_tasks(completed=True)
print_table(("Pet", "Task"), [
    (pet_names_by_task_id[id(task)], task.title)
    for task in completed_tasks
])

print_section("Mochi's Incomplete Tasks (Combined Filters)", "FILTER")
mochi_incomplete_tasks = owner.get_tasks(pet_name="Mochi", completed=False)
print_table(("Task", "Status"), [
    (task.title, "[PENDING]")
    for task in mochi_incomplete_tasks
])

schedule = scheduler.generate_schedule(owner)

print_section("Today's Schedule", "SCHEDULE")
schedule_rows = []
for task in scheduler.sort_by_time(schedule):
    pet_name = pet_names_by_task_id[id(task)]
    schedule_rows.append(
        (
            task.scheduled_time or "Unscheduled",
            pet_name,
            task.title,
            f"{task.duration_minutes} min",
            task.priority.title(),
            "[PENDING]",
        )
    )
if schedule_rows:
    print_table(
        ("Time", "Pet", "Task", "Duration", "Priority", "Status"),
        schedule_rows,
    )
else:
    print("[INFO] No unfinished tasks fit within the available time.")