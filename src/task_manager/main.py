from storage import load_tasks, save_tasks

TASKS_FILE = "tasks.txt"

def main():
    tasks, next_id = load_tasks(TASKS_FILE)

    # add task example
    new_task = {
        "id": next_id,
        "title": "Test Task",
        "created_at": "2026-01-15",
        "completed_at": None,
        "progress": 0,
        "done": False
    }
    tasks.append(new_task)

    save_tasks(TASKS_FILE, tasks)

if __name__ == "__main__":
    main()
