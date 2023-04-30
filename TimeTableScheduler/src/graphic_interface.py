import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from src.database_connection import DatabaseConnection
from src.enums.ClassTypes import ClassTypes
from src.enums.Configuration import Configuration
from src.enums.Semesters import Semesters
from src.enums.Years import Years
from src.service.filter_service import get_disciplines_for_year_and_semester, get_student_groups_in_year, \
    get_available_slots_for_teacher_and_student_group, get_available_rooms_for_time_slot_and_class_type
from src.utils.utils import Utils


class SchedulerApp:

    def __init__(self, master):
        self.selected_semester = None
        self.selected_year = None
        self.master = master
        self.master.title("Scheduler App")
        self.notebook = ttk.Notebook(self.master, width=Configuration.WIDTH, height=Configuration.HEIGHT)
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

        self.create_schedule_class_tab()

    def create_schedule_class_tab(self):
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
        self.discipline_var.trace('w', self.update_student_group_options)

        self.student_group_var = tk.StringVar(inner_frame)
        self.student_group_var.trace('w', self.update_time_slot_options)

        self.teacher_var = tk.StringVar(inner_frame)
        self.teacher_var.trace('w', self.update_time_slot_options)

        self.time_slot_var = tk.StringVar(inner_frame)
        self.time_slot_var.trace('w', self.update_room_options)

        self.class_type_var = tk.StringVar(inner_frame)
        self.class_type_var.trace('w', self.update_room_options)

        self.room_var = tk.StringVar(inner_frame)

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

        # Choosing group
        student_group_label = tk.Label(inner_frame, text="Grupa")
        student_group_label.pack()

        self.student_group_var.set('')
        self.student_group_menu = tk.OptionMenu(inner_frame, self.student_group_var, '')
        self.student_group_menu.pack()

        # Choosing teacher
        teacher_group_label = tk.Label(inner_frame, text="Profesorul")
        teacher_group_label.pack()

        all_teachers = DatabaseConnection.get_instance().get_all_rows('Teachers')
        all_teachers = [f"{teacher[1]}, {teacher[2]}" for teacher in all_teachers]
        self.teacher_var.set(all_teachers[0])
        self.teacher_menu = tk.OptionMenu(inner_frame, self.teacher_var, *all_teachers)
        self.teacher_menu.pack()

        # Choosing weekday
        weekday_label = tk.Label(inner_frame, text="Ziua si ora")
        weekday_label.pack()

        self.time_slot_var.set('')
        self.time_slot_menu = tk.OptionMenu(inner_frame, self.time_slot_var, '')
        self.time_slot_menu.pack()

        # Choosing class type
        class_type_label = tk.Label(inner_frame, text="Tipul orei")
        class_type_label.pack()

        self.class_type_var.set('Curs')
        self.class_type_menu = tk.OptionMenu(inner_frame, self.class_type_var, 'Curs', 'Laborator', 'Seminar')
        self.class_type_menu.pack()

        # Choosing room
        room_label = tk.Label(inner_frame, text="Sala")
        room_label.pack()

        self.room_var.set('')
        self.room_type_menu = tk.OptionMenu(inner_frame, self.room_var, '')
        self.room_type_menu.pack()

        # Add button
        add_button = tk.Button(inner_frame, text="Add",
                               command=lambda: Utils.add_schedule(self.discipline_var.get(),
                                                                  self.student_group_var.get(),
                                                                  self.teacher_var.get(),
                                                                  self.time_slot_var.get(),
                                                                  self.class_type_var.get(),
                                                                  self.room_var.get())
                               )
        add_button.pack(pady=10)

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
        except Exception as e:
            print(f"Exception raised: {e}")
            pass

    def update_student_group_options(self, *args):
        try:
            year = self.year_var.get()

            student_groups = get_student_groups_in_year(year)

            menu = self.student_group_menu['menu']
            menu.delete(0, 'end')
            self.student_group_var.set(student_groups[0])
            for student_group in student_groups:
                menu.add_command(label=student_group, command=lambda d=student_group: self.student_group_var.set(d))
        except Exception as e:
            print(f"Exception raised: {e}")
            pass

    def update_time_slot_options(self, *args):
        try:
            teacher = self.teacher_var.get()
            student_group = self.student_group_var.get()

            time_slots = get_available_slots_for_teacher_and_student_group(teacher, student_group)

            menu = self.time_slot_menu['menu']
            menu.delete(0, 'end')
            self.time_slot_var.set(time_slots[0])
            for time_slot in time_slots:
                menu.add_command(label=time_slot, command=lambda d=time_slot: self.time_slot_var.set(d))
        except Exception as e:
            print(f"Exception raised: {e}")
            pass

    def update_room_options(self, *args):
        try:
            time_slot = self.time_slot_var.get()
            class_type = self.class_type_var.get()

            rooms = get_available_rooms_for_time_slot_and_class_type(
                time_slot, (class_type == 'Curs'), (class_type == 'Laborator'), (class_type == 'Seminar')
            )

            menu = self.room_type_menu['menu']
            menu.delete(0, 'end')
            self.room_var.set(rooms[0])
            for room in rooms:
                menu.add_command(label=room, command=lambda d=room: self.room_var.set(d))
        except Exception as e:
            print(f"Exception raised: {e}")
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
                            height=(Configuration.HEIGHT - 50))
        tree['columns'] = tuple(Configuration.HEADINGS[name])
        for index, heading in enumerate(Configuration.HEADINGS[name]):
            tree.heading(index, text=heading)

        for key in Configuration.COLUMN_WIDTHS[name].keys():
            tree.column(key, width=Configuration.COLUMN_WIDTHS[name][key])

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

            add_label = tk.Label(frame, text="Add student group:", font=add_font)
            values = ["Anul 1", "Anul 2", "Anul 3", "Master Anul 1", "Master Anul 2"]
            selected_value = tk.StringVar()
            year_dropdown = ttk.Combobox(frame, textvariable=selected_value, values=values)
            year_dropdown.bind("<<ComboboxSelected>>", self.on_select_year)
            year_label = tk.Label(frame, text="Year:")
            add_label.pack(pady=5)
            year_label.pack(pady=2)
            year_dropdown.pack(pady=2)

            name_label = tk.Label(frame, text="Name:")
            name_entry = tk.Entry(frame)
            name_label.pack(pady=2)
            name_entry.pack(pady=2)

            add_button = tk.Button(frame, text="Add",
                                   command=lambda: Utils.add_student_group(self.selected_year, name_entry, tree))
            add_button.pack(pady=10)
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
            add_label = tk.Label(frame, text="Add Discipline:", font=add_font)
            semester_values = Semesters.get_all_values()
            year_values = Years.get_all_values()
            selected_value = tk.StringVar(value=Years.get_default_value())
            year_dropdown = ttk.Combobox(frame, textvariable=selected_value, values=year_values)
            year_dropdown.bind("<<ComboboxSelected>>", self.on_select_year)
            # selected_value.set(Years.get_default_value())
            year_label = tk.Label(frame, text="Year:")
            add_label.pack(pady=5)
            year_label.pack(pady=2)
            year_dropdown.pack(pady=2)
            selected_value = tk.StringVar()
            semester_dropdown = ttk.Combobox(frame, textvariable=selected_value, values=semester_values)
            semester_dropdown.bind("<<ComboboxSelected>>", self.on_select_semester)
            selected_value.set(Semesters.get_default_value())
            year_label = tk.Label(frame, text="Semester:")
            add_label.pack(pady=5)
            year_label.pack(pady=2)
            semester_dropdown.pack(pady=2)

            name_label = tk.Label(frame, text="Name:")
            name_entry = tk.Entry(frame)
            name_label.pack(pady=2)
            name_entry.pack(pady=2)
            has_course_var = tk.IntVar()
            has_laboratory_var = tk.IntVar()
            has_seminary_var = tk.IntVar()
            course = tk.Checkbutton(frame, text=f'   {ClassTypes.COURSE}  ', variable=has_course_var)
            laboratory = tk.Checkbutton(frame, text=f'{ClassTypes.LABORATORY}', variable=has_laboratory_var)
            seminary = tk.Checkbutton(frame, text=f' {ClassTypes.SEMINARY} ', variable=has_seminary_var)

            # Pack the checkbox into the window
            course.pack()
            laboratory.pack()
            seminary.pack()

            add_button = tk.Button(frame, text="Add",
                                   command=lambda: Utils.add_discipline(name_entry, self.selected_year,
                                                                        self.selected_semester, has_course_var,
                                                                        has_laboratory_var, has_seminary_var, tree))
            add_button.pack(pady=10)
        elif name == "Rooms":
            pass
        elif name == "Schedules":
            pass
        else:
            print('invalid option')

    def on_select_year(self, event):
        selected_value = event.widget.get()
        print(f"Selected year value: {selected_value}")
        self.selected_year = selected_value

    def on_select_semester(self, event):
        selected_value = event.widget.get()
        print(f"Selected semester value: {selected_value}")
        self.selected_semester = selected_value
