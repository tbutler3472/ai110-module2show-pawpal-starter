from datetime import datetime

from pawpal_system import Owner, Pet, Scheduler, Task


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

print("Recurring Task Completion")
for pet, task in (
    (mochi, daily_task),
    (mochi, weekly_task),
    (luna, one_time_task),
    (luna, brush_coat),
):
    next_task = pet.complete_task(task)
    if next_task is None:
        print(f"- {task.title}: completed; no repeat created")
    else:
        print(
            f"- {task.title}: completed; next due "
            f"{next_task.due_date:%Y-%m-%d}"
        )

scheduler = Scheduler()
print("\nScheduling Conflict Warnings")
conflict_warnings = scheduler.detect_conflicts(owner)
if conflict_warnings:
    for warning in conflict_warnings:
        print(f"- {warning}")
else:
    print("- No scheduling conflicts.")

pet_names_by_task_id = {
    id(task): pet.name
    for pet in owner.pets
    for task in pet.tasks
}

print("Tasks Sorted by Scheduled Time")
print("=" * 72)
print(f"{'Time':<10} {'Pet':<12} {'Task':<24} {'Status'}")
print("-" * 72)
for task in scheduler.sort_by_time(owner.get_tasks()):
    pet_name = pet_names_by_task_id[id(task)]
    scheduled_time = task.scheduled_time or "Unscheduled"
    status = "Complete" if task.completed else "Pending"
    print(f"{scheduled_time:<10} {pet_name:<12} {task.title:<24} {status}")

print("\nTasks Filtered by Pet (Mochi)")
for task in owner.get_tasks(pet_name="Mochi"):
    print(f"- {task.title}")

print("\nTasks Filtered by Completion Status (Complete)")
for task in owner.get_tasks(completed=True):
    print(f"- {task.title}")

print("\nMochi's Incomplete Tasks (Combined Filters)")
for task in owner.get_tasks(pet_name="Mochi", completed=False):
    print(f"- {task.title}")

schedule = scheduler.generate_schedule(owner)

print("Today's Schedule")
print("=" * 72)
print(f"{'Time':<10} {'Pet':<12} {'Task':<24} {'Duration':<12} {'Priority'}")
print("-" * 72)
for task in scheduler.sort_by_time(schedule):
    pet_name = pet_names_by_task_id[id(task)]
    print(
        f"{task.scheduled_time or 'Unscheduled':<10} {pet_name:<12} {task.title:<24} "
        f"{task.duration_minutes:>3} min       {task.priority.title()}"
    )