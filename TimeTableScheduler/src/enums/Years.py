class Years:
    BACHELOR_YEAR_1 = "Anul 1"
    BACHELOR_YEAR_2 = "Anul 2"
    BACHELOR_YEAR_3 = "Anul 3"
    MASTER_YEAR_1 = "Master Anul 1"
    MASTER_YEAR_2 = "Master Anul 2"

    @staticmethod
    def get_default_value():
        return Years.BACHELOR_YEAR_1

    @staticmethod
    def get_all_values() -> list:
        return [Years.BACHELOR_YEAR_1, Years.BACHELOR_YEAR_2, Years.BACHELOR_YEAR_3,
                Years.MASTER_YEAR_1, Years.MASTER_YEAR_2]

    @staticmethod
    def is_bachelor_first_year(year: str):
        return year == Years.BACHELOR_YEAR_1

    @staticmethod
    def is_bachelor_second_year(year: str):
        return year == Years.BACHELOR_YEAR_2

    @staticmethod
    def is_bachelor_third_year(year: str):
        return year == Years.BACHELOR_YEAR_3

    @staticmethod
    def is_master_first_year(year: str):
        return year == Years.MASTER_YEAR_1

    @staticmethod
    def is_master_second_year(year: str):
        return year == Years.MASTER_YEAR_2

    @staticmethod
    def is_any_year(year: str):
        return Years.is_bachelor_first_year(year) or Years.is_bachelor_second_year(year) or Years.is_bachelor_third_year(year) \
            or Years.is_master_first_year(year) or Years.is_master_second_year(year)

    @staticmethod
    def get_year_index(year: str):
        if Years.is_bachelor_first_year(year):
            return 1

        if Years.is_bachelor_second_year(year):
            return 2

        if Years.is_bachelor_third_year(year):
            return 3

        if Years.is_master_first_year(year):
            return 4

        if Years.is_master_second_year(year):
            return 5

        return 0
