import datetime
import unittest
from unittest.mock import patch, mock_open, MagicMock

from src.service.html_service import HTMLPage, TimetablePage


class TestHTMLPage(unittest.TestCase):

    def test_add(self):
        html_page = HTMLPage()

        self.assertEqual(len(html_page.elements), 0)
        html_page.add('')
        self.assertEqual(len(html_page.elements), 1)

    def test_generate_html(self):
        html_page = HTMLPage()
        html_page.header = '<html><body>'

        html_page.add('<span>test</span>')

        result = html_page.generate_html()

        self.assertEqual(result, '<html><body><span>test</span></body></html>')


class TestTimetablePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_generate_html(self):
        mock_title = 'Title'
        mock_headers = ['id', 'firstname', 'lastname']
        mock_data = [[1, 'john', 'doe'], [2, 'lorm', ['ipsum', 'sit']]]
        mock_path = ''

        HTMLPage.header = ''
        HTMLPage.closing_header = ''

        mock_file_open = mock_open()

        with patch('builtins.open', mock_file_open):
            timetable_page = TimetablePage(mock_title, mock_headers, mock_data, mock_path)

            self.assertEqual(timetable_page.title, mock_title)
            self.assertEqual(type(timetable_page.date) is datetime.date, True)
            self.assertEqual(timetable_page.headers, mock_headers)
            self.assertEqual(timetable_page.data, mock_data)
            self.assertEqual(timetable_page.cols, len(mock_headers))
            self.assertEqual(timetable_page.path, mock_path)

            result = timetable_page.generate_html()

            mock_file_open.assert_called_once_with(mock_path, 'wt')
            handle = mock_file_open()
            handle.close.assert_called_once()

            self.assertEqual(result, '<h1>Title</h1>'
                                     '<div>'
                                     f'<strong>Generated: {datetime.date.today().isoformat()}</strong></div>'
                                     '<hr>'
                                     '<table>'
                                        '<tr>'
                                            '<th colspan="1">id</th>'
                                            '<th colspan="1">firstname</th>'
                                            '<th colspan="1">lastname</th>'
                                        '</tr>'
                                        '<tr>'
                                            '<td colspan="1">1</td>'
                                            '<td colspan="1">john</td>'
                                            '<td colspan="1">doe</td>'
                                        '</tr>'
                                        '<tr>'
                                            '<td colspan="1">2</td>'
                                            '<td colspan="1">lorm</td>'
                                            '<td colspan="1">ipsum, sit</td>'
                                        '</tr>'
                                     '</table>')
