from datetime import datetime


class Task:
    """Represents a single todo task."""

    def __int__(self, title, priority, done=False):
        """Initialize a new task."""
        self.title = title.strip()
        self.priority = priority
        self.done = done
        self.created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_done(self):
        """Mark the task as completed."""
        self.done = True

    def edit_title(self, new_title):
        """Change the task title."""
        if new_title.strip():
            self.title = new_title.strip()
            return True
        return False

    def __str__(self):
        """String representation for printing."""
        status = "✔ Done" if self.done else "Pending"
        return f"{self.title}  |  {self.priority}  |  {status}  |  Created: {self.created}"
    
    def to_dict(self):
        """Convert task to dictionary for JSON saving."""
        return {
            "title": self.title,
            "priority": self.priority,
            "done": self.done,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data):
        """Creat Task from dictionary (for loading from JSON)."""
        return cls(
            title=data["title"],
            priority=data["priority"],
            done=data["done"]
        )