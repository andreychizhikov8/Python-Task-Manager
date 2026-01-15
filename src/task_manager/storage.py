def load_tasks(path):
    tasks = []
    next_id = 1
    if path == None:
        return tasks, next_id
    with open("tasks.json", "r", encoding="utf-8") as file:
        for line in file:
            id_str, title, created_at_str, completed_at_str, progress_str, done_str = line.strip().split(";")
            task = {
                "id": int(id_str),
                "title": title,
                "created_at": int(created_at_str),
                "completed_at": int(completed_at_str),
                "progress": int(progress_str),
                "done": done_str == "true"
            }
            tasks.append(task)
            next_id += 1
    return tasks, next_id


def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        for task in tasks:
            line = (
                 f"{task['id']};"
                 f"{task['title']};"
                 f"{task['created_at']};"
                 f"{task['completed_at']};"
                 f"{task['progress']};" 
                 f"{task['done']}\n"
            )
            file.write(line)













