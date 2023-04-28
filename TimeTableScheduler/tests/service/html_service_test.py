import unittest

from src.service.html_service import TimetablePage
from src.service.timetable_service import TimetableGenerator
from tests.mock import MOCK_STUDENT_TIMETABLE, TIMETABLE_MOCK


class TestTimetablePage(unittest.TestCase):
    pass
    # def test_generate_html(self):
    #     title = "Timetable test"
    #     data = [
    #         ['Head 1', 'Head 2', 'Head 3', 'Head 4', 'Head 5'],
    #         ['Day 1'],
    #         ['12', '14', 'Name', 'Author', 'C102'],
    #         ['Day 2'],
    #         ['12', '14', 'Name', 'Author', 'C102'],
    #     ]
    #
    #     timetable = TimetablePage(title, data, 5, 'test_timetable.html')
    #     html = timetable.generate_html()
    #
    #     assert title in html
    #     assert MOCK_STUDENT_TIMETABLE in html


class TestTimetableService(unittest.TestCase):

    def test_generate_all_timetables(self):
        timetable_service = TimetableGenerator(TIMETABLE_MOCK)

        timetable_service.generate_all()

    def test_main_page_generation(self):
        timetable_service = TimetableGenerator(TIMETABLE_MOCK)

        timetable_service.generate_main_page()

    def test_students_page_generation(self):
        timetable_service = TimetableGenerator(TIMETABLE_MOCK)

        timetable_service.generate_student_page()

    def test_professors_page_generation(self):
        timetable_service = TimetableGenerator(TIMETABLE_MOCK)

        timetable_service.generate_professors_page()

    def test_rooms_page_generation(self):
        timetable_service = TimetableGenerator(TIMETABLE_MOCK)

        timetable_service.generate_rooms_page()

    def test_classes_page_generation(self):
        timetable_service = TimetableGenerator(TIMETABLE_MOCK)

        timetable_service.generate_classes_page()
