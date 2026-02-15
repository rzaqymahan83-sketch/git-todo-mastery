APP_NAME = "Todo CLI"
VERSION = "0.2.0"
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
            print(f"-> Task '{task}' added successfully (currently only displayed)")
        else:
            print("x Task title cannot be empty!")

    elif choice == "2":
        print("\nNo tasks have been added yet.\n")
    
    elif choice == "3":
        print("\nGoodbye! See you in the next session...\n")
        break
    
    else:
        print("x Invalid choice! Please enter 1, 2 or 3.\n")

    print("-" * 45)
    