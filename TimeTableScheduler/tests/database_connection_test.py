import unittest

from src.database_connection import DatabaseConnection


class DatabaseConnectionTest(unittest.TestCase):

    def test_get_all_classes(self):
        conn = DatabaseConnection()
        print(conn.get_all_planned_disciplines())
