from typing import List

from src.service.timetable_service import ProgrammedClass

MOCK_PLANNED_COURSES = [
    (1, '16:00 - 18:00', 'Miercuri', 'Educatie fizica', 'Captarencu Oana', 'A2', 1, 0, 0, 'B3', 2),
    (2, '16:00 - 18:00', 'Miercuri', 'Retele de calculatoare', 'Diac Paul', 'A1', 1, 0, 0, 'C112', 2),
    (3, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'A1', 1, 0, 0, 'B3', 1),
    (4, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'A2', 1, 0, 0, 'B3', 1),
    (5, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'A3', 1, 0, 0, 'B3', 1),
    (6, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'A4', 1, 0, 0, 'B3', 1),
    (7, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'A5', 1, 0, 0, 'B3', 1),
    (8, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'B1', 1, 0, 0, 'B3', 1),
    (9, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'B2', 1, 0, 0, 'B3', 1),
    (10, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'B3', 1, 0, 0, 'B3', 1),
    (11, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'B4', 1, 0, 0, 'B3', 1),
    (12, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'E1', 1, 0, 0, 'B3', 1),
    (13, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'E2', 1, 0, 0, 'B3', 1),
    (14, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'E3', 1, 0, 0, 'B3', 1),
    (15, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'X1', 1, 0, 0, 'B3', 1),
    (16, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'X2', 1, 0, 0, 'B3', 1),
    (17, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'X3', 1, 0, 0, 'B3', 1),
    (18, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'X4', 1, 0, 0, 'B3', 1),
    (19, '08:00 - 10:00', 'Luni', 'Logica pentru informatica', 'Achirei Emanuel', 'X5', 1, 0, 0, 'B3', 1),
    (20, '08:00 - 10:00', 'Luni', 'Calculabilitate decidabilitate si complexitate', 'Crisan Gloria-Cerasela', 'MOC1', 1,
     0, 0, 'C112', 4),
    (21, '08:00 - 10:00', 'Luni', 'Calculabilitate decidabilitate si complexitate', 'Crisan Gloria-Cerasela', 'MSI1', 1,
     0, 0, 'C112', 4),
    (22, '08:00 - 10:00', 'Luni', 'Calculabilitate decidabilitate si complexitate', 'Crisan Gloria-Cerasela', 'MLC1', 1,
     0, 0, 'C112', 4),
    (
        23, '08:00 - 10:00', 'Luni', 'Calculabilitate decidabilitate si complexitate', 'Crisan Gloria-Cerasela',
        'MSAI1', 1,
        0, 0, 'C112', 4),
    (24, '08:00 - 10:00', 'Luni', 'Calculabilitate decidabilitate si complexitate', 'Crisan Gloria-Cerasela', 'MSD1', 1,
     0, 0, 'C112', 4),
    (25, '08:00 - 10:00', 'Luni', 'Calculabilitate decidabilitate si complexitate', 'Crisan Gloria-Cerasela', 'MSI1', 1,
     0, 0, 'C112', 4),
    (26, '08:00 - 10:00', 'Luni', 'Managementul proiectelor', 'Croitoru Eugen', 'MOC2', 1, 0, 0, 'C114', 5),
    (27, '08:00 - 10:00', 'Luni', 'Managementul proiectelor', 'Croitoru Eugen', 'MSI2', 1, 0, 0, 'C114', 5),
    (28, '08:00 - 10:00', 'Luni', 'Managementul proiectelor', 'Croitoru Eugen', 'MLC2', 1, 0, 0, 'C114', 5),
    (29, '08:00 - 10:00', 'Luni', 'Managementul proiectelor', 'Croitoru Eugen', 'MSAI2', 1, 0, 0, 'C114', 5),
    (30, '08:00 - 10:00', 'Luni', 'Managementul proiectelor', 'Croitoru Eugen', 'MSD2', 1, 0, 0, 'C114', 5),
    (31, '08:00 - 10:00', 'Luni', 'Managementul proiectelor', 'Croitoru Eugen', 'MSI2', 1, 0, 0, 'C114', 5)
]

