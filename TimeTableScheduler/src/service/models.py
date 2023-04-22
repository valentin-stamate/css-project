class ProgrammedClass:

    def __init__(self, day, to, from_, group, group_class, year, class_name, class_type, professors, rooms, frequency='', package=''):
        self.day = day
        self.to = to
        self.from_ = from_
        self.group = group # 1, 2, 3 etc
        self.group_class = group_class # B1, A2
        self.year = year
        self.class_name = class_name
        self.class_type = class_type
        self.professors = professors
        self.rooms = rooms
        self.frequency = frequency
        self.package = package

    def get_year(self):
        return f'{self.year}' # 1

    def get_class_identifier(self):
        return f'{self.group_class}' # A2

    def get_group_year(self):
        return f'{self.year}{self.group_class[0]}' # 1A

    def get_full_group_identifier(self):
        return f'{self.year}{self.group_class}' # 1A1

    @staticmethod
    def get_list_for_group_timetable(pc):
        return [pc.to, pc.from_, pc.class_name, pc.class_type, pc.professors, pc.rooms, pc.frequency, pc.package]

    @staticmethod
    def get_list_for_group_type_timetable(pc):
        full_group = f'{pc.year}{pc.group_class}'
        return [pc.to, pc.from_, full_group, pc.class_name, pc.class_type, pc.professors, pc.rooms, pc.frequency, pc.package]
