import unittest
from unittest.mock import Mock

from src.database_connection import DatabaseConnection
from src.entities import Teachers, Disciplines, Rooms, TimeSlots, StudentGroups


class DatabaseConnectionTest(unittest.TestCase):

    def test_execute_query_valid(self):
        query = "INSERT INTO Teachers (name, title) VALUES ('Nume Profesor', 'Titlu profesor')"
        db = DatabaseConnection.get_instance()
        db.cursor = Mock()
        db.connection = Mock()

        result = db.execute_query(query)

        db.cursor.execute.assert_called_once_with(query)
        db.connection.commit.assert_called_once()
        self.assertEqual(result, 0)

    def test_execute_query_invalid(self):
        query = "INVALID QUERY"
        db = DatabaseConnection.get_instance()
        db.cursor = Mock()
        db.cursor.execute.side_effect = Exception()
        db.connection = Mock()

        result = db.execute_query(query)

        db.cursor.execute.assert_called_once_with(query)
        db.connection.commit.assert_not_called()
        self.assertEqual(result, 2)

    def test_insert_teacher_valid_values(self):
        teacher = Teachers(name="Nume Profesor", title="Titlu profesor")
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=True)
        db.get_teacher = Mock(return_value=False)

        result = db.insert_teacher(teacher)

        db.execute_query.assert_called_once_with(
            "INSERT INTO Teachers (name, title) VALUES ('Nume Profesor', 'Titlu profesor')")
        self.assertEqual(result, True)

    def test_insert_teacher_existing_values(self):
        teacher = Teachers(name="Nume Profesor", title="Titlu profesor")
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=True)
        db.get_teacher = Mock(return_value=True)

        result = db.insert_teacher(teacher)

        db.execute_query.assert_not_called()
        self.assertEqual(result, 1)

    def test_insert_discipline_valid_values(self):
        discipline = Disciplines(name="Discipline Name", semester=1)
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=True)
        db.get_discipline = Mock(return_value=False)

        result = db.insert_discipline(discipline)

        db.execute_query.assert_called_once_with(
            "INSERT INTO Disciplines (name, semester, for_year_1, for_year_2, for_year_3, for_year_4, for_year_5, has_course, has_laboratory, has_seminary) VALUES ('Discipline Name', 1, False, False, False, False, False, True, False, False)")
        self.assertEqual(result, True)

    def test_insert_discipline_existing_values(self):
        discipline = Disciplines(name="Discipline Name", semester=1)
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=False)
        db.get_discipline = Mock(return_value=False)

        result = db.insert_discipline(discipline)

        db.execute_query.assert_called_once()
        self.assertEqual(result, False)

    def test_insert_room_valid_values(self):
        room = Rooms(name="Room Name", can_host_course=True)
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=True)
        db.get_room = Mock(return_value=False)

        result = db.insert_room(room)

        db.execute_query.assert_called_once_with(
            "INSERT INTO Rooms (name, can_host_course, can_host_laboratory, can_host_seminary) VALUES ('Room Name', True, False, False)")
        self.assertEqual(result, True)

    def test_insert_room_invalid_values(self):
        room = Rooms(name="Room Name", can_host_course=True)
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=False)
        db.get_room = Mock(return_value=False)

        result = db.insert_room(room)

        db.execute_query.assert_called_once()
        self.assertEqual(result, False)

    def test_insert_schedule(self):
        timeslot = TimeSlots(time="08:00-10:00", weekday="Luni", discipline=0, teacher=0,
                             students=0, is_course=True, is_laboratory=False, is_seminary=False, room=0)
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=None)

        result = db.insert_schedule(timeslot)

        db.execute_query.assert_called_once_with(
            "INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, student_group_id, is_course, is_laboratory, is_seminary, room_id) VALUES ('08:00-10:00', 'Luni', 0, 0, 0, True, False, False, 0)")
        self.assertEqual(result, None)

    def test_insert_student_group_valid_values(self):
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=True)
        db.get_student_group = Mock(return_value=False)

        student_group = StudentGroups(year=1, group_name="Grupa 1")

        result = db.insert_group(student_group)

        db.execute_query.assert_called_once_with(
            "INSERT INTO StudentGroups (year, group_name) VALUES (1, 'Grupa 1')")
        self.assertEqual(result, True)

    def test_insert_student_group_existing_values(self):
        db = DatabaseConnection.get_instance()
        db.execute_query = Mock(return_value=True)
        db.get_student_group = Mock(return_value=True)

        student_group = StudentGroups(year=1, group_name="Grupa 1")

        result = db.insert_group(student_group)

        db.execute_query.assert_not_called()
        self.assertEqual(result, 1)
