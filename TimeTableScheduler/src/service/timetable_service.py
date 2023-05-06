import os
from typing import List

from src.service.html_service import HTMLPage, TimetablePage
from src.service.models import ProgrammedClass


class TimetableGenerator:
    group_headers = ['De la', 'Pana la', 'Disciplina', 'Tip', 'Profesor', 'Sala']
    year_group_headers = ['De la', 'Pana la', 'Grupa', 'Disciplina', 'Tip', 'Profesor', 'Sala']
    professor_headers = ['De la', 'Pana la', 'Disciplina', 'Tip', 'Studenti', 'Sala']
    room_headers = ['De la', 'Pana la', 'Disciplina', 'Tip', 'Profesor', 'Studenti']
    classes_headers = ['De la', 'Pana la', 'Disciplina', 'Tip', 'Studenti', 'Profesor', 'Sala']

    def __init__(self, programmed_classes: List[ProgrammedClass]):
        if not os.path.exists("html/pages"):
            os.makedirs("html/pages")
        self.programmed_classes = programmed_classes

    @staticmethod
    def categorize_by_year(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            key = p_class.get_year()  # 1
            if key not in categorized_classes:
                categorized_classes[key] = []

            categorized_classes[key].append(p_class)

        return categorized_classes

    @staticmethod
    def categorize_by_group_type(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            key = p_class.get_group_year()  # 1A

            if key not in categorized_classes:
                categorized_classes[key] = []

            categorized_classes[key].append(p_class)

        return categorized_classes

    @staticmethod
    def categorize_by_group(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            key = p_class.get_full_group_identifier()

            if key not in categorized_classes:
                categorized_classes[key] = []

            categorized_classes[key].append(p_class)

        return categorized_classes

    @staticmethod
    def categorize_by_day(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            key = p_class.day

            if key not in categorized_classes:
                categorized_classes[key] = []

            categorized_classes[key].append(p_class)

        return categorized_classes

    @staticmethod
    def categorize_by_professor(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            for professor in p_class.professors:
                if professor not in categorized_classes:
                    categorized_classes[professor] = []

                categorized_classes[professor].append(p_class)

        return categorized_classes

    @staticmethod
    def transform_for_timetable(data: List[ProgrammedClass], lambda_):
        """ Converts the categorized data of ProgrammedClass into a categorized data of list """

        categorized_by_days = TimetableGenerator.categorize_by_day(data)

        new_data = []

        # The key is actually the day
        for key in categorized_by_days.keys():
            elements = categorized_by_days[key]

            new_data.append([key])
            for el in elements:
                new_data.append(lambda_(el))

        return new_data

    @staticmethod
    def categorize_by_rooms(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            key = p_class.room

            if key not in categorized_classes:
                categorized_classes[key] = []

            categorized_classes[key].append(p_class)

        return categorized_classes

    @staticmethod
    def categorize_by_class(classes: List[ProgrammedClass]):
        categorized_classes = {}

        for p_class in classes:
            key = p_class.class_name

            if key not in categorized_classes:
                categorized_classes[key] = []

            categorized_classes[key].append(p_class)

        return categorized_classes

    def generate_all(self):
        self.generate_main_page()
        self.generate_classes_page()
        self.generate_student_page()
        self.generate_professors_page()
        self.generate_rooms_page()

    def generate_main_page(self):
        html_page = HTMLPage()

        html_page.add('<h1>Orar</h1>')
        html_page.add('<p></p><h3>Facultatea de Informatica</h3>')
        html_page.add('<ul>'
                      '<li><a href="students.html">Studenti</a></li>'
                      '<li><a href="professors.html">Profesori</a></li>'
                      '<li><a href="rooms.html">Sali</a></li>'
                      '<li><a href="classes.html">Discipline</a></li>'
                      '</ul>')
        html_page.add('<p></p><div>Generated with <b>SmartTimetable</b></div>')

        html = html_page.generate_html()
        file = open('./html/index.html', 'wt')
        file.write(html)
        file.close()

    def generate_student_page(self):
        html_page = HTMLPage()

        html_page.add('<h1>Orar Studenti</h1>')

        html_page.add('<ul>')

        # Generates the year timetable
        classes_categorized_by_year = self.categorize_by_year(self.programmed_classes)
        classes_list = list(classes_categorized_by_year.keys())
        classes_list.sort()
        for year_key in classes_list:
            classes = classes_categorized_by_year[year_key]
            year_key = int(year_key)
            html_name = f'classes_{year_key}.html'

            year_title = ('Master ' if year_key > 3 else '') + 'Anul ' + str(year_key if year_key <= 3 else year_key - 3)

            html_page.add(f'<li><a href="pages/{html_name}">{year_title}</a>')

            data = self.transform_for_timetable(classes, ProgrammedClass.get_list_for_group_type_timetable)
            html_table = TimetablePage(f'Orar Informatica, anul {year_key}', self.year_group_headers, data, f'./html/pages/{html_name}')
            html_table.generate_html()

            # Generates the group type timetable
            classes_categorized_by_group_type = self.categorize_by_group_type(classes)
            html_page.add('<ul>')
            for group_type_key in classes_categorized_by_group_type.keys():
                classes = classes_categorized_by_group_type[group_type_key]
                html_name = f'classes_group_type_{group_type_key}.html'
                html_page.add(f'<li><a href="pages/{html_name}">Grupa {group_type_key}</a>')

                data = self.transform_for_timetable(classes, ProgrammedClass.get_list_for_group_type_timetable)
                html_table = TimetablePage(f'Orar {group_type_key}', self.year_group_headers, data,
                                           f'./html/pages/{html_name}')
                html_table.generate_html()

                # Generates the group timetable
                classes_by_group = self.categorize_by_group(classes)

                if len(classes_by_group) == 1:
                    continue

                html_page.add('<ul>')
                for group_key in classes_by_group.keys():
                    classes = classes_by_group[group_key]
                    html_name = f'classes_{group_key}.html'

                    html_page.add(f'<li><a href="pages/{html_name}">{group_key}</a></li>')

                    data = self.transform_for_timetable(classes, ProgrammedClass.get_list_for_group_timetable)

                    html_table = TimetablePage(f'Orar {group_key}', self.group_headers, data,
                                               f'./html/pages/{html_name}')
                    html_table.generate_html()

                html_page.add('</ul></li>')

            html_page.add('</ul></li>')

        html_page.add('</ul>')

        html = html_page.generate_html()
        file = open('./html/students.html', 'wt')
        file.write(html)
        file.close()

    def generate_professors_page(self):
        html_page = HTMLPage()

        html_page.add('<h1>Orar Profesori</h1>')
        html_page.add('<ul>')

        categorized_classes = self.categorize_by_professor(self.programmed_classes)
        classes_list = list(categorized_classes.keys())
        classes_list.sort()
        for professor in classes_list:
            classes = categorized_classes[professor]
            html_name = f'p_{professor}.html'

            html_page.add(f'<li><a href="pages/{html_name}">{professor}</a></li>')

            data = self.transform_for_timetable(classes, ProgrammedClass.get_list_for_professor_timetable)
            html_table = TimetablePage(f'Orar {professor}', self.professor_headers, data, f'./html/pages/{html_name}')
            html_table.generate_html()

        html_page.add('</ul>')

        html = html_page.generate_html()
        file = open('./html/professors.html', 'wt')
        file.write(html)
        file.close()

    def generate_rooms_page(self):
        html_page = HTMLPage()

        html_page.add('<h1>Orar Sali</h1>')
        html_page.add('<ul>')

        categorized_classes = self.categorize_by_rooms(self.programmed_classes)
        classes_list = list(categorized_classes.keys())
        classes_list.sort()
        for room in classes_list:
            classes = categorized_classes[room]
            html_name = f'r_{room}.html'

            html_page.add(f'<li><a href="pages/{html_name}">{room}</a></li>')

            data = self.transform_for_timetable(classes, ProgrammedClass.get_list_for_room_timetable)
            html_table = TimetablePage(f'Orar Sala {room}', self.room_headers, data, f'./html/pages/{html_name}')
            html_table.generate_html()

        html_page.add('</ul>')

        html = html_page.generate_html()
        file = open('./html/rooms.html', 'wt')
        file.write(html)
        file.close()

    def generate_classes_page(self):
        html_page = HTMLPage()

        html_page.add('<h1>Orar Discipline</h1>')
        html_page.add('<ul>')

        categorized_classes = self.categorize_by_class(self.programmed_classes)
        classes_list = list(categorized_classes.keys())
        classes_list.sort()
        for class_name in classes_list:
            classes = categorized_classes[class_name]
            html_name = f'd_{class_name}.html'

            html_page.add(f'<li><a href="pages/{html_name}">{class_name}</a></li>')

            data = self.transform_for_timetable(classes, ProgrammedClass.get_list_for_class_timetable)
            html_table = TimetablePage(f'Orar Disciplina {class_name}', self.room_headers, data, f'./html/pages/{html_name}')
            html_table.generate_html()

        html_page.add('</ul>')

        html = html_page.generate_html()
        file = open('./html/classes.html', 'wt')
        file.write(html)
        file.close()
