from __future__ import annotations

from dataclasses import dataclass, field


class Owner:
    def __init__(self, name: str, preferences: str = "") -> None:
        self.name = name
        self.preferences = preferences
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def update_pet(self, pet: Pet) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str

    def update_priority(self, priority: str) -> None:
        pass


class Scheduler:
    def generate_schedule(self, owner: Owner) -> list[Task]:
        pass

    def explain_task(self, task: Task) -> str:
        pass