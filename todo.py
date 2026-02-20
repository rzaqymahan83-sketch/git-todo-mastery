APP_NAME = "Todo CLI"
VERSION = "0.7.0"
AUTHOR = "Mahan"

def show_welcome():
    print("=" * 45)
    print(f"   {APP_NAME}   v{VERSION}".center(45))
    print(f"      Built by {AUTHOR}".center(45))
    print("=" * 45)
    print()


def show_menu():
    print("  Main Menu:")
    print("  1. Add new task")
    print("  2. Show all tasks")
    print("  3. Exit")
    print()


# _______________________________________
# Main Program
# _______________________________________

show_welcome()

while True:
    show_menu()
    choice = input("Your chocie (1-3): ").strip()

    if choice == "1":
        task = input("New task title: ").strip()
        if task:
            print(f"→ Task '{task}' added successfully (currently only displayed)")
        else:
            print("× Task title cannot be empty!")

    elif choice == "2":
        print("\nNo tasks have been added yet.\n")
    
    elif choice == "3":
        print("\nGoodbye! See you in the next session...\n")
        break
    
    else:
        print("× Invalid choice! Please enter 1, 2 or 3.\n")

    print("-" * 45)




tasks = []

def show_welcome():
    print("=" * 50)
    print(f"   {APP_NAME}  v{VERSION}".center(50))
    print(f"      Built by {AUTHOR}".center(50))
    print("=" * 50)
    print()


def show_menu():
    print("\nMain Menu:")
    print("  1. Add new task")
    print("  2. Show all tasks")
    print("  3. Exit")
    print()


def add_task():
    title = input("Enter new task title: ").strip()

    if not title:
        print("× Error: Task title cannot be empty!")
        return

    tasks.append(title)
    print(f"✓ Task added: '{title}'")


def show_tasks():
    if not tasks:
        print("\nNo tasks yet. Add your first task!\n")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"   {i}. {task}")
    print()


# _______________________________________
# Main Program
# _______________________________________

show_welcome()

while True:
    show_menu()
    choice = input("Your choice (1-3): ").strip()

    if choice == "1":
        add_task()

    elif chocie == "2":
        show_tasks()

    elif choice == "3":
        print("\nThank you for using Todo CLI. Goodbye!\n")
        break

    else:
        print("× Invalid option! Please enter 1, 2 or 3.")

    print("-" * 50)



tasks = []

def show_welcome():
    print("=" * 50)
    print(f"   {APP_NAME}  v{VERSION}".center(50))
    print(f"      Built by {AUTHOR}".center(50))
    print("=" * 50)
    print()


def show_menu():
    print("\nMain Menu:")
    print("  1. Add new task")
    print("  2. Show all tasks")
    print("  3. Clear all tasks")
    print("  4. Exit")
    print()


def add_task():
    title = input("Enter new task title: ").strip()

    if not title:
        print("× Error: task title cannot be empty!")
        return

    tasks.append(title)
    print(f"✓ Task added: '{title}'")


def show_tasks():
    if not tasks:
        print("\nNo tasks yet. Time to add some!\n")
        return

    print("\nYour current tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"   {index}. {task}")
    print(f"\nTotal tasks: {len(tasks)}\n")


def clear_all_tasks():
    if not tasks:
        print("→ No tasks to clear.\n")
        return

    confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()

    if confirm in ["yes", "y"]:
        tasks.clear()
        print("✓ All tasks have been cleared!\n")
    else:
        print("→ Operation cancelled.\n")


# _______________________________________
# Main Program
# _______________________________________

show_welcome()

while True:
    show_menu()
    chocie = input("Your choice (1-4): ").strip()
    
    if chocie == "1":
        add_task()

    elif chocie == "2":
        show_tasks()

    elif choice == "3":
        clear_all_tasks()
    
    elif chocie == "4":
        print("\nThank you for using Todo CLI. Goodbye!\n")
        break

    else:
        print("× Invalid option! Please enter 1, 2, 3 or 4.")

    print("-" * 50)


tasks = []


def show_welcome():
    print("=" * 50)
    print(f"   {APP_NAME}  v{VERSION}".center(50))
    print(f"      Built by {AUTHOR}".center(50))
    print("=" * 50)
    print()


def show_menu():
    print("\nMain Menu:")
    print("  1. Add new task")
    print("  2. Show all tasks")
    print("  3. Delete a task (by number)")
    print("  4. Clear all tasks")
    print("  5. Exit")
    print()
    

def add_task():
    title = input("Enter new task title: ").strip()

    if not title:
        print("× Error: Task title cannot be empty!")
        return

    # New structure: Dictionary for each task
    new_task = {
        "title": title,
        "done": False
    }

    tasks.append(new_task)
    print(f"✓ Task added: '{title}'")


def show_tasks():
    if not tasks:
        print("\nNo tasks yet. Add your first one!\n")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"  {i}. {status} {task['title']}")

    print(f"\nTotal: {len(tasks)} tasks\n")


