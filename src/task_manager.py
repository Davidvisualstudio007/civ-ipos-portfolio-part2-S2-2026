from src.file_handler import save_tasks
from src.task import Task
from src.validators import clean_title, parse_due_date


def add_task(tasks, title, description, due_date):
    """
    Add a new task after validating the title and due date.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The task title. Blank or duplicate titles are rejected.
        description (str): A brief description of the task.
        due_date (str): The due date, e.g. '01-12-2030' or '1 Dec 2030'.
            Stored as 'DD-MM-YYYY'. Cannot be in the past.

    Returns:
        bool: True if the task is added, False otherwise.

    Side Effects:
        - Prints an error message if the input is rejected.
        - Saves the task list using `save_tasks`.
    """
    try:
        title = clean_title(title, tasks)
        due_date = parse_due_date(due_date)
    except ValueError as error:
        print(f"Error: {error}")
        return False

    tasks.append(Task(title, description, due_date))
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def list_tasks(tasks, status=None):
    """
    Display tasks in the task list, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter tasks
        by (e.g., "pending" or "completed").

    Returns:
        None

    Side Effects:
        - Prints the list of tasks to the console.
    """
    if not status:
        # If status is not set
        filtered = tasks
    else:
        # Filter tasks based on their status
        filtered = []
        for task in tasks:
            if task.status == status:
                filtered.append(task)

    if not filtered:
        print("No tasks found.")
        return
    for task in filtered:
        print(
            f"{task.title} | {task.description} | "
            f"Due: {task.due_date} | Status: {task.status}"
        )


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]
