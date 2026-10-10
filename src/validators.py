"""Reusable input validators for the Task Manager CLI.

Uses python-dateutil to read dates in everyday formats
(01-12-2030, 1/12/2030, 1 Dec 2030).
"""
from datetime import date, datetime

from dateutil import parser

DATE_FORMAT = "%d-%m-%Y"

# dateutil fills in missing parts of a date from a default.
# Parsing with two different defaults shows if something was missing.
_DEFAULT_A = datetime(2000, 1, 1)
_DEFAULT_B = datetime(2001, 2, 2)


def parse_due_date(text, today=None):
    """Parse a due date and return it as DD-MM-YYYY.

    Args:
        text (str): The date as typed, e.g. "1/12/2030" or "1 Dec 2030".
        today (datetime.date, optional): Date to compare against.
            Defaults to the real date. Tests pass a fixed one.

    Returns:
        str: The date in DD-MM-YYYY format.

    Raises:
        ValueError: If the date is invalid, incomplete or in the past.
    """
    if today is None:
        today = date.today()
    text = (text or "").strip()

    try:
        first = parser.parse(text, dayfirst=True, default=_DEFAULT_A)
        second = parser.parse(text, dayfirst=True, default=_DEFAULT_B)
    except (ValueError, OverflowError) as error:
        raise ValueError(f"'{text}' is not a valid date.") from error

    if first != second:
        raise ValueError("Due date must include a day, month and year.")
    if first.date() < today:
        raise ValueError("Due date cannot be in the past.")
    return first.strftime(DATE_FORMAT)


def clean_title(title, tasks):
    """Trim a title and check it is not blank or a duplicate.

    Args:
        title (str): The title as typed.
        tasks (list): Existing Task objects.

    Returns:
        str: The trimmed title.

    Raises:
        ValueError: If the title is blank or already exists (any case).
    """
    cleaned = (title or "").strip()
    if not cleaned:
        raise ValueError("Title cannot be empty.")
    if any(task.title.strip().lower() == cleaned.lower() for task in tasks):
        raise ValueError("A task with this title already exists.")
    return cleaned
