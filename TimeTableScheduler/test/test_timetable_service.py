import os
import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.service.html_service import HTMLPage
from src.service.timetable_service import TimetableGenerator
from test.const.mock import TIMETABLE_MOCK_SMALL, MAIN_PAGE_MOCK


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
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_group_type(self):
        result = TimetableGenerator.categorize_by_group_type(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], '1A')
        self.assertEqual(sorted_keys[1], '2A')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_group(self):
        result = TimetableGenerator.categorize_by_group(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], '1A1')
        self.assertEqual(sorted_keys[1], '2A4')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_day(self):
        result = TimetableGenerator.categorize_by_day(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'Friday')
        self.assertEqual(sorted_keys[1], 'Monday')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[1]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[0]])

    def test_categorize_by_professor(self):
        result = TimetableGenerator.categorize_by_professor(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'Singh')
        self.assertEqual(sorted_keys[1], 'Smith')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[1]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[0]])

    def test_categorize_by_rooms(self):
        result = TimetableGenerator.categorize_by_rooms(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'A101')
        self.assertEqual(sorted_keys[1], 'A103')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[0]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[1]])

    def test_categorize_by_class(self):
        result = TimetableGenerator.categorize_by_class(TIMETABLE_MOCK_SMALL)

        keys = result.keys()

        self.assertEqual(len(keys), 2)

        sorted_keys = list(keys)
        sorted_keys.sort()

        self.assertEqual(sorted_keys[0], 'Database Systems')
        self.assertEqual(sorted_keys[1], 'Introduction to Programming')

        self.assertEqual(result[sorted_keys[0]], [TIMETABLE_MOCK_SMALL[1]])
        self.assertEqual(result[sorted_keys[1]], [TIMETABLE_MOCK_SMALL[0]])

    def test_transform_for_timetable(self):
        mock_lambda = MagicMock(return_value='')

        result = TimetableGenerator.transform_for_timetable(TIMETABLE_MOCK_SMALL, mock_lambda)
        self.assertEqual(result, [['Monday'], '', ['Friday'], ''])

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
        # ss = MagicMock()
        # ss.assert_called()
        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_student_page()

            self.assertEqual(mock_file_open.call_count, 5)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 5)
            self.assertEqual(handle.write.call_count, 5)

    def test_generate_professors_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()
        # ss = MagicMock()
        # ss.assert_called()
        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_professors_page()

            self.assertEqual(mock_file_open.call_count, 3)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 3)
            self.assertEqual(handle.write.call_count, 3)

    def test_generate_rooms_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()
        # ss = MagicMock()
        # ss.assert_called()
        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_rooms_page()

            self.assertEqual(mock_file_open.call_count, 3)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 3)
            self.assertEqual(handle.write.call_count, 3)

    def test_generate_classes_page(self):
        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()
        # ss = MagicMock()
        # ss.assert_called()
        with patch('builtins.open', mock_file_open):
            timetable_generator = TimetableGenerator(TIMETABLE_MOCK_SMALL)
            timetable_generator.generate_classes_page()

            self.assertEqual(mock_file_open.call_count, 3)

            handle = mock_file_open()
            self.assertEqual(handle.close.call_count, 3)
            self.assertEqual(handle.write.call_count, 3)

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