def delete_task():
    if not tasks:
        print("→ No tasks to delete.\n")
        return

    show_tasks()

    try:
        num = input("Enter task number to delete: ").strip()
        index = int(num) - 1

        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"✓ Deleted:  '{deleted['title']}'")
        else:
            print("× Invalid task number!")

    except ValueError:
        print("× Please enter a valid number!")


def clear_all_tasks():
    if not tasks:
        print("→ Nothing to clear.\n")
        return

    confirm = input("Delete All tasks? (yes/no): ").strip().lower()
    if confirm in ["yes", "y"]:
        tasks.clear()
        print("✓ All tasks cleared!\n")
    else:
        print("→ Cancelled.\n")


# _______________________________________
# Main Program
# _______________________________________

show_welcome()

while True:
    show_menu()
    choice = input("Your choice (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice = "4":
        clear_all_tasks()
    elif choice == "5":
        print("\nThank you for using Todo CLI. Goodbye!\n")
        break
    else:
        print("× Invalid choice! Please select 1-5.")

    print("-" * 50)


PRIORITY_LEVELS = ("Low", "Medium", "High", "Urgent")

tasks = []


def show_welcome():
    print("=" * 60)
    print(f"   {APP_NAME}  v{VERSION}".center(60))
    print(f"      Built by {AUTHOR}".center(60))
    print("=" * 60)
    print()


def show_menu():
    print("\nMain Menu:")
    print("  1. Add new task")
    print("  2. Show all tasks (sorted by priority)")
    print("  3. Delete a task")
    print("  4. Clear all tasks")
    print("  5. Exit")
    print()


def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("× Title cannot be empty!")
        return

    print("\nPriority levels:", ", ".join(PRIORITY_LEVELS))
    while True:
        prio = input("Choose priority (Low/Medium/High/Urgent): ").strip().capitalize()
        if prio in PRIORITY_LEVELS:
            break
        print("× Invalid priority! Try again.")

    new_task = {
        "title": title,
        "priority": prio,
        "done": False,
        "created": "today"
    }

    tasks.append(new_task)
    print(f"✓ Added: {title}  [{prio}]")


def show_tasks():
    if not tasks:
        print("\nNo tasks yet.\n")
        return

    priority_order = {"Urgent": 0, "High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda t: priority_order.get(t["priority"], 999))

    print("\nYour tasks (sorted by priority):")
    for i, task in enumerate(sorted_tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"  {i}. {status} {task['title']}  →  {task['pririty']}")

    print(f"\nTotal: {len(tasks)} tasks\n")


def delete_task():
    if not tasks:
        print("→ No tasks to delete.\n")
        return

    show_tasks()
    try:
        num = int(input("Task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            deleted = tasks.pop(num)
            print(f"✓ Removed: {deleted['title']}")
        else:
            print("× Invalid number!")
    except ValueError:
        print("× Please enter a number!")


def clear_all_tasks():
    if not tasks:
        print("→ Nothing to clear.\n")
        return

    if input("Delete ALL? (yes/no): ").strip().lower() in ["yes", "y"]:
        tasks.clear()
        print("✓ Everything cleared!\n")
    else:
        print("→ Cancelled.\n")


# _______________________________________
# Main Program
# _______________________________________

show_welcome()

while True:
    show_menu()
    choice = input("Your choice (1-5): ").strip()

    if chocie == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif chocie == "3":
        delete_task()
    elif chocie == "4":
        clear_all_tasks()
    elif chocie == "5":
        print("\nGoodbye! See you next time.\n")
        break
    else:
        print("× Choose 1 to 5 please.")

    print("-" * 60)


tasks []


def show_welcome():
    print("=" * 70)
    line = f" {APP_NAME.upper()}  v{VERSION} ".center(68, "=")
    print(f"={line}=")
    print(f"      Built bt {AUTHOR}".center(70))
    print("=" * 70)
    print()


def show_menu():
    print("\n" + "=" * 30 + " MAIN MENU " + "=" * 30)
    print("  1. Add new task")
    print("  2. Show all tasks (sorted by priority)")
    print("  3. Search tasks by keyword")
    print("  4. Delete a task")
    print("  5. Clear all tasks")
    print("  6. Exit")
    print("=" * 70)


def add_task():
    title = input("Task title: ").strip()
    if not title:
        print("× Title cannot be empty!".center(70))
        return

    print("\nAvailable priorities:", ", ".join(PRIORITY_LEVELS))
    while True:
        prio_input = input("Priority: ").strip().title()
        if prio_input in PRIORITY_LEVELS:
            prio = prio_input
            break
        print("× Invalid priority. Please try again.")

    new_task = {
        "title": title,
        "priority": prio,
        "done": False,
        "created": "today"
    }

    tasks.append(new_task)
    print(f"\n✓ Task added successfully: {title!r} [{prio}]".center(70))


def show_tasks(filtered_tasks=None):
    to_show = filtered_tasks if filtered_tasks is not None else tasks

    if not to_show:
        print("\nNo tasks found.\n".center(70))
        return

    priority_order = {"Urgent":0, "High":1, "Medium":2, "Low":3}
    sorted_tasks = sorted(to_show, key=lambda t: priority_order.get(t["priority"], 999))

    print("\n" + "-" * 25 + " TASKS " + "-" * 25)
    for i, task in enumerate(sorted_tasks, 1):
        mark = "[✔]" if task["done"] else "[ ]"
        line = f"{i:2d}. {mark} {task['title']:<35}  {task['priority']:>8}"
        print(line)
    print("-" * 70)
    print(f"Total tasks: {len(to_show)}".rjust(70))


def search_tasks():
    if not tasks:
        print("\nThere are no tasks to search yet.\n")
        return

    keyword = input("Search keyword (in title): ").strip().lower()
    if not keyword:
        print("× Please enter a search term.")
        return

    results = [t for t in tasks if keyword in t["title"].lower()]

    print(f"\nSearch results for '{keyword}':")
    show_tasks(results)


def delete_task():
    if not tasks:
        print("→ No tasks to delete.\n")
        return

    show_tasks()
    try:
        num = input("\nTask number to delete → ").strip()
        idx = int(num) - 1
        if 0 <=idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"✓ Removed: {removed['title']!r}".center(70))
        else:
            print("× Invalid task number."center(70))
    except ValueError:
        print("× Please enter a valid number.".center(70))


def clear_all_tasks():
    if not tasks:
        print("→ No tasks to clear.\n")
        return

    ans = input("Delete ALL tasks? (yes/no): ").strip().lower()
    if ans in ("yes", "y"):
        tasks.clear()
        print("✓ All tasks have been deleted.".center(70))
    else:
        print("→ Operation cancelled.".center(70))


# _______________________________________
# Main Program
# _______________________________________

show_welcome()

while True:
    show_menu()
    chocie = input("→ Your choice (1-6): ").strip()

    if choice == "1":
        add_task()
    elif chocie == "2":
        show_tasks()
    elif choice == "3":
        search_tasks()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        clear_all_tasks()
    elif choice == "6":
        print("\n" + "=" * 30 + " GOODBYE " + "=" * 30 + "\n")
        break
    else:
        print("× Please select a number between 1 and 6.".center(70))

    print("-" * 70)