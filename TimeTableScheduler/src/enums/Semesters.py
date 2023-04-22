class Semesters:
    FIRST_SEMESTER = "Semestrul 1"
    SECOND_SEMESTER = "Semestrul 2"

    @staticmethod
    def get_default_value():
        return Semesters.FIRST_SEMESTER

    @staticmethod
    def get_all_values() -> list:
        return [Semesters.FIRST_SEMESTER, Semesters.SECOND_SEMESTER]

    @staticmethod
    def is_first_semester(semester: str):
        return semester == Semesters.FIRST_SEMESTER

    @staticmethod
    def is_second_semester(semester: str):
        return semester == Semesters.SECOND_SEMESTER
