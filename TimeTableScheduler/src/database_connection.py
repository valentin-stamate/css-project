import sqlite3

from src.entities import *
from src.enums.Configuration import Configuration
from src.enums.Years import Years


class DatabaseConnection:
    __instance = None

    def __init__(self):
        if DatabaseConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseConnection.__instance = self
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursor = self.connection.cursor()

    @staticmethod
    def get_instance():
        if DatabaseConnection.__instance is None:
            DatabaseConnection()
        return DatabaseConnection.__instance

    def close(self):
        self.connection.close()

    def get_all_rows(self, table_name):
        return self.format_data(table_name, self.get_all_rows_unformatted(table_name))

    def get_all_planned_disciplines(self):
        self.cursor.execute(
            "SELECT TS.id, TS.time, TS.weekday, D.name, T.name, SG.group_name, TS.is_course, TS.is_laboratory, TS.is_seminary, R.name, SG.year FROM TimeSlots TS JOIN Disciplines D on TS.discipline_id = D.id JOIN Teachers T on TS.teacher_id = T.id JOIN StudentGroups SG on TS.student_group_id = SG.id JOIN Rooms R on TS.room_id = R.id")
        return self.cursor.fetchall()

    def get_all_rows_unformatted(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def get_all_rows_by_column(self, table_name, column, value):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column} = {value}")
        rows = self.cursor.fetchall()
        return rows

    def get_all_rows_by_columns(self, table_name, column1, value1, column2, value2):
        assert table_name is not None and column1 is not None and value1 is not None \
               and column2 is not None and value2 is not None

        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column1} = {value1} AND {column2} = {value2}")
        rows = self.cursor.fetchall()
        return rows

    def get_all_rows_by_columns_3(self, table_name, column1, value1, column2, value2, column3, value3):
        self.cursor.execute(
            f"SELECT * FROM {table_name} WHERE {column1} = {value1} AND {column2} = {value2} AND {column3} = {value3}")
        rows = self.cursor.fetchall()
        return rows

    def insert_teacher(self, teacher: Teachers):
        assert teacher is not None
        if self.get_teacher(teacher):
            return 1
        query = f"INSERT INTO Teachers (name, title) VALUES " \
                f"('{teacher.name}', " \
                f"'{teacher.title}')"
        return self.execute_query(query)

    def insert_discipline(self, discipline: Disciplines):
        assert discipline is not None
        if self.get_discipline(discipline):
            return 1
        query = f"INSERT INTO Disciplines (name, semester, for_year_1, for_year_2, for_year_3, for_year_4, for_year_5, has_course, has_laboratory, has_seminary) VALUES " \
                f"('{discipline.name}', " \
                f"{discipline.semester}, " \
                f"{discipline.for_year1}, " \
                f"{discipline.for_year2}, " \
                f"{discipline.for_year3}, " \
                f"{discipline.for_year4}, " \
                f"{discipline.for_year5}, " \
                f"{discipline.has_course}, " \
                f"{discipline.has_laboratory}, " \
                f"{discipline.has_seminary})"
        return self.execute_query(query)

    def insert_group(self, group: StudentGroups):
        assert group is not None
        if self.get_student_group(group):
            return 1
        query = f"INSERT INTO StudentGroups (year, group_name) VALUES " \
                f"({group.year}, " \
                f"'{group.group_name}')"
        return self.execute_query(query)

    def insert_room(self, room):
        assert room is not None
        if self.get_room(room):
            print("Already exists")
            return 1
        query = f"INSERT INTO Rooms (name, can_host_course, can_host_laboratory, can_host_seminary) VALUES " \
                f"('{room.name}', " \
                f"{room.can_host_course}, " \
                f"{room.can_host_laboratory}, " \
                f"{room.can_host_seminary})"
        return self.execute_query(query)

    def insert_schedule(self, schedule: TimeSlots):
        assert schedule is not None

        query = f"INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, student_group_id, is_course, is_laboratory, is_seminary, room_id) VALUES " \
                f"('{schedule.time}', " \
                f"'{schedule.weekday}', " \
                f"{schedule.discipline}, " \
                f"{schedule.teacher}, " \
                f"{schedule.students}, " \
                f"{schedule.is_course}, " \
                f"{schedule.is_laboratory}, " \
                f"{schedule.is_seminary}, " \
                f"{schedule.room})"
        self.execute_query(query)

    def delete_entry(self, table, id):
        assert type(id) == int
        base_query = f"DELETE FROM {table} where id = {id}"
        self.execute_query(base_query)

        if table == 'Disciplines':
            reference_query = f"DELETE FROM TimeSlots where discipline_id = {id}"
        elif table == 'Rooms':
            reference_query = f"DELETE FROM TimeSlots where room_id = {id}"
        elif table == 'Teachers':
            reference_query = f"DELETE FROM TimeSlots where teacher_id = {id}"
        elif table == 'StudentGroups':
            reference_query = f"DELETE FROM TimeSlots where student_group_id = {id}"
        else:
            return
        self.execute_query(reference_query)

    def execute_query(self, query):
        try:
            print(f"Executed query: {query}")
            self.cursor.execute(query)
            self.connection.commit()
            return 0
        except Exception as e:
            print("Exception at insert" + str(e))
            return 2

    def get_teacher(self, teacher):
        return self.get_all_rows_by_column('Teachers', 'name', f"'{teacher.name}'") != []

    def get_discipline(self, discipline):
        return self.get_all_rows_by_column('Disciplines', 'name', f"'{discipline.name}'") != []

    def get_room(self, room: Rooms):
        print(self.get_all_rows_by_column('Rooms', 'name', f"'{room.name}'"))
        return self.get_all_rows_by_column('Rooms', 'name', f"'{room.name}'") != []

    def get_student_group(self, group):
        rows = self.get_all_rows_by_column('StudentGroups', 'group_name', f"'{group.group_name}'")
        print(rows)
        for row in rows:
            print(row)
            if str(row[1]) == str(group.year):
                return True
        return False

    def format_data(self, table_name, rows):
        assert table_name is not None and type(table_name) == str
        assert rows is not None and type(rows) == list

        if table_name == 'StudentGroups':
            return self.replace(rows, 1, Configuration.CONVERSION_YEARS_FOR_DB)
        elif table_name == 'Rooms':
            _ = self.replace(rows, 2, Configuration.CONVERSION_BOOLEAN_FOR_DB)
            _ = self.replace(_, 3, Configuration.CONVERSION_BOOLEAN_FOR_DB)
            return self.replace(_, 4, Configuration.CONVERSION_BOOLEAN_FOR_DB)
        elif table_name == 'Disciplines':
            _ = self.replace(rows, 8, Configuration.CONVERSION_BOOLEAN_FOR_DB)
            _ = self.replace(_, 9, Configuration.CONVERSION_BOOLEAN_FOR_DB)
            rows = self.replace(_, 10, Configuration.CONVERSION_BOOLEAN_FOR_DB)
            updated_rows = []
            for row in rows:
                updated_rows.append((row[0], row[1], DatabaseConnection.get_year(row), row[7], row[8], row[9], row[10]))
            return updated_rows
        elif table_name == 'TimeSlots':
            formatted = []
            for row in rows:
                _ = list(row)
                _[3] = self.get_all_rows_by_column("Disciplines", "id", _[3])[0][1]
                _[4] = self.get_all_rows_by_column("Teachers", "id", _[4])[0][1]

                student_group = self.get_all_rows_by_column("StudentGroups", "id", _[5])[0]
                if int(student_group[1]) > 3:
                    _[5] = student_group[2]
                else:
                    _[5] = f"{student_group[1]}{student_group[2]}"

                _[9] = self.get_all_rows_by_column("Rooms", "id", _[9])[0][1]

                class_type = "Curs" if _[6] else ("Laborator" if _[7] else "Seminar")
                _[6] = class_type
                del _[7]
                del _[7]

                formatted.append(_)
            return formatted
        else:
            pass
        return rows

    def replace(self, rows, index: int, values):
        assert rows != []
        assert index < len(rows)
        updated_rows = []
        for row in rows:
            updated_row = list(row)
            updated_row[index] = values[updated_row[index]]
            updated_rows.append(updated_row)
        return updated_rows

    @classmethod
    def get_year(cls, row):
        assert len(row) > 7

        if row[2] == 1:
            return Years.BACHELOR_YEAR_1
        if row[3] == 1:
            return Years.BACHELOR_YEAR_2
        if row[4] == 1:
            return Years.BACHELOR_YEAR_3
        if row[5] == 1:
            return Years.MASTER_YEAR_1
        if row[6] == 1:
            return Years.MASTER_YEAR_2
