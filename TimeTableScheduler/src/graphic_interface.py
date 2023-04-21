import tkinter as tk
from tkinter import ttk


class SchedulerApp:
    WIDTH = 1200
    TABS = 5

    def __init__(self, master):
        self.master = master
        self.master.title("Scheduler App")
        self.notebook = ttk.Notebook(self.master, width=SchedulerApp.WIDTH)
        self.notebook.pack(fill="both", expand=True)
        self.current_tab = None
        style = ttk.Style()
        style.configure("myStyle.TNotebook", tabposition="n", font=("TkDefaultFont", 26))
        self.notebook.configure(style="myStyle.TNotebook")

        # create tabs
        self.create_tab("Students")
        self.create_tab("Teachers")
        self.create_tab("Disciplines")
        self.create_tab("Rooms")
        self.create_tab("Schedule")

    def create_tab(self, name):
        # create a new tab with a text widget for content
        tab = tk.Frame(self.notebook)
        tab.pack(side="top")
        label = tk.Label(tab, width=40, height=30)
        label.pack(side="top")
        inner_frame = tk.Frame(tab, height=300)
        inner_frame.pack()
        # add the tab to the tabs list and select it
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
