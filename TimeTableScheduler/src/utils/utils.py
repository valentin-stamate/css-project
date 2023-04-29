import tkinter as tk
from tkinter import messagebox

from src.database_connection import DatabaseConnection
from src.entities import *


class Utils:
    converted_years_ui = {
        "Year 1": 1,
        "Year 2": 2,
        "Year 3": 3,
        "Master 1": 4,
        "Master 2": 5
    }

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
        return Utils.converted_years_ui[year]


