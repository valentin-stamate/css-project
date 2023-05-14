import datetime
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
    ProgrammedClass(day="Wednesday", to="10:00", from_="8:00", group_class="A1", year=2,
                    class_name="Data Structures and Algorithms", class_type="Lab",
                    professors=["Wang"], room="C302"),
    ProgrammedClass(day='Friday', to='14:00', from_='12:00', group_class='A4', year=2, class_name='Database Systems',
                    class_type='Lecture', professors=['Singh'], room='A103'),
]

MOCK_STUDENT_GROUPS = [
    (1, 1, 'A1'),
    (2, 2, 'A1'),
    (3, 3, 'A1'),
]
MOCK_STUDENT_GROUPS_FORMATTED = [
    [1, 'Anul 1', 'A1'],
    [2, 'Anul 2', 'A1'],
    [3, 'Anul 3', 'A1'],
]
MAIN_PAGE_MOCK = '<h1>Orar</h1><p></p><h3>Facultatea de Informatica</h3><ul><li><a ' \
                 'href="students.html">Studenti</a></li><li><a href="professors.html">Profesori</a></li><li><a ' \
                 'href="rooms.html">Sali</a></li><li><a ' \
                 'href="classes.html">Discipline</a></li></ul><p></p><div>Generated with <b>SmartTimetable</b></div>'

MOCK_STUDENT_PAGE_1 = f'<h1>Orar Informatica, anul 1</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Grupa</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Sala</th></tr><tr><td colspan="7">Monday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">1A1</td><td colspan="1">Introduction to Programming</td><td colspan="1">Lecture</td><td colspan="1">Smith</td><td colspan="1">A101</td></tr></table>'
MOCK_STUDENT_PAGE_2 = f'<h1>Orar 1A</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Grupa</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Sala</th></tr><tr><td colspan="7">Monday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">1A1</td><td colspan="1">Introduction to Programming</td><td colspan="1">Lecture</td><td colspan="1">Smith</td><td colspan="1">A101</td></tr></table>'
MOCK_STUDENT_PAGE_3 = f'<h1>Orar Informatica, anul 2</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Grupa</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Sala</th></tr><tr><td colspan="7">Wednesday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">2A1</td><td colspan="1">Data Structures and Algorithms</td><td colspan="1">Lab</td><td colspan="1">Wang</td><td colspan="1">C302</td></tr><tr><td colspan="7">Friday</td></tr><tr><td colspan="1">12:00</td><td colspan="1">14:00</td><td colspan="1">2A4</td><td colspan="1">Database Systems</td><td colspan="1">Lecture</td><td colspan="1">Singh</td><td colspan="1">A103</td></tr></table>'
MOCK_STUDENT_PAGE_4 = f'<h1>Orar 2A</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Grupa</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Sala</th></tr><tr><td colspan="7">Wednesday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">2A1</td><td colspan="1">Data Structures and Algorithms</td><td colspan="1">Lab</td><td colspan="1">Wang</td><td colspan="1">C302</td></tr><tr><td colspan="7">Friday</td></tr><tr><td colspan="1">12:00</td><td colspan="1">14:00</td><td colspan="1">2A4</td><td colspan="1">Database Systems</td><td colspan="1">Lecture</td><td colspan="1">Singh</td><td colspan="1">A103</td></tr></table>'
MOCK_STUDENT_PAGE_5 = f'<h1>Orar 2A1</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Sala</th></tr><tr><td colspan="6">Wednesday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Data Structures and Algorithms</td><td colspan="1">Lab</td><td colspan="1">Wang</td><td colspan="1">C302</td></tr></table>'
MOCK_STUDENT_PAGE_6 = f'<h1>Orar 2A4</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Sala</th></tr><tr><td colspan="6">Friday</td></tr><tr><td colspan="1">12:00</td><td colspan="1">14:00</td><td colspan="1">Database Systems</td><td colspan="1">Lecture</td><td colspan="1">Singh</td><td colspan="1">A103</td></tr></table>'
MOCK_STUDENT_PAGE = f'<h1>Orar Studenti</h1><ul><li><a href="pages/classes_1.html">Anul 1</a><ul><li><a href="pages/classes_group_type_1A.html">Semianul 1A</a></ul></li><li><a href="pages/classes_2.html">Anul 2</a><ul><li><a href="pages/classes_group_type_2A.html">Semianul 2A</a><ul><li><a href="pages/classes_2A1.html">2A1</a></li><li><a href="pages/classes_2A4.html">2A4</a></li></ul></li></ul></li></ul>'

