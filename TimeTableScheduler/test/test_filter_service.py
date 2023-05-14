import unittest
from unittest.mock import patch

from src.enums.TimePeriods import TimePeriods
from src.enums.Weekdays import Weekdays
from src.enums.Years import Years
from src.service import filter_service as target


def mocked_disciplines():
    return [
        ["1", "Disciplina 1", "1", "0", "0", "0", "0", "1", "1", "0", "1"],
        ["2", "Disciplina 2", "1", "0", "0", "0", "0", "2", "1", "0", "1"],
        ["3", "Disciplina 3", "1", "0", "1", "0", "0", "1", "1", "1", "0"],
        ["4", "Disciplina 4", "0", "0", "0", "1", "0", "2", "1", "0", "1"],
    ]


def mocked_student_groups():
    return [
        ["1", "1", "A1"],
        ["2", "1", "A2"],
        ["3", "2", "B1"],
        ["4", "2", "B2"],
        ["5", "3", "C1"],
        ["6", "3", "C2"],
        ["7", "4", "D1"],
        ["8", "4", "D2"],
        ["9", "5", "E1"],
        ["10", "5", "E2"],
    ]


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


def mocked_time_slots_teacher():
    return [
        ["1", "16:00 - 18:00", "Miercuri", "10", "1", "31", "1", "0", "0", "1"],
        ["2", "08:00 - 10:00", "Luni", "11", "1", "32", "0", "1", "0", "2"],
        ["3", "12:00 - 14:00", "Marti", "12", "1", "33", "0", "0", "1", "3"],
        ["4", "14:00 - 16:00", "Miercuri", "13", "1", "34", "0", "0", "1", "4"],
    ]


def mocked_db_call_time_slots_student_group(table_name: str, filter_column: str, filter_value: int):
    if table_name != "TimeSlots":
        raise Exception("Should be called only for TimeSlots table")

    if filter_column == 'student_group_id':
        if filter_value == 1:
            return [
                ["1", "16:00 - 18:00", "Miercuri", "10", "18", "1", "1", "0", "0", "1"],
                ["2", "12:00 - 14:00", "Marti", "11", "19", "1", "0", "1", "0", "2"],
            ]
        elif filter_value == 2:
            return [
                ["3", "16:00 - 18:00", "Miercuri", "10", "18", "2", "1", "0", "0", "1"],
                ["4", "18:00 - 20:00", "Miercuri", "11", "19", "2", "0", "0", "1", "2"],
                ["5", "08:00 - 10:00", "Luni", "11", "19", "2", "0", "1", "0", "2"],
            ]

    return []


def mocked_db_call_rooms(table_name: str, filter_column: str, filter_value: bool):
    if table_name != "Rooms":
        raise Exception("Should be called only for Rooms table")

    if filter_column == 'can_host_course':
        return [
            ["1", "B3", "1", "0", "0"],
            ["12", "C112", "1", "0", "0"],
            ["13", "C114", "1", "0", "0"]
        ]

    if filter_column == 'can_host_laboratory':
        return [
            ["4", "C210", "0", "1", "0"],
            ["5", "C401", "0", "1", "0"],
            ["6", "C403", "0", "1", "0"]
        ]

    if filter_column == 'can_host_seminary':
        return [
            ["16", "C308", "0", "0", "1"],
            ["17", "C901", "0", "0", "1"],
            ["18", "C903", "0", "0", "1"],
        ]

    return []


def mocked_db_call_time_slots_by_room_id_weekday_and_time(table_name: str, filter_column1: str, filter_value1: int,
                                                          filter_column2: str, filter_value2: str,
                                                          filter_column3: str, filter_value3: str):
    if table_name != "TimeSlots":
        raise Exception("Should be called only for TimeSlots table")

    if filter_column1 == 'room_id' and filter_column2 == 'weekday' and filter_column3 == 'time':
        if filter_value1 in ['1', '5', '18'] and filter_value2 == '"Luni"' and filter_value3 in '"08:00 - 10:00"':
            return [
                ['1', "08:00 - 10:00", "Luni", "1", "1", "1", "1", "0", "0", f"{filter_value1}"]
            ]

    return []


