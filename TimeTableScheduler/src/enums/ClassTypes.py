class ClassTypes:
    COURSE = 'Curs'
    LABORATORY = 'Laborator'
    SEMINARY = 'Seminar'

    @staticmethod
    def get_default_value():
        return ClassTypes.COURSE

    @staticmethod
    def get_all_values() -> list:
        return [ClassTypes.COURSE, ClassTypes.LABORATORY, ClassTypes.SEMINARY]

    @staticmethod
    def is_course(class_type: str):
        return class_type == ClassTypes.COURSE

    @staticmethod
    def is_laboratory(class_type: str):
        return class_type == ClassTypes.LABORATORY

    @staticmethod
    def is_seminary(class_type: str):
        return class_type == ClassTypes.SEMINARY
