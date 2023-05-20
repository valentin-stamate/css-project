from src.database_connection import DatabaseConnection
from src.enums.Semesters import Semesters
from src.enums.TimePeriods import TimePeriods
from src.enums.Weekdays import Weekdays
from src.enums.Years import Years


def get_year_index_from_string(year: str) -> int:
    assert year is not None and type(year) == str and len(year.strip()) > 0

    year_index = 0
    if Years.is_bachelor_first_year(year):
        year_index = 2
    elif Years.is_bachelor_second_year(year):
        year_index = 3
    elif Years.is_bachelor_third_year(year):
        year_index = 4
    elif Years.is_master_first_year(year):
        year_index = 5
    elif Years.is_master_second_year(year):
        year_index = 6

    if year_index == 0:
        raise Exception(f"Invalid year: \"{year}\"")

    return year_index


def encode_year_str_to_int(year: str) -> int:
    assert year is not None and type(year) == str and len(year.strip()) > 0

    year_int = 0
    if Years.is_bachelor_first_year(year):
        year_int = 1
    elif Years.is_bachelor_second_year(year):
        year_int = 2
    elif Years.is_bachelor_third_year(year):
        year_int = 3
    elif Years.is_master_first_year(year):
        year_int = 4
    elif Years.is_master_second_year(year):
        year_int = 5

    if year_int == 0:
        raise Exception(f"Invalid year: \"{year}\"")

    return year_int


def get_disciplines_for_year_and_semester(year: str, semester: str):
    assert year is not None and type(year) == str and len(year.strip()) > 0
    assert semester is not None and type(semester) == str and len(semester.strip()) > 0

    disciplines = DatabaseConnection.get_instance().get_all_rows_unformatted("Disciplines")

    year_index = get_year_index_from_string(year)

    semester = 1 if Semesters.is_first_semester(semester) else 2

    filtered_disciplines = []
    for discipline in disciplines:
        if int(discipline[year_index]) == 1 and int(discipline[7]) == semester:
            filtered_disciplines.append(discipline[1])

    assert filtered_disciplines is not None
    return filtered_disciplines


def get_student_groups_in_year(year: str, class_type: str):
    assert year is not None and type(year) == str and len(year.strip()) > 0
    assert class_type is not None and type(class_type) == str and len(class_type.strip()) > 0

    if class_type == 'Curs':
        return Years.get_all_values()

    student_groups = DatabaseConnection.get_instance().get_all_rows_unformatted("StudentGroups")

    year_index = encode_year_str_to_int(year)

    filtered_student_groups = []
    for student_group in student_groups:
        if int(student_group[1]) == year_index:
            name = student_group[2] if year_index > 3 else str(year_index) + student_group[2]
            filtered_student_groups.append(name)

    assert filtered_student_groups is not None
    return filtered_student_groups


def get_teacher_entity_id_by_name_and_title(teacher_with_name_and_title: str) -> int:
    assert teacher_with_name_and_title is not None and type(teacher_with_name_and_title) == str and \
           len(teacher_with_name_and_title.strip()) > 0

    if teacher_with_name_and_title.strip() == '':
        return 1

    teacher_name = teacher_with_name_and_title.split(", ")[0].strip()
    teacher_title = teacher_with_name_and_title.split(", ")[1].strip()

    matched_teacher_entities = DatabaseConnection.get_instance().get_all_rows_by_columns(
        "Teachers", "name", f"\"{teacher_name}\"", "title", f"\"{teacher_title}\""
    )

    assert matched_teacher_entities is not None

    if len(matched_teacher_entities) == 0:
        raise Exception(f"Couldn't find teacher \"{teacher_with_name_and_title}\" in database.")

    return int(matched_teacher_entities[0][0])


def get_student_group_entity_ids_by_name(student_group_name: str) -> [int]:
    assert student_group_name is not None and type(student_group_name) == str and len(student_group_name.strip()) > 0

    if Years.is_any_year(student_group_name):
        year_index = Years.get_year_index(student_group_name)
        matched_student_group_entities = DatabaseConnection.get_instance().get_all_rows_by_column(
            "StudentGroups", "year", f"{year_index}"
        )

        return [int(entity[0]) for entity in matched_student_group_entities]

    if "M" in student_group_name:
        matched_student_group_entities = DatabaseConnection.get_instance().get_all_rows_by_column(
            "StudentGroups", "group_name", f"\"{student_group_name}\""
        )
    else:
        year = student_group_name[0]
        student_group_name = student_group_name[1:]

        matched_student_group_entities = DatabaseConnection.get_instance().get_all_rows_by_columns(
            "StudentGroups", "group_name", f"\"{student_group_name}\"", "year", year
        )

    assert matched_student_group_entities is not None

    if len(matched_student_group_entities) == 0:
        raise Exception(f"Couldn't find group \"{student_group_name}\" in database.")

    return [int(matched_student_group_entities[0][0])]


