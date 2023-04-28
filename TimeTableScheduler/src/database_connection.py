import sqlite3

from src.entities import Teachers, StudentGroups


class DatabaseConnection:
    converted_years_db = {
        1: "Year 1",
        2: "Year 2",
        3: "Year 3",
        4: "Master 1",
        5: "Master 2",
    }
    converted_boolean_db = {
        1: "Yes",
        0: "No"
    }
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
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        return self.format_data(table_name, rows)

    def get_all_rows_by_column(self, table_name, column, value):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column} = {value}")
        rows = self.cursor.fetchall()
        return rows

    def insert_teacher(self, teacher: Teachers):
        if self.get_teacher(teacher):
            return 1
        query = f"INSERT INTO Teachers (name, title) VALUES " \
                f"('{teacher.name}', " \
                f"'{teacher.title}')"
        return self.execute_query(query)

    def insert_discipline(self, discipline):
        query = f"INSERT INTO Disciplines (name, year, semester, has_course, has_laboratory, has_seminary) VALUES " \
                f"('{discipline.name}', " \
                f"{discipline.year}, " \
                f"{discipline.semester}, " \
                f"{discipline.has_course}, " \
                f"{discipline.has_laboratory}, " \
                f"{discipline.has_seminary})"
        return self.execute_query(query)

    def insert_group(self, group: StudentGroups):
        if self.get_student_group(group):
            return 1
        query = f"INSERT INTO StudentGroups (year, group_name) VALUES " \
                f"({group.year}, " \
                f"'{group.group_name}')"
        return self.execute_query(query)

    def insert_room(self, room):
        query = f"INSERT INTO Rooms (name, can_host_course, can_host_laboratory, can_host_seminary) VALUES " \
                f"('{room.name}', " \
                f"{room.can_host_course}, " \
                f"{room.can_host_laboratory}, " \
                f"{room.can_host_seminary})"
        self.execute_query(query)

    def execute_query(self, query):
        try:
            print(f"Executed query: {query}")
            self.cursor.execute(query)
            self.connection.commit()
            return 0
        except Exception as e:
            print(str(e))
            return 2

    def get_teacher(self, teacher):
        return self.get_all_rows_by_column('Teachers', 'name', f"'{teacher.name}'") != []

    def get_discipline(self, discipline):
        return self.get_all_rows_by_column('Disciplines', 'name', f"'{discipline.name}'") != []

    def get_room(self, room):
        return self.get_all_rows_by_column('Rooms', 'name', f"'{room.name}'") != []

    def get_student_group(self, group):
        rows = self.get_all_rows_by_column('StudentGroups', 'group_name', f"'{group.group_name}'")
        print(rows)
        for row in rows:
            print(row)
            if row[1] == group.year:
                return True
        return False

    def format_data(self, table_name, rows):
        if table_name == 'StudentGroups':
            return self.replace(rows, 1, DatabaseConnection.converted_years_db)
        elif table_name == 'Rooms':
            _ = self.replace(rows, 2, DatabaseConnection.converted_boolean_db)
            _ = self.replace(_, 3, DatabaseConnection.converted_boolean_db)
            return self.replace(_, 4, DatabaseConnection.converted_boolean_db)
        elif table_name == 'Disciplines':
            _ = self.replace(rows, 2, DatabaseConnection.converted_boolean_db)
            _ = self.replace(_, 3, DatabaseConnection.converted_boolean_db)
            return self.replace(_, 4, DatabaseConnection.converted_boolean_db)
        else:
            pass
        return rows

    def replace(self, rows, index: int, values):
        updated_rows = []
        for row in rows:
            updated_row = list(row)
            updated_row[index] = values[updated_row[index]]
            updated_rows.append(updated_row)
        return updated_rows
