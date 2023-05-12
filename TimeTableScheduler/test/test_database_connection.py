import time
import unittest
from unittest import mock
from unittest.mock import Mock

from src.database_connection import DatabaseConnection
from src.entities import Teachers, Disciplines, Rooms, TimeSlots, StudentGroups
from src.enums.Configuration import Configuration
from src.enums.Years import Years
from test.const.mock import MOCK_STUDENT_GROUPS


class DatabaseConnectionTest(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnection.get_instance()

    def tearDown(self):
        self.db.close()
        self.db.__instance = None
        self.db = None

    # def test_execute_query_valid(self):
    #     query = "INSERT INTO Teachers (name, title) VALUES ('Nume Profesor', 'Titlu profesor')"
    #     self.db.cursor = Mock()
    #     self.db.cursor.execute = Mock(return_value=True)
    #     self.db.connection = Mock()
    #     self.db.connection.commit = Mock(return_value=True)
    #
    #     result = self.db.execute_query(query)
    #
    #     self.db.cursor.execute.assert_called_once_with(query)
    #     self.db.connection.commit.assert_called_once()
    #     self.assertEqual(result, 0)
    #
    # def test_execute_query_invalid(self):
    #     query = "INVALID QUERY"
    #     self.db.cursor = Mock()
    #     self.db.cursor.execute.side_effect = Exception()
    #     self.db.connection = Mock()
    #     self.db.connection.commit = Mock()
    #
    #     result = self.db.execute_query(query)
    #
    #     self.db.cursor.execute.assert_called_once_with(query)
    #     self.db.connection.commit.assert_not_called()
    #     self.assertEqual(result, 2)

    def test_insert_teacher_valid_values(self):
        teacher = Teachers(name="Nume Profesor", title="Titlu profesor")

        self.db.execute_query = Mock(return_value=True)
        self.db.get_teacher = Mock(return_value=False)

        result = self.db.insert_teacher(teacher)

        self.db.execute_query.assert_called_once_with(
            "INSERT INTO Teachers (name, title) VALUES ('Nume Profesor', 'Titlu profesor')")
        self.assertEqual(result, True)

    def test_insert_teacher_existing_values(self):
        teacher = Teachers(name="Nume Profesor", title="Titlu profesor")

        self.db.execute_query = Mock(return_value=True)
        self.db.get_teacher = Mock(return_value=True)

        result = self.db.insert_teacher(teacher)

        self.db.execute_query.assert_not_called()
        self.assertEqual(result, 1)

    def test_insert_discipline_valid_values(self):
        discipline = Disciplines(name="Discipline Name", semester=1)

        self.db.execute_query = Mock(return_value=True)
        self.db.get_discipline = Mock(return_value=False)

        result = self.db.insert_discipline(discipline)

        self.db.execute_query.assert_called_once_with(
            "INSERT INTO Disciplines (name, semester, for_year_1, for_year_2, for_year_3, for_year_4, for_year_5, has_course, has_laboratory, has_seminary) VALUES ('Discipline Name', 1, False, False, False, False, False, True, False, False)")
        self.assertEqual(result, True)

    def test_insert_discipline_existing_values(self):
        discipline = Disciplines(name="Discipline Name", semester=1)

        self.db.execute_query = Mock(return_value=False)
        self.db.get_discipline = Mock(return_value=True)

        result = self.db.insert_discipline(discipline)

        self.db.execute_query.assert_not_called()
        self.assertEqual(result, 1)

    def test_insert_room_valid_values(self):
        room = Rooms(name="Room Name", can_host_course=True)

        self.db.execute_query = Mock(return_value=True)
        self.db.get_room = Mock(return_value=False)

        result = self.db.insert_room(room)

        self.db.execute_query.assert_called_once_with(
            "INSERT INTO Rooms (name, can_host_course, can_host_laboratory, can_host_seminary) VALUES ('Room Name', True, False, False)")
        self.assertEqual(result, True)

    def test_insert_room_invalid_values(self):
        room = Rooms(name="Room Name", can_host_course=True)

        self.db.execute_query = Mock(return_value=False)
        self.db.get_room = Mock(return_value=True)

        result = self.db.insert_room(room)

        self.db.execute_query.assert_not_called()
        self.assertEqual(result, 1)

    def test_insert_schedule(self):
        timeslot = TimeSlots(time="08:00-10:00", weekday="Luni", discipline=0, teacher=0,
                             students=0, is_course=True, is_laboratory=False, is_seminary=False, room=0)

        self.db.execute_query = Mock(return_value=None)

        result = self.db.insert_schedule(timeslot)

        self.db.execute_query.assert_called_once_with(
            "INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, student_group_id, is_course, is_laboratory, is_seminary, room_id) VALUES ('08:00-10:00', 'Luni', 0, 0, 0, True, False, False, 0)")
        self.assertEqual(result, None)

    def test_insert_student_group_valid_values(self):
        self.db.execute_query = Mock(return_value=True)
        self.db.get_student_group = Mock(return_value=False)

        student_group = StudentGroups(year=1, group_name="Grupa 1")

        result = self.db.insert_group(student_group)

        self.db.execute_query.assert_called_once_with(
            "INSERT INTO StudentGroups (year, group_name) VALUES (1, 'Grupa 1')")
        self.assertEqual(result, True)

    def test_insert_student_group_existing_values(self):
        self.db.execute_query = Mock(return_value=True)
        self.db.get_student_group = Mock(return_value=True)

        student_group = StudentGroups(year=1, group_name="Grupa 1")

        result = self.db.insert_group(student_group)

        self.db.execute_query.assert_not_called()
        self.assertEqual(result, 1)

    def test_delete_entry_disciplines(self):
        self.db.execute_query = Mock(return_value=True)
        base_query = f"DELETE FROM Disciplines where id = 0"
        reference_query = f"DELETE FROM TimeSlots where discipline_id = 0"
        expected_calls = [
            mock.call(base_query),
            mock.call(reference_query)
        ]

        self.db.delete_entry("Disciplines", 0)

        self.db.execute_query.assert_has_calls(expected_calls, any_order=False)

    def test_delete_entry_rooms(self):
        self.db.execute_query = Mock(return_value=True)
        base_query = f"DELETE FROM Rooms where id = 0"
        reference_query = f"DELETE FROM TimeSlots where room_id = 0"
        expected_calls = [
            mock.call(base_query),
            mock.call(reference_query)
        ]

        self.db.delete_entry("Rooms", 0)

        self.db.execute_query.assert_has_calls(expected_calls, any_order=False)

    def test_delete_entry_teachers(self):
        self.db.execute_query = Mock(return_value=True)
        base_query = f"DELETE FROM Teachers where id = 0"
        reference_query = f"DELETE FROM TimeSlots where teacher_id = 0"
        expected_calls = [
            mock.call(base_query),
            mock.call(reference_query)
        ]

        self.db.delete_entry("Teachers", 0)

        self.db.execute_query.assert_has_calls(expected_calls, any_order=False)

    def test_delete_entry_student_group(self):
        self.db.execute_query = Mock(return_value=True)
        base_query = f"DELETE FROM StudentGroups where id = 0"
        reference_query = f"DELETE FROM TimeSlots where student_group_id = 0"
        expected_calls = [
            mock.call(base_query),
            mock.call(reference_query)
        ]

        self.db.delete_entry("StudentGroups", 0)

        self.db.execute_query.assert_has_calls(expected_calls, any_order=False)

    def test_delete_entry_invalid_table(self):
        self.db.execute_query = Mock(return_value=True)
        base_query = f"DELETE FROM Invalid Table where id = 0"

        self.db.delete_entry("Invalid Table", 0)

        self.db.execute_query.assert_called_once_with(base_query)

    def test_replace(self):
        rows = [(0, 1, 'A1')]

        result = self.db.replace(rows, 1, Configuration.CONVERSION_YEARS_FOR_DB)
        self.assertEqual(result, [[0, 'Anul 1', 'A1']])

    def test_close(self):
        self.db.connection = Mock()
        self.db.connection.close = Mock()
        result = self.db.close()
        self.db.connection.close.assert_called_once()
        self.assertEqual(result, None)

    def test_get_year(self):
        result_1 = self.db.get_year((None, None, 1))
        result_2 = self.db.get_year((None, None, None, 1))
        result_3 = self.db.get_year((None, None, None, None, 1))
        result_4 = self.db.get_year((None, None, None, None, None, 1))
        result_5 = self.db.get_year((None, None, None, None, None, None, 1))
        self.assertEqual(result_1, Years.BACHELOR_YEAR_1)
        self.assertEqual(result_2, Years.BACHELOR_YEAR_2)
        self.assertEqual(result_3, Years.BACHELOR_YEAR_3)
        self.assertEqual(result_4, Years.MASTER_YEAR_1)
        self.assertEqual(result_5, Years.MASTER_YEAR_2)

    def test_get_room(self):
        self.db.get_all_rows_by_column = Mock(return_value=[])
        room = Rooms('name')
        result = self.db.get_room(room)
        self.assertEqual(result, False)

    def test_get_discipline(self):
        self.db.get_all_rows_by_column = Mock(return_value=[])
        disc = Disciplines('name', None)
        result = self.db.get_discipline(disc)
        self.assertEqual(result, False)

    def test_get_teacher(self):
        self.db.get_all_rows_by_column = Mock(return_value=[])
        teacher = Teachers('name', None)
        result = self.db.get_teacher(teacher)
        self.assertEqual(result, False)

    def test_get_student_group(self):
        self.db.get_all_rows_by_column = Mock(return_value=MOCK_STUDENT_GROUPS)

        group = StudentGroups(1, 'A1')
        result = self.db.get_student_group(group)
        self.assertEqual(result, True)

        group = StudentGroups(4, 'A1')
        result = self.db.get_student_group(group)
        self.assertEqual(result, False)

    def test_singleton(self):
        # Test that an exception is raised if a second instance is created
        with self.assertRaises(Exception):
            db2 = DatabaseConnection()
