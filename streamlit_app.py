import streamlit as st
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Initialize
tasks = load_tasks()

st.title("📝 Task Manager")

# -------------------------
# ADD TASK
# -------------------------
st.subheader("➕ Add Task")

task_name = st.text_input("Enter task")

if st.button("Add Task"):
    if task_name.strip() != "":
        tasks.append({"name": task_name, "done": False})
        save_tasks(tasks)
        st.success("Task added!")
        st.rerun()
    else:
        st.warning("Please enter a task")

# -------------------------
# VIEW & UPDATE TASKS
# -------------------------
st.subheader("📋 Your Tasks")

if not tasks:
    st.info("No tasks yet")
else:
    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([5, 2, 2])

        # Task name + checkbox
        with col1:
            updated_status = st.checkbox(
                task["name"],
                value=task["done"],
                key=f"check_{i}"
            )

            if updated_status != task["done"]:
                tasks[i]["done"] = updated_status
                save_tasks(tasks)
                st.rerun()

        # Status display
        with col2:
            if task["done"]:
                st.write("✅ Done")
            else:
                st.write("❌ Pending")

        # Delete button
        with col3:
            if st.button("Delete", key=f"del_{i}"):
                tasks.pop(i)
                save_tasks(tasks)
                st.rerun()


