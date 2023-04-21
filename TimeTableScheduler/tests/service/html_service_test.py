import unittest

from src.service.html_service import TimetablePage
from tests.mock import MOCK_STUDENT_TIMETABLE


class TestTimetablePage(unittest.TestCase):

    def test_generate_html(self):
        title = "Timetable test"
        data = [
            ['Head 1', 'Head 2', 'Head 3', 'Head 4', 'Head 5'],
            ['Day 1'],
            ['12', '14', 'Name', 'Author', 'C102'],
            ['Day 2'],
            ['12', '14', 'Name', 'Author', 'C102'],
        ]

        timetable = TimetablePage(title, data, 5)
        html = timetable.generate_html()

        assert title in html
        assert MOCK_STUDENT_TIMETABLE in html
