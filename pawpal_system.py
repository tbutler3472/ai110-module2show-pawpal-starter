from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta


class Owner:
    def __init__(
        self, name: str, preferences: str = "", available_minutes: int = 0
    ) -> None:
        """Initialize an owner and their available time."""
        self.name = name
        self.preferences = preferences
        self.available_minutes = available_minutes
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pets."""
        if pet not in self.pets:
            self.pets.append(pet)

    def update_pet(self, pet: Pet) -> None:
        """Replace a pet with the same name or add it if absent."""
        for index, existing_pet in enumerate(self.pets):
            if existing_pet.name == pet.name:
                self.pets[index] = pet
                return
        self.add_pet(pet)

    def get_tasks(
        self,
        pet_name: str | None = None,
        completed: bool | None = None,
    ) -> list[Task]:
        """Filter tasks by case-insensitive pet name and/or completion status."""
        return [
            task
            for pet in self.pets
            if pet_name is None or pet.name.casefold() == pet_name.casefold()
            for task in pet.tasks
            if completed is None or task.completed is completed
        ]


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        if task not in self.tasks:
            self.tasks.append(task)

    def complete_task(self, task: Task) -> Task | None:
        """Complete this pet's task and add a fresh daily or weekly occurrence."""
        if not any(existing_task is task for existing_task in self.tasks):
            raise ValueError("The task does not belong to this pet.")
        if task.completed:
            return None

        task.mark_complete()
        frequency = task.frequency.strip().casefold()
        recurrence_days = {"daily": 1, "weekly": 7}.get(frequency)
        if recurrence_days is None:
            return None

        next_task = Task(
            title=task.title,
            duration_minutes=task.duration_minutes,
            priority=task.priority,
            description=task.description,
            frequency=task.frequency,
            scheduled_time=task.scheduled_time,
            due_date=(task.due_date or datetime.now())
            + timedelta(days=recurrence_days),
        )
        self.add_task(next_task)
        return next_task


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    description: str = ""
    frequency: str = ""
    completed: bool = False
    scheduled_time: str | None = None
    due_date: datetime | None = None

    def update_priority(self, priority: str) -> None:
        """Set the task's priority."""
        self.priority = priority

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True


class Scheduler:
    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort HH:MM task times chronologically, placing unscheduled tasks last."""
        return sorted(
            tasks,
            key=lambda task: (
                not task.scheduled_time,
                task.scheduled_time or "",
            ),
        )

    def detect_conflicts(self, owner: Owner) -> list[str]:
        """Warn when tasks share an exact time and due date; skip untimed tasks."""
        tasks_by_slot: dict[
            tuple[date | None, str], list[tuple[str, Task]]
        ] = {}
        for pet in owner.pets:
            for task in pet.tasks:
                if not task.scheduled_time:
                    continue
                due_date = task.due_date.date() if task.due_date else None
                slot = (due_date, task.scheduled_time)
                tasks_by_slot.setdefault(slot, []).append((pet.name, task))

        warnings = []
        for (due_date, scheduled_time), conflicting_tasks in tasks_by_slot.items():
            if len(conflicting_tasks) < 2:
                continue
            date_label = due_date.isoformat() if due_date else "unspecified date"
            task_labels = ", ".join(
                f"'{task.title}' for {pet_name}"
                for pet_name, task in conflicting_tasks
            )
            warnings.append(
                f"Scheduling conflict on {date_label} at {scheduled_time}: "
                f"{task_labels}."
            )
        return warnings

    def generate_schedule(self, owner: Owner) -> list[Task]:
        """Return prioritized unfinished tasks that fit the owner's available time."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        today = datetime.now().date()
        pending_tasks = [
            task for task in owner.get_tasks()
            if (
                not task.completed
                and task.duration_minutes > 0
                and (task.due_date is None or task.due_date.date() <= today)
            )
        ]
        ordered_tasks = sorted(
            pending_tasks,
            key=lambda task: priority_order.get(task.priority.lower(), len(priority_order)),
        )

        schedule: list[Task] = []
        remaining_minutes = max(0, owner.available_minutes)
        for task in ordered_tasks:
            if task.duration_minutes <= remaining_minutes:
                schedule.append(task)
                remaining_minutes -= task.duration_minutes
        return schedule

    def explain_task(self, task: Task) -> str:
        """Describe a task's priority and duration."""
        return (
            f"{task.title} has {task.priority} priority "
            f"and takes {task.duration_minutes} minutes."
        )