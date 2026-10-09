from pawpal_system import Owner, Pet, Scheduler, Task


owner = Owner("Jordan", available_minutes=90)

mochi = Pet("Mochi", "dog")
mochi.add_task(Task("Morning walk", 30, "high"))
mochi.add_task(Task("Breakfast", 10, "medium"))

luna = Pet("Luna", "cat")
luna.add_task(Task("Playtime", 20, "high"))
luna.add_task(Task("Brush coat", 15, "low"))

owner.add_pet(mochi)
owner.add_pet(luna)

scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)
pet_names_by_task_id = {
    id(task): pet.name
    for pet in owner.pets
    for task in pet.tasks
}

print("Today's Schedule")
print("=" * 72)
print(f"{'Pet':<12} {'Task':<24} {'Duration':<12} {'Priority'}")
print("-" * 72)
for task in schedule:
    pet_name = pet_names_by_task_id[id(task)]
    print(
        f"{pet_name:<12} {task.title:<24} "
        f"{task.duration_minutes:>3} min       {task.priority.title()}"
    )