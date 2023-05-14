import unittest
from unittest.mock import MagicMock, Mock, patch

from src.database_connection import DatabaseConnection
from src.service.models import ProgrammedClass
from src.utils.utils import Utils
from test.const.mock import MOCK_PLANNED_COURSES


def mocked_db_call_student_group_entity_ids(table_name: str, filter_column: str, filter_value: str):
    if table_name != "StudentGroups":
        raise Exception("Should be called only for StudentGroups table")

    if filter_column == 'year':
        return [
            ["1", f"{filter_value}", "A1"],
            ["3", f"{filter_value}", "B1"],
            ["5", f"{filter_value}", "C1"],
        ]

    if filter_column == 'group_name':
        return [
            ["7", f"{filter_value}", "A1"],
            ["8", f"{filter_value}", "B1"],
            ["9", f"{filter_value}", "C1"],
        ]

    return []


def mocked_db_call_student_group_entity_ids_multiple_filters(table_name: str, filter_column1: str, filter_value1: str,
                                                             filter_column2: str, filter_value2: str):
    if table_name != "StudentGroups":
        raise Exception("Should be called only for StudentGroups table")

    if filter_column1 == 'group_name' and filter_column2 == 'year':
        return [
            ["15", f"{filter_value2}", f"{filter_value1}"]
        ]

    return []


class UtilsTest(unittest.TestCase):
    def tearDown(self) -> None:
        super().tearDown()

    @patch(target="src.database_connection.DatabaseConnection.get_all_planned_disciplines",
           return_value=[MOCK_PLANNED_COURSES[0]])
    def test_convert_disciplines_rows_to_objects(self, mocker):
        conn = DatabaseConnection.get_instance()

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

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_unformatted",
           return_value=[[1, 'Discipline1']])
    def test_get_discipline_id_by_name(self, mocker):
        result = Utils.get_discipline_id_by_name('Discipline1')
        self.assertEqual(result, 1)
        result = Utils.get_discipline_id_by_name('Discipline2')
        self.assertEqual(result, 0)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_unformatted",
           return_value=[[1, 'Room1']])
    def test_get_room_id_by_name(self, mocker):
        result = Utils.get_room_id_by_name('Room1')
        self.assertEqual(result, 1)
        result = Utils.get_room_id_by_name('Room2')
        self.assertEqual(result, 0)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           return_value=[["5", 'Ion Ionescu', "Conf. Dr."]])
    def test_get_teacher_id_by_name(self, mocker):
        result = Utils.get_teacher_id_by_name('')
        self.assertEqual(result, 1)

        result = Utils.get_teacher_id_by_name('Ion Ionescu, Conf. Dr.')
        self.assertEqual(result, 5)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           return_value=[])
    def test_get_teacher_id_by_name_teacher_entity_not_found(self, mocker):
        try:
            result = Utils.get_teacher_id_by_name('Andrei Ionescu, Lect.')
            self.fail('Should have thrown exception')
        except Exception as e:
            self.assertTrue("Couldn't find teacher " in e.args[0])

    def test_get_student_group_entity_ids_by_name_empty_name(self):
        student_group_name = ""
        expected_response = []

        response = Utils.get_student_group_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_student_group_entity_ids)
    def test_get_student_group_entity_ids_by_name_whole_year(self, mocker):
        student_group_name = "Anul 1"
        expected_response = [1, 3, 5]

        response = Utils.get_student_group_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_student_group_entity_ids)
    def test_get_student_group_entity_ids_by_name_master_student_group(self, mocker):
        student_group_name = "MOC1"
        expected_response = [7]

        response = Utils.get_student_group_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           side_effect=mocked_db_call_student_group_entity_ids_multiple_filters)
    def test_get_student_group_entity_ids_by_name_bachelor_student_group(self, mocker):
        student_group_name = "1A1"
        expected_response = [15]

        response = Utils.get_student_group_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.enums.Years.Years.is_any_year",
           return_value=False)
    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           return_value=[])
    def test_get_student_group_entity_ids_by_name_unknown_student_group(self, mocker1, mocker2):
        student_group_name = "should-not-be-found-in-db"

        try:
            response = Utils.get_student_group_ids_by_name(student_group_name)
            self.fail("Should have thrown exception")
        except Exception as e:
            self.assertTrue("Couldn't find group" in e.args[0])
