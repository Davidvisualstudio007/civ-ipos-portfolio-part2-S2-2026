"""Unit tests for src/validators.py (Issue #1)."""
import unittest
from datetime import date

from src.task import Task
from src.validators import clean_title, parse_due_date

TODAY = date(2026, 10, 8)


class TestParseDueDate(unittest.TestCase):
    """Tests for parse_due_date using a fixed 'today'."""

    def test_standard_format(self):
        """DD-MM-YYYY still works."""
        self.assertEqual(parse_due_date("01-12-2026", today=TODAY), "01-12-2026")

    def test_past_date_raises(self):
        """A date before today raises ValueError."""
        with self.assertRaises(ValueError):
            parse_due_date("07-10-2026", today=TODAY)

    def test_garbage_raises(self):
        """Text that is not a date raises ValueError."""
        with self.assertRaises(ValueError):
            parse_due_date("next tuesday maybe", today=TODAY)

    def test_missing_day_raises(self):
        """'Dec 2026' has no day, so it is rejected."""
        with self.assertRaises(ValueError):
            parse_due_date("Dec 2026", today=TODAY)


class TestCleanTitle(unittest.TestCase):
    """Tests for clean_title."""

    def test_trims_spaces(self):
        """Spaces around the title are removed."""
        self.assertEqual(clean_title("  Shoot  ", []), "Shoot")

    def test_duplicate_raises(self):
        """A title already in the list, any case, raises ValueError."""
        existing = [Task("Shoot", "", "01-12-2099")]
        with self.assertRaises(ValueError):
            clean_title("SHOOT", existing)


if __name__ == "__main__":
    unittest.main()
