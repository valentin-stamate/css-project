import csv
import tkinter as tk
from tkinter import messagebox

from src.database_connection import DatabaseConnection
from src.entities import *
from src.enums.Configuration import Configuration
from src.enums.Years import Years
from src.service.models import ProgrammedClass


class Utils:
    database_connection = DatabaseConnection.get_instance()

    @staticmethod
    def add_teacher(name_entry, title_entry, tree, table,timeslots_tree):
        name_val = name_entry.get()
        title_val = title_entry.get()
        if name_val != '' and title_val != '':
            new_teacher = Teachers(name=name_val, title=title_val)
            print(new_teacher.name)
            print(new_teacher.title)
            status = Utils.database_connection.insert_teacher(new_teacher)
            if status == 0:
                name_entry.delete(0, tk.END)
                title_entry.delete(0, tk.END)
                Utils.popup('Success', "Teacher added")
                Utils.load_data(tree, table)
                if timeslots_tree is not None:
                    print("reloading Schedule tree")
                    Utils.load_data(timeslots_tree, 'TimeSlots')
            elif status == 1:
                Utils.popup('Failed', "Teacher already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @staticmethod
    def add_student_group(year, name_entry, tree, table,timeslots_tree):
        print(f"Year val {year}")
        year_val = Utils.convert_year(year)
        name_val = name_entry.get()
        if year_val != '' and name_val != '':
            new_group = StudentGroups(year=year_val, group_name=name_val)
            status = Utils.database_connection.insert_group(new_group)
            if status == 0:
                # year_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                Utils.popup('Success', "Student Group added")
                Utils.load_data(tree, table)
                if timeslots_tree is not None:
                    print("reloading Schedule tree")
                    Utils.load_data(timeslots_tree, 'TimeSlots')
            elif status == 1:
                Utils.popup('Failed', "Student Group already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @classmethod
    def add_discipline(cls, name_entry, year, semester, has_course, has_laboratory,
                       has_seminary, tree, table,timeslots_tree):

        year_val = Utils.convert_year(year)
        for_years = Utils.format_all_years(year_val)
        semester_val = Utils.convert_semester(semester)
        name_val = name_entry.get()
        has_course_val = has_course.get()
        has_laboratory_val = has_laboratory.get()
        has_seminary_val = has_seminary.get()
        print(f'{has_course_val}{has_laboratory_val}{has_seminary_val}')
        if year_val != '' and name_val != '' and semester_val != '' and has_seminary_val + has_course_val + has_seminary_val != 0:
            new_discipline = Disciplines(name=name_val, semester=semester_val, for_year1=for_years[0],
                                         for_year2=for_years[1], for_year3=for_years[2], for_year4=for_years[3],
                                         for_year5=for_years[4], has_course=has_course_val,
                                         has_laboratory=has_laboratory_val, has_seminary=has_seminary_val)
            status = Utils.database_connection.insert_discipline(new_discipline)
            if status == 0:
                # year_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                Utils.popup('Success', "Discipline Added")
                Utils.load_data(tree, table)
                if timeslots_tree is not None:
                    print("reloading Schedule tree")
                    Utils.load_data(timeslots_tree, 'TimeSlots')
            elif status == 1:
                Utils.popup('Failed', "Discipline already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @classmethod
    def add_room(cls, name_entry, for_course, for_laboratory, for_seminary, tree, table,timeslots_tree):
        name_val = name_entry.get()
        for_course_val = for_course.get()
        for_laboratory_val = for_laboratory.get()
        for_seminary_val = for_seminary.get()
        print(f'{for_course_val}{for_laboratory_val}{for_seminary_val}')
        if name_val != '' and for_seminary_val + for_course_val + for_seminary_val != 0:
            new_room = Rooms(name=name_val, can_host_course=for_course_val, can_host_laboratory=for_laboratory_val,
                             can_host_seminary=for_seminary_val)
            status = Utils.database_connection.insert_room(new_room)
            print(status)
            if status == 0:
                # year_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                Utils.popup('Success', "Room Added")
                Utils.load_data(tree, table)
                if timeslots_tree is not None:
                    print("reloading Schedule tree")
                    Utils.load_data(timeslots_tree, 'TimeSlots')
            elif status == 1:
                Utils.popup('Failed', "Room already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @staticmethod
    def add_schedule(discipline, student_group, teacher, time_slot, class_type, room, timeslots_tree):
        assert discipline is not None and type(discipline) == str
        assert teacher is not None and type(teacher) == str
        assert time_slot is not None and type(time_slot) == str
        assert class_type is not None and type(class_type) == str
        assert room is not None and type(room) == str
        assert room is not None and type(room) == str

        if len(discipline.strip()) == 0 or len(student_group.strip()) == 0 or \
                len(teacher.strip()) == 0 or len(time_slot.strip()) == 0 or \
                len(class_type.strip()) == 0 or len(room.strip()) == 0:
            Utils.popup('Invalid data', "At least one input field is empty")

        discipline_id = Utils.get_discipline_id_by_name(discipline)
        student_group_ids = Utils.get_student_group_ids_by_name(student_group)
        teacher_id = Utils.get_teacher_id_by_name(teacher)
        weekday = time_slot.split(", ")[0].strip()
        time_period = time_slot.split(", ")[1].strip()
        room_id = Utils.get_room_id_by_name(room)
        for student_group_id in student_group_ids:
            new_time_slot = TimeSlots(time=time_period, weekday=weekday, discipline=discipline_id,
                                      teacher=teacher_id, students=student_group_id, is_course=(class_type == "Curs"),
                                      is_laboratory=(class_type == "Laborator"), is_seminary=(class_type == "Seminar"),
                                      room=room_id)
            Utils.database_connection.insert_schedule(new_time_slot)
        if timeslots_tree is not None:
            print("reloading Schedule tree")
            Utils.load_data(timeslots_tree, 'TimeSlots')

    @staticmethod
    def get_discipline_id_by_name(discipline_name):
        assert discipline_name is not None and type(discipline_name) == str

        disciplines = Utils.database_connection.get_all_rows_unformatted("Disciplines")

        assert disciplines is not None

        for discipline in disciplines:
            if discipline[1] == discipline_name:
                return discipline[0]

        return 0

    @staticmethod
    def get_student_group_ids_by_name(student_group_name) -> [int]:
        assert student_group_name is not None and type(student_group_name) == str

        if student_group_name.strip() == '':
            return []

        if Years.is_any_year(student_group_name):
            year_index = Years.get_year_index(student_group_name)
            matched_student_group_entities = DatabaseConnection.get_instance().get_all_rows_by_column(
                "StudentGroups", "year", f"{year_index}"
            )

            return [int(entity[0]) for entity in matched_student_group_entities]

        if "M" in student_group_name:
            matched_student_group_entities = Utils.database_connection.get_all_rows_by_column(
                "StudentGroups", "group_name", f"\"{student_group_name}\""
            )
        else:
            year = student_group_name[0]
            student_group_name = student_group_name[1:]

            matched_student_group_entities = Utils.database_connection.get_all_rows_by_columns(
                "StudentGroups", "group_name", f"\"{student_group_name}\"", "year", year
            )

        assert matched_student_group_entities is not None

        if len(matched_student_group_entities) == 0:
            raise Exception(f"Couldn't find group \"{student_group_name}\" in database.")

        return [int(matched_student_group_entities[0][0])]

    @staticmethod
    def get_teacher_id_by_name(teacher_with_name_and_title):
        assert teacher_with_name_and_title is not None and type(teacher_with_name_and_title) == str

        if teacher_with_name_and_title.strip() == '':
            return 1

        teacher_name = teacher_with_name_and_title.split(", ")[0].strip()
        teacher_title = teacher_with_name_and_title.split(", ")[1].strip()

        matched_teacher_entities = Utils.database_connection.get_all_rows_by_columns(
            "Teachers", "name", f"\"{teacher_name}\"", "title", f"\"{teacher_title}\""
        )

        assert matched_teacher_entities is not None

        if len(matched_teacher_entities) == 0:
            raise Exception(f"Couldn't find teacher \"{teacher_with_name_and_title}\" in database.")

        return int(matched_teacher_entities[0][0])

    @staticmethod
    def get_room_id_by_name(room_name):
        assert room_name is not None and type(room_name) == str

        rooms = Utils.database_connection.get_all_rows_unformatted("Rooms")

        assert rooms is not None

        for room in rooms:
            if room[1] == room_name:
                return room[0]

        return 0

    @staticmethod
    def popup(popup_type, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(popup_type, message)

    @classmethod
    def load_data(cls, tree, table):
        print(f"Loading data for {table}")
        tree.delete(*tree.get_children())
        rows = Utils.database_connection.get_instance().get_all_rows(table)
        for row in rows:
            tree.insert("", tk.END, values=row)

    @classmethod
    def convert_year(cls, year):
        print(year)
        return Configuration.CONVERSION_YEARS_FOR_UI[year]

    @classmethod
    def convert_semester(cls, semester):
        return semester[-1]

    @classmethod
    def format_all_years(cls, year):
        print(f"Format {year}")
        if year == 1:
            return 1, 0, 0, 0, 0
        elif year == 2:
            return 0, 1, 0, 0, 0
        elif year == 3:
            return 0, 0, 1, 0, 0
        elif year == 4:
            return 0, 0, 0, 1, 0
        elif year == 5:
            return 0, 0, 0, 0, 1
        else:
            print("No valid year was found to be inserted for Discipline")
            return 1, 0, 0, 0, 0

    @classmethod
    def delete_entry(cls, tree, table, timeslots_tree=None):
        selected_items = tree.selection()
        if len(selected_items) == 0:
            Utils.popup("Error", "At least one row must be selected for deletion")
        else:
            for item in selected_items:
                item_values = tree.item(item)['values']
                entry_id = item_values[0]
                print(f"Table {table}, id = {entry_id}")
                Utils.database_connection.delete_entry(table=table, id=entry_id)
            Utils.load_data(tree, table)
            if timeslots_tree is not None:
                print("reloading Schedule tree")
                Utils.load_data(timeslots_tree, 'TimeSlots')

    @classmethod
    def load_student_group_file(cls, tree, name):
        rows = Utils.load_file(name)
        if len(rows) == 0:
            Utils.popup("Error", f'File not found /data/{name.lower()}.csv')
        elif len(rows[0]) != 2:
            Utils.popup("Invalid Input", f'File /data/{name.lower()}.csv should only have 2 columns')
        else:
            error_rows = []
            for row in rows:
                if len(row) != 2:
                    error_rows.append((row, "Invalid number of columns"))
                else:
                    new_group = StudentGroups(row[0], row[1])
                    status = Utils.database_connection.insert_group(new_group)
                    if status != 0:
                        error_rows.append((row, "Already exists"))
            Utils.load_data(tree, name)
            Utils.show_load_status(error_rows)

    @classmethod
    def load_teacher_file(cls, tree, name):
        rows = Utils.load_file(name)
        if len(rows) == 0:
            Utils.popup("Error", f'File not found /data/{name.lower()}.csv')
        elif len(rows[0]) != 2:
            Utils.popup("Invalid Input", f'File /data/{name.lower()}.csv should only have 2 columns')
        else:
            error_rows = []
            for row in rows:
                if len(row) != 2:
                    error_rows.append((row, "Invalid number of columns"))
                else:
                    new_teacher = Teachers(row[0], row[1])
                    status = Utils.database_connection.insert_teacher(new_teacher)
                    if status != 0:
                        error_rows.append((row, "Already exists"))
            Utils.load_data(tree, name)
            Utils.show_load_status(error_rows)

    @classmethod
    def load_discipline_file(cls, tree, name):
        rows = Utils.load_file(name)
        if len(rows) == 0:
            Utils.popup("Error", f'File not found /data/{name.lower()}.csv')
        elif len(rows[0]) != 10:
            Utils.popup("Invalid Input", f'File /data/{name.lower()}.csv should only have 2 columns')
        else:
            error_rows = []
            for row in rows:
                if len(row) != 10:
                    error_rows.append((row, "Invalid number of columns"))
                else:
                    new_discipline = Disciplines(row[0], row[1], row[2], row[3], row[4],
                                                 row[5], row[6], row[7], row[8], row[9])
                    status = Utils.database_connection.insert_discipline(new_discipline)
                    if status != 0:
                        error_rows.append((row, "Already exists"))
            Utils.load_data(tree, name)
            Utils.show_load_status(error_rows)

    @classmethod
    def load_room_file(cls, tree, name):
        rows = Utils.load_file(name)
        if len(rows) == 0:
            Utils.popup("Error", f'File not found /data/{name.lower()}.csv')
        elif len(rows[0]) != 4:
            Utils.popup("Invalid Input", f'File /data/{name.lower()}.csv should only have 2 columns')
        else:
            error_rows = []
            for row in rows:
                if len(row) != 4:
                    error_rows.append((row, "Invalid number of columns"))
                else:
                    new_group = Rooms(row[0], row[1], row[1], row[1])
                    status = Utils.database_connection.insert_room(new_group)
                    if status != 0:
                        error_rows.append((row, "Already exists"))
            Utils.load_data(tree, name)
            Utils.show_load_status(error_rows)

    @classmethod
    def load_file(cls, name: str):
        print(f"Load file for {name}")
        try:
            with open(f'data/{name.lower()}.csv') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = []
                for row in csv_reader:
                    rows.append(row)
                return rows[1:]
        except FileNotFoundError as _:
            return []

    @classmethod
    def show_load_status(cls, error_rows):
        if len(error_rows) != 0:
            message = ''
            for row in error_rows:
                message += f"Row {row[0]} could not be inserted. {row[1]}\n"
            Utils.popup("Error", message)
        else:
            Utils.popup("Success", f"Data loaded into the database")

    @staticmethod
    def planned_disciplines_rows_to_objects(rows):
        planned_disciplines = []

        for discipline in rows:
            time = discipline[1]

            from_ = time.split(' - ')[0]
            to = time.split(' - ')[1]

            disciple_type = [discipline[6], discipline[7], discipline[8]]
            disciple_types = ['Curs', 'Laborator', 'Seminar']

            type_ = ''

            for i in range(len(disciple_types)):
                dt = int(disciple_type[i])

                if dt == 1:
                    type_ = disciple_types[i]

            discipline = ProgrammedClass(discipline[2], from_, to, discipline[5], int(discipline[10]), discipline[3],
                                         type_, [discipline[4]], discipline[9])
            planned_disciplines.append(discipline)

        return planned_disciplines
