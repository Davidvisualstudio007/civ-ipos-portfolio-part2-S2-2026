"""Tests for Issue #2: rich table, status filter and completing tasks."""
import unittest
from unittest.mock import patch

from rich.console import Console

import main
from src.task import Task
from src.task_manager import build_task_table, complete_task, list_tasks

FUTURE = "01-12-2099"


def render(table):
    """Turn a rich table into plain text so tests can check it."""
    console = Console(record=True, width=120)
    console.print(table)
    return console.export_text()


class TestBuildTaskTable(unittest.TestCase):
    """Tests for build_task_table."""

    def setUp(self):
        """Create one pending and one completed task."""
        self.tasks = [
            Task("Edit reel", "Cut 30s version", FUTURE, "pending"),
            Task("Invoice client", "Send invoice", FUTURE, "completed"),
        ]

    def test_table_shows_all_tasks(self):
        """Both tasks and the headers appear in the table."""
        text = render(build_task_table(self.tasks))
        self.assertIn("Title", text)
        self.assertIn("Status", text)
        self.assertIn("Edit reel", text)
        self.assertIn("Invoice client", text)

    def test_filter_by_status(self):
        """Filtering by 'completed' hides pending tasks."""
        text = render(build_task_table(self.tasks, status="completed"))
        self.assertIn("Invoice client", text)
        self.assertNotIn("Edit reel", text)

    def test_empty_list_returns_none(self):
        """No table is built when nothing matches."""
        self.assertIsNone(build_task_table([]))


class TestListTasks(unittest.TestCase):
    """Tests for list_tasks."""

    @patch("src.task_manager.console")
    def test_empty_message(self, mock_console):
        """An empty list prints a friendly message."""
        list_tasks([])
        mock_console.print.assert_called_once_with("No tasks found.")


@patch("src.task_manager.save_tasks")
class TestCompleteTask(unittest.TestCase):
    """Tests for complete_task."""

    def test_marks_completed(self, mock_save):
        """The task becomes 'completed' and the list is saved."""
        tasks = [Task("Edit reel", "", FUTURE)]
        self.assertTrue(complete_task(tasks, "edit reel"))
        self.assertEqual(tasks[0].status, "completed")
        mock_save.assert_called_once_with(tasks)

    def test_unknown_title(self, mock_save):
        """Returns False and saves nothing if the title is not found."""
        self.assertFalse(complete_task([], "Nope"))
        mock_save.assert_not_called()


class TestMenu(unittest.TestCase):
    """Tests for the menu in main.py."""

    @patch("main.list_tasks")
    @patch("main.load_tasks", return_value=[])
    @patch("builtins.input", side_effect=["3", "completed", "5"])
    def test_list_passes_filter(self, _input, _load, mock_list):
        """Choosing List then typing 'completed' filters by that status."""
        main.main()
        mock_list.assert_called_once_with([], "completed")


if __name__ == "__main__":
    unittest.main()