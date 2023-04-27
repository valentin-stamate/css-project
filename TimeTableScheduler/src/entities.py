class Teachers:
    def __init__(self, name, title, id='0'):
        self.id = id
        self.name = name
        self.title = title


class Disciplines:
    def __init__(self, id, name, year, semester, has_course=True, has_laboratory=False, has_seminary=False):
        self.id = id
        self.name = name
        self.year = year
        self.semester = semester
        self.has_course = has_course
        self.has_laboratory = has_laboratory
        self.has_seminary = has_seminary


class Rooms:
    def __init__(self, id, name, can_host_course, can_host_laboratory, can_host_seminary):
        self.id = id
        self.name = name
        self.can_host_course = can_host_course
        self.can_host_laboratory = can_host_laboratory
        self.can_host_seminary = can_host_seminary


class TimeSlots:
    def __init__(self, id, time, weekday, discipline, teacher, students):
        self.id = id
        self.time = time
        self.weekday = weekday
        self.discipline = discipline
        self.teacher = teacher
        self.students = students


class Students:
    def __init__(self, id, year, student_group, timeslots: TimeSlots):
        self.id = id
        self.year = year
        self.student_group = student_group
        self.timeslots = timeslots
