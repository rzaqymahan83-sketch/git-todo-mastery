import json
import os
from task import Task


class TodoManager:
    """Manages the collection of tasks with persistence"""

    PRIORITY_LEVELS = ("Low", "Medium", "High", "Urgent")
    DATA_FILE = "tasks.json"

    def __init__(self):
        """Initialize manager and load tasks."""
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file."""
        if not os.path.exists(self.DATA_FILE):
            print("No saved tasks found. Starting fresh.")
            return

        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
            print(f"✓ Loaded {len(self.tasks)} tasks from file.")
        except Exception as e:
            print(f"× Error loading tasks: {e}")
            self.tasks = []

    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            data = [t.to_dict() for t in self.tasks]
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("✓ Tasks saved successfully.")
        except Exception as e:
            print(f"× Failed to save: {e}")

    def add_task(self, title, priority):
        """Add a new task."""
        if priority not in self.PRIORITY_LEVELS:
            raise ValueError("Invalid priority")
        new_task = Task(title, priority)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def get_sorted_tasks(self):
        """Return tasks sorted by priority."""
        order = {"Urgent": 0, "High": 1, "Medium": 2, "Low": 3}
        return sorted(self.tasks, key=lambda t: order.get(t.priority, 999))

    def mark_done(self, index):
        """Mark task at index as done."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save_tasks()
            return True
        return False

    def edit_title(self, index, new_title):
        """Edit task title at index."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index].edit_title(new_title)
        return False

    def delete_task(self, index):
        """Delete task at index."""
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            return removed
        return None

    def clear_all(self):
        """Remove all tasks."""
        self.tasks.clear()
        self.save_tasks()

    def view_task(self, index):
        """Get task at index for details."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None
