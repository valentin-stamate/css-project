class ProgrammedClass:

    def __init__(self, day, from_, to, group_class, year, class_name, class_type, professors, room):
        self.day = day
        self.from_ = from_
        self.to = to
        self.year = year

        self.group = group_class[len(group_class) - 1]  # 1, 2, 3 etc
        if year > 3:
            self.group = 1

        self.group_class = group_class  # B1, A2

        self.class_name = class_name
        self.class_type = class_type
        self.professors = professors
        self.room = room

    def get_year(self):
        return f'{self.year}'  # 1

    def get_class_identifier(self):
        return f'{self.group_class}'  # A2

    def get_group_year(self):
        return f'{self.year}{self.group_class[0]}'  # 1A

    def get_full_group_identifier(self):
        return f'{self.year}{self.group_class}'  # 1A1

    @staticmethod
    def get_list_for_group_timetable(pc):
        return [pc.from_, pc.to, pc.class_name, pc.class_type, pc.professors, pc.room]

    @staticmethod
    def get_list_for_group_type_timetable(pc):
        full_group = ProgrammedClass.get_full_group_identifier(pc)
        return [pc.from_, pc.to, full_group, pc.class_name, pc.class_type, pc.professors, pc.room]

    @staticmethod
    def get_list_for_professor_timetable(pc):
        full_group = ProgrammedClass.get_full_group_identifier(pc)
        return [pc.from_, pc.to, pc.class_name, pc.class_type, full_group, pc.room]

    @staticmethod
    def get_list_for_class_timetable(pc):
        full_group = ProgrammedClass.get_full_group_identifier(pc)
        return [pc.from_, pc.to, pc.class_name, pc.class_type, pc.professors, full_group]

    @staticmethod
    def get_list_for_room_timetable(pc):
        full_group = ProgrammedClass.get_full_group_identifier(pc)
        return [pc.from_, pc.to, pc.class_name, pc.class_type, pc.professors, full_group]
