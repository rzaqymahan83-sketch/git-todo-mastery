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


import json
import os

tasks = []
PRIORITY_LEVELS = ("Low", "Medium", "High", "Urgent")
DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from 'tasks.json' file into the global tasks list.

    If file doesn't exist or is invalid, starts with an empty list.
    """
    global tasks

    if not os.path.exists(DATA_FILE):
        tasks = []
        print("No saved tasks found. Starting fresh.")
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
        print(f"✓ Loaded {len(tasks)} tasks from file.")
    except json.JSONDecodeError:
        print("× Invalid JSON format in tasks.json → starting with empty list")
        tasks = []
    except Exception as e:
        print(f"× Error loading tasks: {e}")
        tasks = []


def save_tasks():
    """Save current tasks list to 'tasks.json' file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
        print("✓ Tasks saved successfully.")
    except Exception as e:
        print(f"× Failed to save tasks: {e}")


def creat_task(title, priority):
    """Create a new task dictionary."""
    return {
        "title": title,
        "priority": priority,
        "done": False,
        "created": "today"
    }


def add_task_to_list(task_dict):
    """Add a task dictionary to the tasks list."""
    tasks.append(task_dict)


def get_sorted_tasks():
    """Return tasks sorted by priority (highest to lowest)."""
    order = {"Urgent": 0, "Hight": 1, "Medium": 2, "Low": 3}
    return sorted(tasks, key=lambda t: order.get(t["priority"], 999))