MOCK_PROFESSORS_PAGE_1 = f'<h1>Orar Singh</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Studenti</th><th colspan="1">Sala</th></tr><tr><td colspan="6">Friday</td></tr><tr><td colspan="1">12:00</td><td colspan="1">14:00</td><td colspan="1">Database Systems</td><td colspan="1">Lecture</td><td colspan="1">2A4</td><td colspan="1">A103</td></tr></table>'
MOCK_PROFESSORS_PAGE_2 = f'<h1>Orar Smith</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Studenti</th><th colspan="1">Sala</th></tr><tr><td colspan="6">Monday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Introduction to Programming</td><td colspan="1">Lecture</td><td colspan="1">1A1</td><td colspan="1">A101</td></tr></table>'
MOCK_PROFESSORS_PAGE_3 = f'<h1>Orar Wang</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Studenti</th><th colspan="1">Sala</th></tr><tr><td colspan="6">Wednesday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Data Structures and Algorithms</td><td colspan="1">Lab</td><td colspan="1">2A1</td><td colspan="1">C302</td></tr></table>'
MOCK_PROFESSORS_PAGE = f'<h1>Orar Profesori</h1><ul><li><a href="pages/p_Singh.html">Singh</a></li><li><a href="pages/p_Smith.html">Smith</a></li><li><a href="pages/p_Wang.html">Wang</a></li></ul>'

MOCK_ROOMS_PAGE_1 = f'<h1>Orar Sala A101</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Studenti</th></tr><tr><td colspan="6">Monday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Introduction to Programming</td><td colspan="1">Lecture</td><td colspan="1">Smith</td><td colspan="1">1A1</td></tr></table>'
MOCK_ROOMS_PAGE_2 = f'<h1>Orar Sala A103</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Studenti</th></tr><tr><td colspan="6">Friday</td></tr><tr><td colspan="1">12:00</td><td colspan="1">14:00</td><td colspan="1">Database Systems</td><td colspan="1">Lecture</td><td colspan="1">Singh</td><td colspan="1">2A4</td></tr></table>'
MOCK_ROOMS_PAGE_3 = f'<h1>Orar Sala C302</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Studenti</th></tr><tr><td colspan="6">Wednesday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Data Structures and Algorithms</td><td colspan="1">Lab</td><td colspan="1">Wang</td><td colspan="1">2A1</td></tr></table>'
MOCK_ROOMS_PAGE = f'<h1>Orar Sali</h1><ul><li><a href="pages/r_A101.html">A101</a></li><li><a href="pages/r_A103.html">A103</a></li><li><a href="pages/r_C302.html">C302</a></li></ul>'

MOCK_CLASSES_PAGE_1 = f'<h1>Orar Disciplina Data Structures and Algorithms</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Studenti</th></tr><tr><td colspan="6">Wednesday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Data Structures and Algorithms</td><td colspan="1">Lab</td><td colspan="1">Wang</td><td colspan="1">2A1</td></tr></table>'
MOCK_CLASSES_PAGE_2 = f'<h1>Orar Disciplina Database Systems</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Studenti</th></tr><tr><td colspan="6">Friday</td></tr><tr><td colspan="1">12:00</td><td colspan="1">14:00</td><td colspan="1">Database Systems</td><td colspan="1">Lecture</td><td colspan="1">Singh</td><td colspan="1">2A4</td></tr></table>'
MOCK_CLASSES_PAGE_3 = f'<h1>Orar Disciplina Introduction to Programming</h1><div><strong>Generated: {datetime.date.today().isoformat()}</strong></div><hr><table><tr><th colspan="1">De la</th><th colspan="1">Pana la</th><th colspan="1">Disciplina</th><th colspan="1">Tip</th><th colspan="1">Profesor</th><th colspan="1">Studenti</th></tr><tr><td colspan="6">Monday</td></tr><tr><td colspan="1">8:00</td><td colspan="1">10:00</td><td colspan="1">Introduction to Programming</td><td colspan="1">Lecture</td><td colspan="1">Smith</td><td colspan="1">1A1</td></tr></table>'
MOCK_CLASSES_PAGE = f'<h1>Orar Discipline</h1><ul><li><a href="pages/d_Data Structures and Algorithms.html">Data Structures and Algorithms</a></li><li><a href="pages/d_Database Systems.html">Database Systems</a></li><li><a href="pages/d_Introduction to Programming.html">Introduction to Programming</a></li></ul>'

MOCK_ROOMS = [
    (1, 'Room1', 1, 1, 0),
    (2, 'Room2', 1, 1, 0),
]
MOCK_ROOMS_FORMATTED = [
    [1, 'Room1', 'Da', 'Da', 'Nu'],
    [2, 'Room2', 'Da', 'Da', 'Nu'],
]

MOCK_DISCIPLINES = [
    (1, 'Discipline1', 1, 0, 0, 0, 0, 1, 0, 1, 0)
]
MOCK_DISCIPLINES_FORMATTED = [
    (1, 'Discipline1', 'Anul 1', 1, 'Nu', 'Da', 'Nu')
]
