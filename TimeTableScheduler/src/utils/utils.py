import tkinter as tk
from tkinter import messagebox

from src.database_connection import DatabaseConnection
from src.entities import Teachers


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
                Utils.popup('Succes', "Teacher added")
                Utils.load_data(tree, Utils.database_connection.get_all_rows("Teachers"))
            elif status == 1:
                Utils.popup('Failed', "Teacher already exists")
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
