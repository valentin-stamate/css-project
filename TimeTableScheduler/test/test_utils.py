import unittest
from unittest.mock import MagicMock, Mock

from src.database_connection import DatabaseConnection
from src.service.models import ProgrammedClass
from src.utils.utils import Utils
from test.const.mock import MOCK_PLANNED_COURSES


class UtilsTest(unittest.TestCase):

    def setUp(self) -> None:
        Utils.database_connection = Mock()

    def tearDown(self) -> None:
        super().tearDown()

    def test_convert_disciplines_rows_to_objects(self):
        conn = DatabaseConnection.get_instance()
        conn.get_all_planned_disciplines = MagicMock(return_value=[MOCK_PLANNED_COURSES[0]])

        rows = conn.get_all_planned_disciplines()
        converted_disciplines = Utils.planned_disciplines_rows_to_objects(rows)

        self.assertEqual(len(converted_disciplines), 1)
        self.assertTrue(type(converted_disciplines[0]) is ProgrammedClass)

    def test_convert_semester(self):
        result = Utils.convert_semester("Semester 1")
        self.assertEqual(result, '1')

    def test_convert_year(self):
        result = Utils.convert_year("Anul 1")
        self.assertEqual(result, 1)
        result = Utils.convert_year("Anul 2")
        self.assertEqual(result, 2)
        result = Utils.convert_year("Anul 3")
        self.assertEqual(result, 3)
        result = Utils.convert_year("Master Anul 1")
        self.assertEqual(result, 4)
        result = Utils.convert_year("Master Anul 2")
        self.assertEqual(result, 5)

    def test_get_room_id_by_name(self):
        Utils.database_connection.get_all_rows_unformatted = Mock(return_value=[[1, 'Discipline1']])
        result = Utils.get_discipline_id_by_name('Discipline1')
        self.assertEqual(result, 1)
        result = Utils.get_discipline_id_by_name('Discipline2')
        self.assertEqual(result, 0)
