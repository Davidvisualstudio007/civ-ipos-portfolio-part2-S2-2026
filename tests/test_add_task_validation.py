"""Tests for Issue #1: title and due date validation in add_task."""
import unittest
from unittest.mock import patch

from src.task import Task
from src.task_manager import add_task

FUTURE_DATE = "01-12-2099"


@patch("src.task_manager.save_tasks")
class TestAddTaskValidation(unittest.TestCase):
    """Check that add_task rejects bad input and accepts common date formats."""

    def setUp(self):
        """Start every test with an empty task list."""
        self.tasks = []

    def test_blank_title_is_rejected(self, mock_save):
        """An empty title should not create a task."""
        result = add_task(self.tasks, "", "Description", FUTURE_DATE)
        self.assertFalse(result)
        mock_save.assert_not_called()

    def test_whitespace_title_is_rejected(self, mock_save):
        """A title of only spaces should not create a task."""
        result = add_task(self.tasks, "    ", "Description", FUTURE_DATE)
        self.assertFalse(result)

    def test_duplicate_title_ignores_case(self, mock_save):
        """'Gym' and 'gym' count as the same task."""
        self.tasks.append(Task("Gym", "Legs", FUTURE_DATE))
        result = add_task(self.tasks, "gym", "Arms", FUTURE_DATE)
        self.assertFalse(result)

    def test_past_due_date_is_rejected(self, mock_save):
        """A task cannot be due before today."""
        result = add_task(self.tasks, "Old task", "Description", "01-01-1999")
        self.assertFalse(result)

    def test_slash_date_is_accepted(self, mock_save):
        """1/12/2099 is read day first and saved as 01-12-2099."""
        result = add_task(self.tasks, "Slash date", "Description", "1/12/2099")
        self.assertTrue(result)
        self.assertEqual(self.tasks[0].due_date, "01-12-2099")


if __name__ == "__main__":
    unittest.main()