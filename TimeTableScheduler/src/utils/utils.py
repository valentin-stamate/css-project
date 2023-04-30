import tkinter as tk
from tkinter import messagebox

from src.database_connection import DatabaseConnection
from src.entities import *
from src.enums.Configuration import Configuration


class Utils:
    database_connection = DatabaseConnection.get_instance()

    @staticmethod
    def add_teacher(name_entry, title_entry, tree):
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
                Utils.load_data(tree, Utils.database_connection.get_all_rows("Teachers"))
            elif status == 1:
                Utils.popup('Failed', "Teacher already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @staticmethod
    def add_student_group(year, name_entry, tree):
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
                Utils.load_data(tree, Utils.database_connection.get_all_rows("StudentGroups"))
            elif status == 1:
                Utils.popup('Failed', "Student Group already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @classmethod
    def add_discipline(cls, name_entry, year, semester, has_course, has_laboratory,
                       has_seminary, tree):

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
                Utils.load_data(tree, Utils.database_connection.get_all_rows("Disciplines"))
            elif status == 1:
                Utils.popup('Failed', "Discipline already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @classmethod
    def add_room(cls, name_entry, for_course, for_laboratory, for_seminary, tree):
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
                Utils.load_data(tree, Utils.database_connection.get_all_rows("Rooms"))
            elif status == 1:
                Utils.popup('Failed', "Room already exists")
            else:
                Utils.popup('Error', "Internal Error")
        else:
            Utils.popup('Invalid data', "At least one input field is empty")

    @staticmethod
    def add_schedule(discipline, student_group, teacher, time_slot, class_type, room):
        if len(discipline.strip()) == 0 or len(student_group.strip()) == 0 or \
                len(teacher.strip()) == 0 or len(time_slot.strip()) == 0 or \
                len(class_type.strip()) == 0 or len(room.strip()) == 0:
            Utils.popup('Invalid data', "At least one input field is empty")

        discipline_id = Utils.get_discipline_id_by_name(discipline)
        student_group_id = Utils.get_student_group_id_by_name(student_group)
        teacher_id = Utils.get_teacher_id_by_name(teacher)
        weekday = time_slot.split(", ")[0].strip()
        time_period = time_slot.split(", ")[1].strip()
        room_id = Utils.get_room_id_by_name(room)

        new_time_slot = TimeSlots(time=time_period, weekday=weekday, discipline=discipline_id,
                                  teacher=teacher_id, students=student_group_id, is_course=(class_type == "Curs"),
                                  is_laboratory=(class_type == "Laborator"), is_seminary=(class_type == "Seminar"),
                                  room=room_id)
        Utils.database_connection.insert_schedule(new_time_slot)

    @staticmethod
    def get_discipline_id_by_name(discipline_name):
        disciplines = Utils.database_connection.get_all_rows_unformatted("Disciplines")

        for discipline in disciplines:
            if discipline[1] == discipline_name:
                return discipline[0]

        return 0

    @staticmethod
    def get_student_group_id_by_name(student_group_name):
        if student_group_name.strip() == '':
            return 1

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

        if len(matched_student_group_entities) == 0:
            raise Exception(f"Couldn't find group \"{student_group_name}\" in database.")

        return int(matched_student_group_entities[0][0])

    @staticmethod
    def get_teacher_id_by_name(teacher_with_name_and_title):
        if teacher_with_name_and_title.strip() == '':
            return 1

        teacher_name = teacher_with_name_and_title.split(", ")[0].strip()
        teacher_title = teacher_with_name_and_title.split(", ")[1].strip()

        matched_teacher_entities = Utils.database_connection.get_all_rows_by_columns(
            "Teachers", "name", f"\"{teacher_name}\"", "title", f"\"{teacher_title}\""
        )
        if len(matched_teacher_entities) == 0:
            raise Exception(f"Couldn't find teacher \"{teacher_with_name_and_title}\" in database.")

        return int(matched_teacher_entities[0][0])

    @staticmethod
    def get_room_id_by_name(room_name):
        rooms = Utils.database_connection.get_all_rows_unformatted("Rooms")

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
    def load_data(cls, tree, data):
        tree.delete(*tree.get_children())
        for row in data:
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
        if year == 1:
            return 1, 0, 0, 0, 0
        elif year == 2:
            return 1, 0, 0, 0, 0
        elif year == 3:
            return 1, 0, 0, 0, 0
        elif year == 4:
            return 1, 0, 0, 0, 0
        elif year == 5:
            return 1, 0, 0, 0, 0
        else:
            print("No valid year was found to be inserted for Discipline")
            return 0, 0, 0, 0, 0
