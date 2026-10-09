import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state["owner"] = Owner("Jordan")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

Use this app to manage pets, add their care tasks, and generate a schedule based on priority
and available time.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

The scheduling UI uses the PawPal+ classes and scheduling logic.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner and Pet Profiles")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
owner = st.session_state["owner"]
owner.name = owner_name

if st.button("Add pet"):
    if any(pet.name == pet_name for pet in owner.pets):
        st.warning(f"{pet_name} is already in your pet list.")
    else:
        owner.add_pet(Pet(pet_name, species))
        st.success(f"Added {pet_name}.")

if owner.pets:
    st.write("Current pets:")
    st.table([{"Name": pet.name, "Species": pet.species} for pet in owner.pets])

st.markdown("### Tasks")
st.caption("Add care tasks to one of your pets.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if owner.pets:
    selected_pet_name = st.selectbox(
        "Assign task to",
        [pet.name for pet in owner.pets],
    )
    if st.button("Add task"):
        selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)
        selected_pet.add_task(
            Task(task_title, int(duration), priority)
        )
        st.success(f"Added {task_title} for {selected_pet.name}.")
else:
    st.info("Add a pet before adding care tasks.")

tasks = [
    {
        "Pet": pet.name,
        "Task": task.title,
        "Duration (minutes)": task.duration_minutes,
        "Priority": task.priority,
        "Completed": task.completed,
    }
    for pet in owner.pets
    for task in pet.tasks
]
if tasks:
    st.write("Current tasks:")
    st.table(tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a daily schedule using task priorities and available time.")
owner.available_minutes = st.number_input(
    "Available time (minutes)",
    min_value=0,
    max_value=1440,
    value=max(0, owner.available_minutes),
)
scheduler = Scheduler()

if st.button("Generate schedule"):
    schedule = scheduler.generate_schedule(owner)
    if schedule:
        pet_names_by_task_id = {
            id(task): pet.name
            for pet in owner.pets
            for task in pet.tasks
        }
        st.write("Today's Schedule:")
        st.table(
            [
                {
                    "Pet": pet_names_by_task_id[id(task)],
                    "Task": task.title,
                    "Duration (minutes)": task.duration_minutes,
                    "Priority": task.priority,
                    "Reason": scheduler.explain_task(task),
                }
                for task in schedule
            ]
        )
    else:
        st.info("No unfinished tasks fit within the available time.")
