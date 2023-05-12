import unittest

from src.service.timetable_service import TimetableGenerator
from test.const.mock import TIMETABLE_MOCK


class TestTimetablePage(unittest.TestCase):

    def test_demo(self):
        pass


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