TIMETABLE_MOCK: List[ProgrammedClass] = [
    ProgrammedClass(day="Monday", to="10:00", from_="8:00", group_class="A1", year=1,
                    class_name="Introduction to Programming", class_type="Lecture", professors=["Smith", "Jones"],
                    room="A101"),
    ProgrammedClass(day="Monday", to="12:00", from_="10:00", group_class="B1", year=1,
                    class_name="Introduction to Programming", class_type="Lecture", professors=["Smith", "Jones"],
                    room="A101"),
    ProgrammedClass(day="Monday", to="14:00", from_="12:00", group_class="A2", year=1,
                    class_name="Discrete Mathematics", class_type="Lecture", professors=["Brown"], room="B201"),
    ProgrammedClass(day="Monday", to="16:00", from_="14:00", group_class="B1", year=1,
                    class_name="Discrete Mathematics", class_type="Lecture", professors=["Brown"], room="B201"),
    ProgrammedClass(day="Tuesday", to="10:00", from_="8:00", group_class="A1", year=1,
                    class_name="Introduction to Programming", class_type="Lab", professors=["Green"], room="C301"),
    ProgrammedClass(day="Tuesday", to="12:00", from_="10:00", group_class="B1", year=2,
                    class_name="Introduction to Programming", class_type="Lab", professors=["Green"], room="C301"),
    ProgrammedClass(day="Tuesday", to="14:00", from_="12:00", group_class="A2", year=2,
                    class_name="Data Structures and Algorithms", class_type="Lecture", professors=["Lee"], room="A102"),
    ProgrammedClass(day="Tuesday", to="16:00", from_="14:00", group_class="B2", year=2,
                    class_name="Data Structures and Algorithms", class_type="Lecture", professors=["Lee"], room="A102"),
    ProgrammedClass(day="Wednesday", to="10:00", from_="8:00", group_class="A1", year=2,
                    class_name="Data Structures and Algorithms", class_type="Lab", professors=["Wang"], room="C302"),
    ProgrammedClass(day="Wednesday", to="12:00", from_="10:00", group_class='B2', year=2,
                    class_name='Data Structures and Algorithms', class_type='Lab', professors=['Wang'], room='C302'),
    ProgrammedClass(day='Wednesday', to='14:00', from_='12:00', group_class='A2', year=3,
                    class_name='Operating Systems', class_type='Lecture', professors=['Chen'], room='B202'),
    ProgrammedClass(day='Wednesday', to='16:00', from_='14:00', group_class='B2', year=3,
                    class_name='Operating Systems', class_type='Lecture', professors=['Chen'], room='B202'),
    ProgrammedClass(day='Thursday', to='10:00', from_='8:00', group_class='A2', year=2, class_name='Operating Systems',
                    class_type='Lab', professors=['Kim'], room='C303'),
    ProgrammedClass(day='Thursday', to='12:00', from_='10:00', group_class='B2', year=2, class_name='Operating Systems',
                    class_type='Lab', professors=['Kim'], room='C303'),
    ProgrammedClass(day='Thursday', to='14:00', from_='12:00', group_class='A2', year=2, class_name='Database Systems',
                    class_type='Lecture', professors=['Singh'], room='A103'),
    ProgrammedClass(day='Friday', to='14:00', from_='12:00', group_class='A2', year=2, class_name='Database Systems',
                    class_type='Lecture', professors=['Singh'], room='A103'),
    ProgrammedClass(day='Friday', to='14:00', from_='12:00', group_class='A4', year=2, class_name='Database Systems',
                    class_type='Lecture', professors=['Singh'], room='A103'),
]

TIMETABLE_MOCK_SMALL: List[ProgrammedClass] = [
    ProgrammedClass(day="Monday", to="10:00", from_="8:00", group_class="A1", year=1,
                    class_name="Introduction to Programming", class_type="Lecture", professors=['Smith'],
                    room="A101"),
    ProgrammedClass(day='Friday', to='14:00', from_='12:00', group_class='A4', year=2, class_name='Database Systems',
                    class_type='Lecture', professors=['Singh'], room='A103'),
]

MOCK_STUDENT_GROUPS = [
    (1, 1, 'A1'),
    (2, 2, 'A1'),
    (3, 3, 'A1'),
]

MAIN_PAGE_MOCK = '<h1>Orar</h1><p></p><h3>Facultatea de Informatica</h3><ul><li><a ' \
                 'href="students.html">Studenti</a></li><li><a href="professors.html">Profesori</a></li><li><a ' \
                 'href="rooms.html">Sali</a></li><li><a ' \
                 'href="classes.html">Discipline</a></li></ul><p></p><div>Generated with <b>SmartTimetable</b></div>'
