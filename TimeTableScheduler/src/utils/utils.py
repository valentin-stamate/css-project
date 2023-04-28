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


