def print_header(title, width=70):
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def show_welcome(app_name, version, author):
    print_header(f" {app_name.upper()}  v{version} ")
    print(f"      Built by {author}".center(70))
    print("=" * 70)
    print()


def show_main_menu():
    print("\n" + "-" * 25 + " MAIN MENU " + "-" * 25)
    print("  1. Add new task")
    print("  2. Show all tasks (sorted)")
    print("  3. Search tasks by keyword")
    print("  4. Mark task as done")
    print("  5. Edit task title")
    print("  6. Delete a task")
    print("  7. Clear all tasks")
    print("  8. View task details.")
    print("  9. Exit (or press Enter)")
    print("-" * 70)


def get_choice():
    return input("→ Your choice (1-8 or Enter to exit): ").strip()


def show_tasks(tasks_list):
    if not tasks_list:
        print("\nNo tasks yet.\n".center(70))
        return

    print("\n" + "-" * 20 + " TASKS " + "-" * 20)
    for i, t in enumerate(tasks_list, 1):
        mark = "[✔]" if t["done"] else "[ ]"
        print(f"{i:2d}. {mark} {t['title']:<40} {t['priority']:>5}")
    print("-" * 70)
    print(f"Total: {len(tasks_list)}".rjust(70))


def show_message(msg, center=True):
    if center:
        print(msg.center(70))
    else:
        print(msg)
