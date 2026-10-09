from __future__ import annotations

from dataclasses import dataclass, field


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

    def get_tasks(self) -> list[Task]:
        """Return all tasks belonging to the owner's pets."""
        return [task for pet in self.pets for task in pet.tasks]


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        if task not in self.tasks:
            self.tasks.append(task)


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    description: str = ""
    frequency: str = ""
    completed: bool = False

    def update_priority(self, priority: str) -> None:
        """Set the task's priority."""
        self.priority = priority

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True


class Scheduler:
    def generate_schedule(self, owner: Owner) -> list[Task]:
        """Return prioritized unfinished tasks that fit the owner's available time."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        pending_tasks = [
            task for task in owner.get_tasks()
            if not task.completed and task.duration_minutes > 0
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