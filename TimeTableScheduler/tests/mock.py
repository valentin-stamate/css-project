from typing import List

from src.service.timetable_service import ProgrammedClass

MOCK_STUDENT_TIMETABLE = '<table><tr><th colspan="1">Head 1</th><th colspan="1">Head 2</th><th colspan="1">Head 3</th><th colspan="1">Head 4</th><th colspan="1">Head 5</th></tr><tr><td colspan="5">Day 1</td></tr><tr><td colspan="1">12</td><td colspan="1">14</td><td colspan="1">Name</td><td colspan="1">Author</td><td colspan="1">C102</td></tr><tr><td colspan="5">Day 2</td></tr><tr><td colspan="1">12</td><td colspan="1">14</td><td colspan="1">Name</td><td colspan="1">Author</td><td colspan="1">C102</td></tr></table>'

TIMETABLE_MOCK: List[ProgrammedClass] = [
    ProgrammedClass(day="Monday", to="10:00", from_="8:00", group=1, group_class="A1", year=1, class_name="Introduction to Programming", class_type="Lecture", professors=["Smith", "Jones"], room="A101", frequency="Weekly"),
    ProgrammedClass(day="Monday", to="12:00", from_="10:00", group=2, group_class="B1", year=1, class_name="Introduction to Programming", class_type="Lecture", professors=["Smith", "Jones"], room="A101", frequency="Weekly"),
    ProgrammedClass(day="Monday", to="14:00", from_="12:00", group=1, group_class="A2", year=1, class_name="Discrete Mathematics", class_type="Lecture", professors=["Brown"], room="B201", frequency="Weekly"),
    ProgrammedClass(day="Monday", to="16:00", from_="14:00", group=2, group_class="B1", year=1, class_name="Discrete Mathematics", class_type="Lecture", professors=["Brown"], room="B201", frequency="Weekly"),
    ProgrammedClass(day="Tuesday", to="10:00", from_="8:00", group=1, group_class="A1", year=1, class_name="Introduction to Programming", class_type="Lab", professors=["Green"], room="C301", frequency="Biweekly"),
    ProgrammedClass(day="Tuesday", to="12:00", from_="10:00", group=2, group_class="B1", year=2, class_name="Introduction to Programming", class_type="Lab", professors=["Green"], room="C301", frequency="Biweekly"),
    ProgrammedClass(day="Tuesday", to="14:00", from_="12:00", group=3, group_class="A2", year=2, class_name="Data Structures and Algorithms", class_type="Lecture", professors=["Lee"], room="A102", frequency="Weekly"),
    ProgrammedClass(day="Tuesday", to="16:00", from_="14:00", group=4, group_class="B2", year=2, class_name="Data Structures and Algorithms", class_type="Lecture", professors=["Lee"], room="A102", frequency="Weekly"),
    ProgrammedClass(day="Wednesday", to="10:00", from_="8:00", group=3, group_class="A1", year=2, class_name="Data Structures and Algorithms", class_type="Lab", professors=["Wang"], room="C302", frequency="", package='A'),
    ProgrammedClass(day="Wednesday", to="12:00", from_="10:00", group=4, group_class='B2', year=2, class_name='Data Structures and Algorithms', class_type='Lab', professors=['Wang'], room='C302', frequency='', package='A'),
    ProgrammedClass(day='Wednesday', to='14:00', from_='12:00', group=3, group_class='A2', year=3, class_name='Operating Systems', class_type='Lecture', professors=['Chen'], room='B202', frequency='', package='B'),
    ProgrammedClass(day='Wednesday', to='16:00', from_='14:00', group=4, group_class='B2', year=3, class_name='Operating Systems', class_type='Lecture', professors=['Chen'], room='B202', frequency='', package='B'),
    ProgrammedClass(day='Thursday', to='10:00', from_='8:00', group=3, group_class='A2', year=2, class_name='Operating Systems', class_type='Lab', professors=['Kim'], room='C303', frequency='', package='B'),
    ProgrammedClass(day='Thursday', to='12:00', from_='10:00', group=4, group_class='B2', year=2, class_name='Operating Systems', class_type='Lab', professors=['Kim'], room='C303', frequency='', package='B'),
    ProgrammedClass(day='Thursday', to='14:00', from_='12:00', group=3, group_class='A2', year=2, class_name='Database Systems', class_type='Lecture', professors=['Singh'], room='A103', frequency='', package='A'),
    ProgrammedClass(day='Friday', to='14:00', from_='12:00', group=3, group_class='A2', year=2, class_name='Database Systems', class_type='Lecture', professors=['Singh'], room='A103', frequency='', package='A'),
    ProgrammedClass(day='Friday', to='14:00', from_='12:00', group=3, group_class='A4', year=2, class_name='Database Systems', class_type='Lecture', professors=['Singh'], room='A103', frequency='', package='A'),
]