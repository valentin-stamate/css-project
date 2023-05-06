import unittest

from src.database_connection import DatabaseConnection
from src.utils.utils import Utils


class UtilsTest(unittest.TestCase):

    def test_convert_disciplines_rows_to_objects(self):
        conn = DatabaseConnection()
        rows = conn.get_all_planned_disciplines()

        converted_disciplines = Utils.planned_disciplines_rows_to_objects(rows)

        print(converted_disciplines)
