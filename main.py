"""Entry point for the Task Manager CLI."""
from src.file_handler import load_tasks
from src.task_manager import add_task, complete_task, delete_task, list_tasks

EXIT_CHOICE = "5"


def handle_add(tasks):
    """Ask for task details and add the task."""
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due Date (e.g. 01-12-2030 or 1 Dec 2030): ")
    if add_task(tasks, title, description, due_date):
        print("Task added successfully.")


def handle_delete(tasks):
    """Ask for a title and delete that task."""
    title = input("Title of the task to delete: ")
    if delete_task(tasks, title):
        print("Task deleted successfully.")
    else:
        print("Task not found.")


def handle_list(tasks):
    """Ask for an optional status filter, then show the table."""
    status = input("Filter by status (pending/completed, blank for all): ")
    list_tasks(tasks, status.strip().lower() or None)


def handle_complete(tasks):
    """Ask for a title and mark that task as completed."""
    title = input("Title of the task to complete: ")
    if complete_task(tasks, title):
        print("Task marked as completed.")
    else:
        print("Task not found.")


# Menu number -> (label, function to run).
MENU = {
    "1": ("Add Task", handle_add),
    "2": ("Delete Task", handle_delete),
    "3": ("List Tasks", handle_list),
    "4": ("Mark Task Complete", handle_complete),
}


def main():
    """Run the menu until the user chooses Exit."""
    tasks = load_tasks()
    while True:
        print("\nTask Manager CLI")
        for key, (label, _handler) in MENU.items():
            print(f"{key}. {label}")
        print(f"{EXIT_CHOICE}. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == EXIT_CHOICE:
            print("Exiting Task Manager.")
            break
        if choice not in MENU:
            print("Invalid choice. Try again.")
            continue
        _label, handler = MENU[choice]
        handler(tasks)


if __name__ == "__main__":
    main()
