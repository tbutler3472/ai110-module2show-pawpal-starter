from pawpal_system import Pet, Task


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