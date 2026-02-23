tasks = []

PRIORITY_LEVELS = ("Low", "Meduim", "High", "Urgent")


def creat_task(title, priority):
    return {
        "title": title,
        "priority": priority,
        "done": False,
        "created": "today"
    }


def add_task_to_list(task_dict):
    tasks.append(task_dict)


def get_sorted_tasks():
    order = {"Urgent": 0, "High": 1, "Medium": 2, "Low": 3}
    return sorted(tasks, key=lambda t: order.get(t["priority"], 999))