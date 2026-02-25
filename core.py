from data import tasks, PRIORITY_LEVELS, creat_task, add_task_to_list, get_sorted_tasks
from ui import show_tasks, show_message


def add_task():
    """Add a new task to the list"""
    try:
        title = input("Task title: ").strip()
        if not title:
            show_message("× Title cannot be empty!")
            return
        
        print("Priorities:", ", ".join(PRIORITY_LEVELS))
        prio = ""
        while prio not in PRIORITY_LEVELS:
            prio = input("Priority: ").strip().title()
            if prio not in PRIORITY_LEVELS:
                print("× Invalid priority.")

        new_task = creat_task(title, prio)
        add_task_to_list(new_task)
        saved_tasks()
        show_message(f"✓ Added and saved: {title} [{prio}]")


def mark_as_done():
    """Mark a task as completed."""
    if not tasks:
        show_message("→ No tasks to mark.")
        return

    show_tasks(get_sorted_tasks())
    try:
        num = int(input("Task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            save_tasks()
            show_message(f"✓ Marked and saved: {tasks[num]['title']}")
        else:
            show_message("× Invalid task number.")
    except ValueError:
        show_message("× Please enter a valid number.")
    except Exception as e:
        show_message(f"× Error: {e}")


def edit_task_title():
    """Edit the title of an existing task."""
    if not tasks:
        show_message("→ No tasks to edit.")
        return

    show_tasks(get_sorted_tasks())
    try:
        num = int(input("Turn number to edit: ")) - 1
        if 0 <= num < len(tasks):
            old_title = tasks[num]["title"]
            new_title = input(f"New title (was: {old_title}): ").strip()
            if new_title:
                tasks[num]["title"] = new_title
                save_tasks()
                show_message(f"✓ Updated and saved: {new_title}")
            else:
                show_message("× Title cannot be empty. Edit cancelled.")
        else:
            show_message("× Invalid task number.")
    except ValueError:
        show_message("× Please enter a valid number.")
    except Exception as e:
        show_message(f"× Error during edit: {e}")


def delete_task():
    """Delete a task from the list."""
    if not tasks:
        show_message("→ No tasks to delete.")
        return

    show_tasks(get_sorted_tasks())
    try:
        num = int(input("Task numer to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks()
            show_message(f"✓ Removed and saved: {removed['title']}")
        else:
            show_message("× Invalid number.")
    except ValueError:
        show_message("× Please enter a valid number.")
    except Exception as e:
        show_message(f"× Error: {e}")


def clear_all():
    """Clear all tasks after confirmation"""
    if not tasks:
        show_message("→ Nothing to clear.")
        return
    try:
        confirm = input("Delete ALL tasks? (yes/no): ").strip().lower()
        if confirm in ("yes", "y"):
            tasks.clear()
            save_tasks()
            show_message("✓ All tasks cleared and saved.")
        else:
            show_message("→ Cancelled.")
    except KeyboardInterrupt:
        show_message("→ Cancelled.")
    except Exception as e:
        show_message(f"× Error: {e}")


def view_task_details():
    """Show detailed information about a specific task."""
    if not tasks:
        show_message("→ No tasks available.")
        return

    show_tasks(get_sorted_tasks())
    try:
        num = input("Enter task number to view details: ").strip()
        index = int(num) - 1
        if 0 <= index < len(tasks):
            t = tasks[index]
            print("\n" + "-" * 40 + " TASK DETAILS " + "-" * 40)
            print(f"Title     : {t['title']}")
            print(f"Priority  : {t['priority']}")
            print(f"Status    : {'Done' if t['done'] else 'Pending'}")
            print(f"Created   : {t['created']}")
            print("-" * 90)
        else:
            show_message("× Invalid task number.")
    except ValueError:
        show_message("× Please enter a valid number.")
    except Exception as e:
        show_message(f"× Error displaying details: {e}")