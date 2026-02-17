APP_NAME = "Todo CLI"
VERSION = "0.4.0"
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
    # Use for + enumerate for numbered display
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