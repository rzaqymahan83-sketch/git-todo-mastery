from data import tasks, PRIORITY_LEVELS, creat_task, add_task_to_list, get_sorted_tasks
from ui import show_tasks


def add_task():
    from ui import show_message
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
    show_message(f"✓ Added: {title} [{prio}]")


def mark_as_done():
    from ui import show_tasks, show_message
    if not tasks:
        show_message("→ No tasks to mark.")
        return

    show_tasks(get_sorted_tasks())
    try:
        num = int(input("Task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            show_message(f"✓ Marked: {tasks[num]['title']}")
        else:
            show_message("× Invalid number.")
    except ValueError:
        show_message("× Enter a number.")


def edit_task_title():
    from ui import show_tasks, show_message
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
                show_message(f"✓ Updated: {new_title}")
            else:
                show_message("× Title cannot be empty. Edit cancelled.")
        else:
            show_message("× Invalid number.")
    except ValueError:
        show_message("× Enter a number.")


def delete_task():
    from ui import show_tasks, show_message
    if not tasks:
        show_message("→ No tasks to delete.")
        return

    show_tasks(get_sorted_tasks())
    try:
        num = int(input("Task numer to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            show_message(f"✓ Removed: {removed['title']}")
        else:
            show_message("× Invalid number.")
    except ValueError:
        show_message("× Enter a number.")


def clear_all():
    from ui import show_message
    if not tasks:
        show_message("→ Nothing to clear.")
        return

    ans = input("Delete ALL? (yes/no): ").strip().lower()
    if ans in ("yes", "y"):
        tasks.clear()
        show_message("✓ All tasks cleared.")
    else:
        show_message("→ Cancelled.")