class TestFilterService(unittest.TestCase):
    def test_get_year_index_from_string_bachelor_first(self):
        year = "Anul 1"
        expected_response = 2

        response = target.get_year_index_from_string(year)

        self.assertEqual(expected_response, response)

    def test_get_year_index_from_string_bachelor_fsecond(self):
        year = "Anul 2"
        expected_response = 3

        response = target.get_year_index_from_string(year)

        self.assertEqual(expected_response, response)

    def test_get_year_index_from_string_bachelor_third(self):
        year = "Anul 3"
        expected_response = 4

        response = target.get_year_index_from_string(year)

        self.assertEqual(expected_response, response)

    def test_get_year_index_from_string_master_first(self):
        year = "Master Anul 1"
        expected_response = 5

        response = target.get_year_index_from_string(year)

        self.assertEqual(expected_response, response)

    def test_get_year_index_from_string_master_second(self):
        year = "Master Anul 2"
        expected_response = 6

        response = target.get_year_index_from_string(year)

        self.assertEqual(expected_response, response)

    def test_get_year_index_from_string_invalid_year(self):
        year = "Anul X"

        try:
            response = target.get_year_index_from_string(year)
            self.fail("Should have thrown exception")
        except Exception as e:
            self.assertTrue("Invalid year" in e.args[0])

    def test_encode_year_str_to_int_bachelor_first(self):
        year = "Anul 1"
        expected_response = 1

        response = target.encode_year_str_to_int(year)

        self.assertEqual(expected_response, response)

    def test_encode_year_str_to_int_bachelor_second(self):
        year = "Anul 2"
        expected_response = 2

        response = target.encode_year_str_to_int(year)

        self.assertEqual(expected_response, response)

    def test_encode_year_str_to_int_bachelor_third(self):
        year = "Anul 3"
        expected_response = 3

        response = target.encode_year_str_to_int(year)

        self.assertEqual(expected_response, response)

    def test_encode_year_str_to_int_master_first(self):
        year = "Master Anul 1"
        expected_response = 4

        response = target.encode_year_str_to_int(year)

        self.assertEqual(expected_response, response)

    def test_encode_year_str_to_int_master_second(self):
        year = "Master Anul 2"
        expected_response = 5

        response = target.encode_year_str_to_int(year)

        self.assertEqual(expected_response, response)

    def test_encode_year_str_to_int_invalid_year(self):
        year = "Anul X"

        try:
            response = target.encode_year_str_to_int(year)
            self.fail("Should have thrown exception")
        except Exception as e:
            self.assertTrue("Invalid year" in e.args[0])

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_unformatted",
           return_value=mocked_disciplines())
    @patch(target="src.service.filter_service.get_year_index_from_string", return_value=2)
    def test_get_disciplines_for_year_and_semester(self, mocker1, mocker2):
        year = "Anul 1"
        semester = "Semestrul 1"
        expected_response = ["Disciplina 1", "Disciplina 3"]

        response = target.get_disciplines_for_year_and_semester(year, semester)

        self.assertEqual(expected_response, response)

    def test_get_student_groups_in_year_course(self):
        year = "Anul 1"
        class_type = "Curs"
        expected_response = Years.get_all_values()

        response = target.get_student_groups_in_year(year, class_type)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_unformatted",
           return_value=mocked_student_groups())
    @patch(target="src.service.filter_service.encode_year_str_to_int", return_value=1)
    def test_get_student_groups_in_year_bachelor(self, mocker1, mocker2):
        year = "Anul 1"
        class_type = "Laborator"
        expected_response = ["1A1", "1A2"]

        response = target.get_student_groups_in_year(year, class_type)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_unformatted",
           return_value=mocked_student_groups())
    @patch(target="src.service.filter_service.encode_year_str_to_int", return_value=4)
    def test_get_student_groups_in_year_master(self, mocker1, mocker2):
        year = "Master Anul 1"
        class_type = "Laborator"
        expected_response = ["D1", "D2"]

        response = target.get_student_groups_in_year(year, class_type)

        self.assertEqual(expected_response, response)

    def test_get_teacher_entity_id_by_name_and_title_empty_teacher(self):
        teacher_with_name_and_title = ""
        expected_response = 1

        response = target.get_teacher_entity_id_by_name_and_title(teacher_with_name_and_title)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           return_value=[["3", "Ion Ionescu", "Conf. Dr."]])
    def test_get_teacher_entity_id_by_name_and_title(self, mocker):
        teacher_with_name_and_title = "Ion Ionescu, Conf. Dr."
        expected_response = 3

        response = target.get_teacher_entity_id_by_name_and_title(teacher_with_name_and_title)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           return_value=[])
    def test_get_teacher_entity_id_by_name_and_title_teacher_not_found(self, mocker):
        teacher_with_name_and_title = "Ion Ionescu, Conf. Dr."

        try:
            response = target.get_teacher_entity_id_by_name_and_title(teacher_with_name_and_title)
            self.fail("Should have thrown exception")
        except Exception as e:
            self.assertTrue("Couldn't find teacher " in e.args[0])

    def test_get_student_group_entity_ids_by_name_empty_name(self):
        student_group_name = ""
        expected_response = 1

        response = target.get_student_group_entity_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_student_group_entity_ids)
    def test_get_student_group_entity_ids_by_name_whole_year(self, mocker):
        student_group_name = "Anul 1"
        expected_response = [1, 3, 5]

        response = target.get_student_group_entity_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_student_group_entity_ids)
    def test_get_student_group_entity_ids_by_name_master_student_group(self, mocker):
        student_group_name = "MOC1"
        expected_response = [7]

        response = target.get_student_group_entity_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           side_effect=mocked_db_call_student_group_entity_ids_multiple_filters)
    def test_get_student_group_entity_ids_by_name_bachelor_student_group(self, mocker):
        student_group_name = "1A1"
        expected_response = [15]

        response = target.get_student_group_entity_ids_by_name(student_group_name)

        self.assertEqual(expected_response, response)

    @patch(target="src.enums.Years.Years.is_any_year",
           return_value=False)
    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns",
           return_value=[])
    def test_get_student_group_entity_ids_by_name_unknown_student_group(self, mocker1, mocker2):
        student_group_name = "should-not-be-found-in-db"

        try:
            response = target.get_student_group_entity_ids_by_name(student_group_name)
            self.fail("Should have thrown exception")
        except Exception as e:
            self.assertTrue("Couldn't find group" in e.args[0])

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           return_value=mocked_time_slots_teacher())
    def test_get_unavailable_slots_for_teacher(self, mocker):
        teacher_id = 1
        expected_response = {"Luni": ["08:00 - 10:00"], "Marti": ["12:00 - 14:00"], "Miercuri": ["16:00 - 18:00", "14:00 - 16:00"]}

        response = target.get_unavailable_slots_for_teacher(teacher_id)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_time_slots_student_group)
    def test_get_unavailable_slots_for_student_groups(self, mocker):
        group_ids = [1, 2]
        expected_response = [
            {'Marti': ['12:00 - 14:00'], 'Miercuri': ['16:00 - 18:00']},
            {'Luni': ['08:00 - 10:00'], 'Miercuri': ['16:00 - 18:00', '18:00 - 20:00']}
        ]

        response = target.get_unavailable_slots_for_student_groups(group_ids)

        self.assertEqual(expected_response, response)

    def test_get_all_time_slots(self):
        expected_response = {weekday: TimePeriods.get_all_values() for weekday in Weekdays.get_all_values()}

        response = target.get_all_time_slots()

        self.assertEqual(expected_response, response)

    def test_remove_slots(self):
        remove_from = {'Luni': ['08:00 - 10:00'], 'Miercuri': ['16:00 - 18:00', '18:00 - 20:00']}
        entities = {'Miercuri': ['16:00 - 18:00']}
        expected_response = {'Luni': ['08:00 - 10:00'], 'Miercuri': ['18:00 - 20:00']}

        response = target.remove_slots(remove_from, entities)

        self.assertEqual(expected_response, response)

    def test_format_slots(self):
        slots = {'Luni': ['08:00 - 10:00'], 'Miercuri': ['16:00 - 18:00', '18:00 - 20:00']}
        expected_response = ["Luni, 08:00 - 10:00", "Miercuri, 16:00 - 18:00", "Miercuri, 18:00 - 20:00"]

        response = target.format_slots(slots)

        self.assertEqual(expected_response, response)

    @patch(target="src.service.filter_service.get_teacher_entity_id_by_name_and_title",
           return_value=1)
    @patch(target="src.service.filter_service.get_unavailable_slots_for_teacher",
           return_value={"Luni": ["08:00 - 10:00"], "Marti": ["12:00 - 14:00"], "Miercuri": ["16:00 - 18:00", "14:00 - 16:00"]})
    @patch(target="src.service.filter_service.get_student_group_entity_ids_by_name",
           return_value=[5])
    @patch(target="src.service.filter_service.get_unavailable_slots_for_student_groups",
           return_value=[{'Luni': ['08:00 - 10:00'], 'Joi': ['08:00 - 10:00', '10:00 - 12:00']}])
    def test_get_available_slots_for_teacher_and_student_group(self, mocker1, mocker2, mocker3, mocker4):
        teacher = "Ion Ionescu, Conf. Dr."
        student_group = "1A1"
        expected_response = [
            'Luni, 10:00 - 12:00', 'Luni, 12:00 - 14:00', 'Luni, 14:00 - 16:00', 'Luni, 16:00 - 18:00', 'Luni, 18:00 - 20:00',
            'Marti, 08:00 - 10:00', 'Marti, 10:00 - 12:00', 'Marti, 14:00 - 16:00', 'Marti, 16:00 - 18:00', 'Marti, 18:00 - 20:00',
            'Miercuri, 08:00 - 10:00', 'Miercuri, 10:00 - 12:00', 'Miercuri, 12:00 - 14:00', 'Miercuri, 18:00 - 20:00',
            'Joi, 12:00 - 14:00', 'Joi, 14:00 - 16:00', 'Joi, 16:00 - 18:00', 'Joi, 18:00 - 20:00',
            'Vineri, 08:00 - 10:00', 'Vineri, 10:00 - 12:00', 'Vineri, 12:00 - 14:00', 'Vineri, 14:00 - 16:00', 'Vineri, 16:00 - 18:00', 'Vineri, 18:00 - 20:00',
            'Sambata, 08:00 - 10:00', 'Sambata, 10:00 - 12:00', 'Sambata, 12:00 - 14:00', 'Sambata, 14:00 - 16:00', 'Sambata, 16:00 - 18:00', 'Sambata, 18:00 - 20:00'
        ]

        response = target.get_available_slots_for_teacher_and_student_group(teacher, student_group)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_rooms)
    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns_3",
           side_effect=mocked_db_call_time_slots_by_room_id_weekday_and_time)
    def test_get_available_rooms_for_time_slot_and_class_type_course(self, mocker1, mocker2):
        time_slot = "Luni, 08:00 - 10:00"
        course = True
        laboratory = False
        seminary = False

        expected_response = ['C112', 'C114']

        response = target.get_available_rooms_for_time_slot_and_class_type(time_slot, course, laboratory, seminary)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_rooms)
    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns_3",
           side_effect=mocked_db_call_time_slots_by_room_id_weekday_and_time)
    def test_get_available_rooms_for_time_slot_and_class_type_laboratory(self, mocker1, mocker2):
        time_slot = "Luni, 08:00 - 10:00"
        course = False
        laboratory = True
        seminary = False

        expected_response = ['C210', 'C403']

        response = target.get_available_rooms_for_time_slot_and_class_type(time_slot, course, laboratory, seminary)

        self.assertEqual(expected_response, response)

    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_column",
           side_effect=mocked_db_call_rooms)
    @patch(target="src.database_connection.DatabaseConnection.get_all_rows_by_columns_3",
           side_effect=mocked_db_call_time_slots_by_room_id_weekday_and_time)
    def test_get_available_rooms_for_time_slot_and_class_type_seminary(self, mocker1, mocker2):
        time_slot = "Luni, 08:00 - 10:00"
        course = False
        laboratory = False
        seminary = True

        expected_response = ['C308', 'C901']

        response = target.get_available_rooms_for_time_slot_and_class_type(time_slot, course, laboratory, seminary)

        self.assertEqual(expected_response, response)