def get_unavailable_slots_for_teacher(teacher_id: int):
    assert teacher_id is not None and type(teacher_id) == int

    classes_for_teacher = DatabaseConnection.get_instance().get_all_rows_by_column(
        "TimeSlots", "teacher_id", teacher_id
    )

    occupied_periods = {}
    for scheduled_class in classes_for_teacher:
        weekday = scheduled_class[2]
        time_period = scheduled_class[1]

        if weekday not in occupied_periods.keys():
            occupied_periods[weekday] = []

        if time_period not in occupied_periods[weekday]:
            occupied_periods[weekday].append(time_period)

    return occupied_periods


def get_unavailable_slots_for_student_groups(group_ids: [int]) -> list[dict]:
    assert group_ids is not None and type(group_ids) == list

    periods = []

    for group_id in group_ids:
        classes_for_student_group = DatabaseConnection.get_instance().get_all_rows_by_column(
            "TimeSlots", "student_group_id", group_id
        )

        occupied_periods = {}
        for scheduled_class in classes_for_student_group:
            weekday = scheduled_class[2]
            time_period = scheduled_class[1]

            if weekday not in occupied_periods.keys():
                occupied_periods[weekday] = []

            if time_period not in occupied_periods[weekday]:
                occupied_periods[weekday].append(time_period)

        periods.append(occupied_periods)

    return periods


def get_all_time_slots() -> dict:
    all_time_slots = {}
    for weekday in Weekdays.get_all_values():
        all_time_slots[weekday] = TimePeriods.get_all_values()

    return all_time_slots


def remove_slots(remove_from: dict, entities: dict) -> dict:
    assert remove_from is not None and type(remove_from) == dict
    assert entities is not None and type(entities) == dict

    for weekday in entities.keys():
        if weekday in remove_from.keys():
            for time_period in entities[weekday]:
                if time_period in remove_from[weekday]:
                    remove_from[weekday].remove(time_period)

    for weekday in remove_from.keys():
        if len(remove_from[weekday]) == 0:
            del remove_from[weekday]

    assert remove_from is not None

    return remove_from


def format_slots(slots: dict) -> list:
    assert slots is not None and type(slots) == dict

    new_slots = []

    for weekday in slots:
        for time_slot in slots[weekday]:
            new_slots.append(f"{weekday}, {time_slot}")

    return new_slots


def get_available_slots_for_teacher_and_student_group(teacher: str, student_group: str):
    assert teacher is not None and type(teacher) == str and len(teacher.strip()) > 0
    assert student_group is not None and type(student_group) == str and len(student_group.strip()) > 0

    available_time_slots = get_all_time_slots()

    assert available_time_slots is not None

    teacher_id = get_teacher_entity_id_by_name_and_title(teacher)
    teacher_unavailable_slots = get_unavailable_slots_for_teacher(teacher_id)
    available_time_slots = remove_slots(available_time_slots, teacher_unavailable_slots)

    assert available_time_slots is not None

    group_ids = get_student_group_entity_ids_by_name(student_group)
    student_group_unavailable_slots_list = get_unavailable_slots_for_student_groups(group_ids)
    for student_group_unavailable_slots in student_group_unavailable_slots_list:
        available_time_slots = remove_slots(available_time_slots, student_group_unavailable_slots)
        assert available_time_slots is not None

    return format_slots(available_time_slots)


def get_available_rooms_for_time_slot_and_class_type(time_slot: str, course: bool, laboratory: bool, seminary: bool):
    assert time_slot is not None and type(time_slot) == str and len(time_slot.strip()) > 0
    assert course is not None and type(course) == bool
    assert laboratory is not None and type(laboratory) == bool
    assert seminary is not None and type(seminary) == bool

    rooms = []
    if course:
        rooms = DatabaseConnection.get_instance().get_all_rows_by_column('Rooms', 'can_host_course', course)
    elif laboratory:
        rooms = DatabaseConnection.get_instance().get_all_rows_by_column('Rooms', 'can_host_laboratory', laboratory)
    elif seminary:
        rooms = DatabaseConnection.get_instance().get_all_rows_by_column('Rooms', 'can_host_seminary', seminary)

    weekday = time_slot.split(", ")[0].strip()
    time_period = time_slot.split(", ")[1].strip()

    available_rooms = []
    for room in rooms:
        schedules_for_room = DatabaseConnection.get_instance().get_all_rows_by_columns_3(
            'TimeSlots', 'room_id', room[0], 'weekday', f"\"{weekday}\"", "time", f"\"{time_period}\""
        )

        if len(schedules_for_room) == 0:
            available_rooms.append(room[1])

    return available_rooms
