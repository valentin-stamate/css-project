import unittest

from src.database_connection import DatabaseConnection
from src.service.models import ProgrammedClass
from src.utils.utils import Utils
from unittest.mock import MagicMock
from test.const.mock import MOCK_PLANNED_COURSES


class UtilsTest(unittest.TestCase):

    def test_convert_disciplines_rows_to_objects(self):
        conn = DatabaseConnection.get_instance()
        conn.get_all_planned_disciplines = MagicMock(return_value=[MOCK_PLANNED_COURSES[0]])

        rows = conn.get_all_planned_disciplines()
        converted_disciplines = Utils.planned_disciplines_rows_to_objects(rows)

        self.assertEqual(len(converted_disciplines), 1)
        self.assertTrue(type(converted_disciplines[0]) is ProgrammedClass)


