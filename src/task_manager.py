from rich.console import Console
from rich.table import Table
from rich.text import Text

from src.file_handler import save_tasks
from src.task import Task
from src.validators import clean_title, parse_due_date

# Shared console used to print tasks.
console = Console()

# Colour for each status in the table.
STATUS_COLOURS = {"pending": "yellow", "completed": "green"}


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


def complete_task(tasks, title):
    """
    Mark a task as completed.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): Title of the task to complete (case is ignored).

    Returns:
        bool: True if the task was found and updated, False otherwise.
    """
    wanted = (title or "").strip().lower()
    for task in tasks:
        if task.title.strip().lower() == wanted:
            task.status = "completed"
            save_tasks(tasks)
            return True
    return False


def build_task_table(tasks, status=None):
    """
    Build a rich Table of tasks, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): Only show tasks with this status.

    Returns:
        Table or None: The table, or None if no tasks match.
    """
    filtered = filter_tasks_by_status(tasks, status) if status else tasks
    if not filtered:
        return None

    table = Table(title="Tasks")
    table.add_column("#", justify="right")
    table.add_column("Title", style="bold")
    table.add_column("Description")
    table.add_column("Due")
    table.add_column("Status")

    for number, task in enumerate(filtered, start=1):
        colour = STATUS_COLOURS.get(task.status, "white")
        table.add_row(
            str(number),
            Text(task.title),
            Text(task.description),
            task.due_date,
            Text(task.status, style=colour),
        )
    return table


def list_tasks(tasks, status=None):
    """
    Print tasks as a coloured table, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter by.
    """
    table = build_task_table(tasks, status)
    if table is None:
        console.print("No tasks found.")
    else:
        console.print(table)


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
