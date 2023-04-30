class Teachers:
    def __init__(self, name, title, id='0'):
        self.id = id
        self.name = name
        self.title = title


class Disciplines:
    def __init__(self, name, semester, for_year1=False, for_year2=False, for_year3=False, for_year4=False,
                 for_year5=False, has_course=True, has_laboratory=False, has_seminary=False, id='0'):
        self.id = id
        self.name = name
        self.for_year1 = for_year1
        self.for_year2 = for_year2
        self.for_year3 = for_year3
        self.for_year4 = for_year4
        self.for_year5 = for_year5
        self.semester = semester
        self.has_course = has_course
        self.has_laboratory = has_laboratory
        self.has_seminary = has_seminary


class Rooms:
    def __init__(self, name, can_host_course=False, can_host_laboratory=False, can_host_seminary=False, id='0'):
        self.id = id
        self.name = name
        self.can_host_course = can_host_course
        self.can_host_laboratory = can_host_laboratory
        self.can_host_seminary = can_host_seminary


class TimeSlots:
    def __init__(self, time, weekday, discipline, teacher, students, is_course, is_laboratory, is_seminary, room, id=0):
        self.id = id
        self.time = time
        self.weekday = weekday
        self.discipline = discipline
        self.teacher = teacher
        self.students = students
        self.is_course = is_course
        self.is_laboratory = is_laboratory
        self.is_seminary = is_seminary
        self.room = room


class StudentGroups:
    def __init__(self, year, group_name, timeslots=None, id='0'):
        if timeslots is None:
            timeslots = []
        self.id = id
        self.year = year
        self.group_name = group_name
        self.timeslots = timeslots
