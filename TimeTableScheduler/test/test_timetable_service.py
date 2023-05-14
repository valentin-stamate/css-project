import os
import unittest
from unittest.mock import MagicMock, mock_open, patch, call

from src.service.html_service import HTMLPage
from src.service.timetable_service import TimetableGenerator
from test.const.mock import TIMETABLE_MOCK_SMALL, MAIN_PAGE_MOCK, MOCK_STUDENT_PAGE_1, MOCK_STUDENT_PAGE_2, \
    MOCK_STUDENT_PAGE_3, MOCK_STUDENT_PAGE_4, MOCK_STUDENT_PAGE, MOCK_STUDENT_PAGE_5, MOCK_STUDENT_PAGE_6, \
    MOCK_PROFESSORS_PAGE_1, MOCK_PROFESSORS_PAGE_2, MOCK_PROFESSORS_PAGE_3, MOCK_PROFESSORS_PAGE, MOCK_ROOMS_PAGE_1, \
    MOCK_ROOMS_PAGE_2, MOCK_ROOMS_PAGE_3, MOCK_ROOMS_PAGE, MOCK_CLASSES_PAGE_1, MOCK_CLASSES_PAGE_2, \
    MOCK_CLASSES_PAGE_3, MOCK_CLASSES_PAGE


class TestTimetableGenerator(unittest.TestCase):

    def test_creating_the_folder(self):
        if os.path.exists('html/pages'):
            os.rmdir('html/pages')
        TimetableGenerator(TIMETABLE_MOCK_SMALL)

        self.assertEqual(os.path.exists('html/pages'), True)

    def test_categorize_by_year(self):
        result = TimetableGenerator.categorize_by_year(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], '1')
        self.assertEqual(sorted_keys[1], '2')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1], TIMETABLE_MOCK_SMALL[2]])

    def test_categorize_by_group_type(self):
        result = TimetableGenerator.categorize_by_group_type(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], '1A')
        self.assertEqual(sorted_keys[1], '2A')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1], TIMETABLE_MOCK_SMALL[2]])

    def test_categorize_by_group(self):
        result = TimetableGenerator.categorize_by_group(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 3)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], '1A1')
        self.assertEqual(sorted_keys[1], '2A1')
        self.assertEqual(sorted_keys[2], '2A4')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1]])
        self.assertEqual(result[sorted_keys[2]], [TIMETABLE_MOCK_SMALL[2]])

    def test_categorize_by_day(self):
        result = TimetableGenerator.categorize_by_day(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 3)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'Friday')
        self.assertEqual(sorted_keys[1], 'Monday')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[2]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[2]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_professor(self):
        result = TimetableGenerator.categorize_by_professor(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 3)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'Singh')
        self.assertEqual(sorted_keys[1], 'Smith')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[2]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[2]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_rooms(self):
        result = TimetableGenerator.categorize_by_rooms(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 3)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'A101')
        self.assertEqual(sorted_keys[1], 'A103')
        self.assertEqual(sorted_keys[2], 'C302')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[2]])
        self.assertEqual(result[sorted_keys[2]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_class(self):
        result = TimetableGenerator.categorize_by_class(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 3)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'Data Structures and Algorithms')
        self.assertEqual(sorted_keys[1], 'Database Systems')
        self.assertEqual(sorted_keys[2], 'Introduction to Programming')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[1]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[2]])
        self.assertEqual(result[sorted_keys[2]], [TIMETABLE_MOCK_SMALL[0]])

    def test_transform_for_timetable(self):
        mock_lambda = MagicMock(return_value='')

        result = TimetableGenerator.transform_for_timetable(TIMETABLE_MOCK_SMALL, mock_lambda)
        self.assertEqual(result, [['Monday'], '', ['Wednesday'], '', ['Friday'], ''])

    def test_generate_main_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()

        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_main_page()

            mock_file_open.assert_called_once_with('./html/index.html', 'wt')

            handle = mock_file_open()
            handle.close.assert_called_once()
            handle.write.assert_called_once_with(MAIN_PAGE_MOCK)

    def test_generate_student_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()
        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_student_page()

            self.assertEqual(mock_file_open.call_count, 7)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 7)
            self.assertEqual(handle.write.call_count, 7)

            self.assertEqual(handle.write.mock_calls[0], call(MOCK_STUDENT_PAGE_1))
            self.assertEqual(handle.write.mock_calls[1], call(MOCK_STUDENT_PAGE_2))
            self.assertEqual(handle.write.mock_calls[2], call(MOCK_STUDENT_PAGE_3))
            self.assertEqual(handle.write.mock_calls[3], call(MOCK_STUDENT_PAGE_4))
            self.assertEqual(handle.write.mock_calls[4], call(MOCK_STUDENT_PAGE_5))
            self.assertEqual(handle.write.mock_calls[5], call(MOCK_STUDENT_PAGE_6))
            self.assertEqual(handle.write.mock_calls[6], call(MOCK_STUDENT_PAGE))

    def test_generate_professors_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()
        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_professors_page()

            self.assertEqual(mock_file_open.call_count, 4)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 4)
            self.assertEqual(handle.write.call_count, 4)

            self.assertEqual(handle.write.mock_calls[0], call(MOCK_PROFESSORS_PAGE_1))
            self.assertEqual(handle.write.mock_calls[1], call(MOCK_PROFESSORS_PAGE_2))
            self.assertEqual(handle.write.mock_calls[2], call(MOCK_PROFESSORS_PAGE_3))
            self.assertEqual(handle.write.mock_calls[3], call(MOCK_PROFESSORS_PAGE))

    def test_generate_rooms_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()

        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_rooms_page()

            self.assertEqual(mock_file_open.call_count, 4)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 4)
            self.assertEqual(handle.write.call_count, 4)

            self.assertEqual(handle.write.mock_calls[0], call(MOCK_ROOMS_PAGE_1))
            self.assertEqual(handle.write.mock_calls[1], call(MOCK_ROOMS_PAGE_2))
            self.assertEqual(handle.write.mock_calls[2], call(MOCK_ROOMS_PAGE_3))
            self.assertEqual(handle.write.mock_calls[3], call(MOCK_ROOMS_PAGE))

    def test_generate_classes_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()

        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_classes_page()

            self.assertEqual(mock_file_open.call_count, 4)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 4)
            self.assertEqual(handle.write.call_count, 4)

            self.assertEqual(handle.write.mock_calls[0], call(MOCK_CLASSES_PAGE_1))
            self.assertEqual(handle.write.mock_calls[1], call(MOCK_CLASSES_PAGE_2))
            self.assertEqual(handle.write.mock_calls[2], call(MOCK_CLASSES_PAGE_3))
            self.assertEqual(handle.write.mock_calls[3], call(MOCK_CLASSES_PAGE))

    def test_generate_all(self):
        timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
        timetable_generator.generate_main_page = MagicMock(return_value=None)
        timetable_generator.generate_classes_page = MagicMock(return_value=None)
        timetable_generator.generate_student_page = MagicMock(return_value=None)
        timetable_generator.generate_professors_page = MagicMock(return_value=None)
        timetable_generator.generate_rooms_page = MagicMock(return_value=None)

        timetable_generator.generate_all()

        timetable_generator.generate_main_page.assert_called_once()
        timetable_generator.generate_classes_page.assert_called_once()
        timetable_generator.generate_student_page.assert_called_once()
        timetable_generator.generate_professors_page.assert_called_once()
        timetable_generator.generate_rooms_page.assert_called_once()
