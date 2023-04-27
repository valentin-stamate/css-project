import sqlite3

from src.entities import Teachers


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
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        return rows

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
        self.execute_query(query)

    def insert_group(self, students):
        query = f"INSERT INTO students (year, student_group) VALUES " \
                f"({students.year}, " \
                f"'{students.student_group}')"
        self.execute_query(query)

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
