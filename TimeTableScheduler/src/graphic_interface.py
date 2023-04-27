import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from src.database_connection import DatabaseConnection
from src.enums.Semesters import Semesters
from src.enums.Years import Years
from src.service.filter_service import get_disciplines_for_year_and_semester
from src.utils.utils import Utils


class SchedulerApp:
    WIDTH = 1200
    HEIGHT = 600
    TABS = 5
    HEADINGS = {
        "Student Groups": ["ID", "Year", "Name"],
        "Teachers": ["ID", "Name", "Title"],
        "Disciplines": ["ID", "Name", "Has Course", "Has Laboratory", "Has Seminary"],
        "Rooms": ["ID", "Name", "Can Host Course", "Can Host Laboratory", "Can Host Seminary"],
        "Schedules": ["ID", "Time", "Weekday", "Discipline", "Teacher", "Students"],
    }

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

        self.create_admin_tab()

    def create_admin_tab(self):
        name = "Schedule class"

        tab = tk.Frame(self.notebook)
        tab.pack(side="top")

        inner_frame = tk.Frame(tab)
        inner_frame.pack()

        # Create vars
        self.semester_var = tk.StringVar(inner_frame)
        self.semester_var.trace('w', self.update_discipline_options)

        self.year_var = tk.StringVar(inner_frame)
        self.year_var.trace('w', self.update_discipline_options)

        self.discipline_var = tk.StringVar(inner_frame)

        # Choosing semester
        semester_label = tk.Label(inner_frame, text="Semestrul")
        semester_label.pack()

        self.semester_var.set(Semesters.get_default_value())
        self.semester_menu = tk.OptionMenu(inner_frame, self.semester_var, *Semesters.get_all_values())
        self.semester_menu.pack()

        # Choosing year
        year_label = tk.Label(inner_frame, text="Anul")
        year_label.pack()

        self.year_var.set(Years.get_default_value())
        self.year_menu = tk.OptionMenu(inner_frame, self.year_var, *Years.get_all_values())
        self.year_menu.pack()

        # Choosing discipline
        discipline_label = tk.Label(inner_frame, text="Disciplina")
        discipline_label.pack()

        self.discipline_var.set('')
        self.discipline_menu = tk.OptionMenu(inner_frame, self.discipline_var, '')
        self.discipline_menu.pack()

        self.notebook.add(tab, text=f"{name}")
        self.select_tab(tab)

        self.update_discipline_options()

    def update_discipline_options(self, *args):
        try:
            semester = self.semester_var.get()
            year = self.year_var.get()

            disciplines = get_disciplines_for_year_and_semester(year, semester)

            menu = self.discipline_menu['menu']
            menu.delete(0, 'end')
            self.discipline_var.set(disciplines[0])
            for discipline in disciplines:
                menu.add_command(label=discipline, command=lambda d=discipline: self.discipline_var.set(d))
        except:
            pass

    def create_tab_and_display_db_table(self, name: str, table: str):
        tab = tk.Frame(self.notebook)
        tab.pack(side="top", pady=10)

        form_frame = tk.Frame(tab)
        form_frame.pack(side='top')

        data_frame = tk.Frame(tab)

        rows = DatabaseConnection.get_instance().get_all_rows(table)
        number_of_columns = len(rows[0]) if len(rows) > 0 else 1

        tree = ttk.Treeview(data_frame, columns=[f"c{i + 1}" for i in range(0, number_of_columns)], show='headings',
                            height=(SchedulerApp.HEIGHT - 50))
        tree['columns'] = tuple(SchedulerApp.HEADINGS[name])
        for index, heading in enumerate(SchedulerApp.HEADINGS[name]):
            tree.heading(index, text=heading)

        Utils.load_data(tree, rows)

        self.create_insert_form(data_frame, name, tree)
        self.notebook.add(tab, text=f"{name}")
        self.select_tab(tab)
        data_frame.pack()
        tree.pack()

    def select_tab(self, tab):
        # select the given tab and set it as the current tab
        self.notebook.select(tab)
        self.current_tab = tab

    @staticmethod
    def start():
        root = tk.Tk()
        SchedulerApp(root)
        root.mainloop()

    def create_insert_form(self, frame, name, tree):
        add_font = Font(size=13)
        if name == "Student Groups":
            pass
        elif name == "Teachers":
            add_label = tk.Label(frame, text="Add teacher:", font=add_font)
            name_label = tk.Label(frame, text="Name:")
            name_entry = tk.Entry(frame)
            add_label.pack(pady=5)
            name_label.pack(pady=2)
            name_entry.pack(pady=2)

            title_label = tk.Label(frame, text="Title:")
            title_entry = tk.Entry(frame)
            title_label.pack(pady=2)
            title_entry.pack(pady=2)

            add_button = tk.Button(frame, text="Add", command=lambda: Utils.add_teacher(name_entry, title_entry, tree))
            add_button.pack(pady=10)
        elif name == "Disciplines":
            pass
        elif name == "Rooms":
            pass
        elif name == "Schedules":
            pass
        else:
            print('invalid option')
