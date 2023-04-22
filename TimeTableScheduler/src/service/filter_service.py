from src.database_connection import DatabaseConnection
from src.enums.Semesters import Semesters
from src.enums.Years import Years


def get_disciplines_for_year_and_semester(year: str, semester: str):
    disciplines = DatabaseConnection.get_instance().get_all_rows("Disciplines")[1:]

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

    semester = 1 if Semesters.is_first_semester(semester) else 2

    filtered_disciplines = []
    for discipline in disciplines:
        if int(discipline[year_index]) == 1 and int(discipline[7]) == semester:
            filtered_disciplines.append(discipline[1])

    return filtered_disciplines
