from datetime import datetime, timedelta

import pytest

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_mark_complete() -> None:
    task = Task("Morning walk", 20, "high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task() -> None:
    pet = Pet("Mochi", "dog")
    task = Task("Morning walk", 20, "high")
    initial_task_count = len(pet.tasks)

    pet.add_task(task)

    assert len(pet.tasks) == initial_task_count + 1


def test_scheduler_sorts_tasks_by_scheduled_time() -> None:
    later_task = Task("Walk", 20, "high", scheduled_time="09:00")
    earlier_task = Task("Breakfast", 10, "medium", scheduled_time="07:30")
    unscheduled_task = Task("Play", 15, "low")

    tasks = Scheduler().sort_by_time(
        [later_task, unscheduled_task, earlier_task]
    )

    assert tasks == [earlier_task, later_task, unscheduled_task]


def test_owner_get_tasks_filters_by_pet_and_completion() -> None:
    owner = Owner("Jordan")
    mochi = Pet("Mochi", "dog")
    completed_task = Task("Breakfast", 10, "medium")
    completed_task.mark_complete()
    incomplete_task = Task("Walk", 20, "high")
    mochi.add_task(completed_task)
    mochi.add_task(incomplete_task)

    luna = Pet("Luna", "cat")
    luna.add_task(Task("Play", 15, "low"))
    owner.add_pet(mochi)
    owner.add_pet(luna)

    assert owner.get_tasks(pet_name="mochi") == [
        completed_task,
        incomplete_task,
    ]
    assert owner.get_tasks(completed=True) == [completed_task]
    assert owner.get_tasks(pet_name="Mochi", completed=False) == [
        incomplete_task
    ]


def test_generate_schedule_remains_priority_based() -> None:
    owner = Owner("Jordan", available_minutes=30)
    pet = Pet("Mochi", "dog")
    low_priority_early = Task("Breakfast", 10, "low", scheduled_time="07:00")
    high_priority_late = Task("Walk", 20, "high", scheduled_time="09:00")
    pet.add_task(low_priority_early)
    pet.add_task(high_priority_late)
    owner.add_pet(pet)

    assert Scheduler().generate_schedule(owner) == [
        high_priority_late,
        low_priority_early,
    ]


@pytest.mark.parametrize(
    ("frequency", "days"),
    [("daily", 1), ("weekly", 7)],
)
def test_pet_completion_creates_next_recurring_occurrence(
    frequency: str,
    days: int,
) -> None:
    due_date = datetime(2026, 10, 9, 8, 30)
    task = Task(
        "Care task",
        20,
        "high",
        description="Care instructions",
        frequency=frequency,
        scheduled_time="08:30",
        due_date=due_date,
    )
    pet = Pet("Mochi", "dog")
    pet.add_task(task)

    next_task = pet.complete_task(task)

    assert task.completed is True
    assert next_task is not None
    assert next_task is not task
    assert next_task.completed is False
    assert next_task.due_date == due_date + timedelta(days=days)
    assert next_task.title == task.title
    assert next_task.duration_minutes == task.duration_minutes
    assert next_task.priority == task.priority
    assert next_task.description == task.description
    assert next_task.frequency == task.frequency
    assert next_task.scheduled_time == task.scheduled_time
    assert pet.tasks == [task, next_task]


def test_completing_recurring_task_twice_does_not_duplicate_occurrence() -> None:
    pet = Pet("Mochi", "dog")
    task = Task("Daily feeding", 5, "high", frequency="daily")
    pet.add_task(task)

    first_occurrence = pet.complete_task(task)
    second_result = pet.complete_task(task)

    assert first_occurrence is not None
    assert second_result is None
    assert pet.tasks == [task, first_occurrence]


def test_completing_one_time_task_does_not_repeat() -> None:
    pet = Pet("Mochi", "dog")
    task = Task("One-time checkup", 25, "medium")
    pet.add_task(task)

    next_task = pet.complete_task(task)

    assert task.completed is True
    assert next_task is None
    assert pet.tasks == [task]


def test_future_recurring_occurrence_is_not_scheduled_today() -> None:
    pet = Pet("Mochi", "dog")
    task = Task(
        "Daily feeding",
        5,
        "high",
        frequency="daily",
        due_date=datetime.now(),
    )
    pet.add_task(task)
    next_task = pet.complete_task(task)
    owner = Owner("Jordan", available_minutes=30)
    owner.add_pet(pet)

    assert next_task is not None
    assert Scheduler().generate_schedule(owner) == []


def test_scheduler_detects_same_time_conflicts_across_pets() -> None:
    due_date = datetime(2026, 10, 9)
    mochi = Pet("Mochi", "dog")
    mochi.add_task(
        Task("Morning walk", 20, "high", scheduled_time="08:00", due_date=due_date)
    )
    luna = Pet("Luna", "cat")
    luna.add_task(
        Task("Medication", 5, "high", scheduled_time="08:00", due_date=due_date)
    )
    owner = Owner("Jordan")
    owner.add_pet(mochi)
    owner.add_pet(luna)

    warnings = Scheduler().detect_conflicts(owner)

    assert len(warnings) == 1
    assert "08:00" in warnings[0]
    assert "Morning walk" in warnings[0]
    assert "Mochi" in warnings[0]
    assert "Medication" in warnings[0]
    assert "Luna" in warnings[0]


def test_scheduler_ignores_different_times_and_unscheduled_tasks() -> None:
    pet = Pet("Mochi", "dog")
    pet.add_task(Task("Breakfast", 10, "medium", scheduled_time="07:00"))
    pet.add_task(Task("Walk", 20, "high", scheduled_time="08:00"))
    pet.add_task(Task("Play", 15, "low"))
    owner = Owner("Jordan")
    owner.add_pet(pet)

    assert Scheduler().detect_conflicts(owner) == []


def test_scheduler_does_not_conflict_tasks_on_different_due_dates() -> None:
    mochi = Pet("Mochi", "dog")
    mochi.add_task(
        Task(
            "Morning walk",
            20,
            "high",
            scheduled_time="08:00",
            due_date=datetime(2026, 10, 9),
        )
    )
    luna = Pet("Luna", "cat")
    luna.add_task(
        Task(
            "Medication",
            5,
            "high",
            scheduled_time="08:00",
            due_date=datetime(2026, 10, 10),
        )
    )
    owner = Owner("Jordan")
    owner.add_pet(mochi)
    owner.add_pet(luna)

    assert Scheduler().detect_conflicts(owner) == []


def test_pet_cannot_complete_task_it_does_not_own() -> None:
    pet = Pet("Mochi", "dog")
    task = Task("Daily feeding", 5, "high", frequency="daily")

    with pytest.raises(ValueError, match="does not belong"):
        pet.complete_task(task)