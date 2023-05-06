import unittest

import tkinter as tk

from src.graphic_interface import SchedulerApp


class GraphicInterfaceTest(unittest.TestCase):

    def test_on_generate_html(self):
        root = tk.Tk()
        app = SchedulerApp(root)
        app.on_generate_html_timetables('')
