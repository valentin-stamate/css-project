import tkinter as tk
from tkinter import ttk

from src.database_connection import DatabaseConnection


class SchedulerApp:
    WIDTH = 1200
    HEIGHT = 600
    TABS = 5

    def __init__(self, master):
        self.master = master
        self.master.title("Scheduler App")
        self.notebook = ttk.Notebook(self.master, width=SchedulerApp.WIDTH, height=SchedulerApp.HEIGHT)
        self.notebook.pack(fill="both", expand=True)
        self.current_tab = None
        style = ttk.Style()
        style.configure("myStyle.TNotebook", tabposition="n", font=("TkDefaultFont", 26))
        self.notebook.configure(style="myStyle.TNotebook")

        # create tabs
        self.create_tab_and_display_db_table("Student Groups", "StudentGroups")
        self.create_tab_and_display_db_table("Teachers", "Teachers")
        self.create_tab_and_display_db_table("Disciplines", "Disciplines")
        self.create_tab_and_display_db_table("Rooms", "Rooms")
        self.create_tab_and_display_db_table("Schedules", "TimeSlots")

    def create_tab_and_display_db_table(self, name: str, table: str):
        tab = tk.Frame(self.notebook)
        tab.pack(side="top")

        inner_frame = tk.Frame(tab)
        inner_frame.pack()

        rows = DatabaseConnection.get_instance().get_all_rows(table)
        number_of_columns = len(rows[0]) if len(rows) > 0 else 1

        tree = ttk.Treeview(inner_frame, columns=[f"c{i + 1}" for i in range(0, number_of_columns)], show='headings',
                            height=(SchedulerApp.HEIGHT - 50))
        for row in rows:
            tree.insert("", tk.END, values=row)
        tree.pack()

        self.notebook.add(tab, text=f"{name}")
        self.select_tab(tab)

    def select_tab(self, tab):
        # select the given tab and set it as the current tab
        self.notebook.select(tab)
        self.current_tab = tab

    @staticmethod
    def start():
        root = tk.Tk()
        SchedulerApp(root)
        root.mainloop()
