class TimePeriods:
    PERIOD_1 = "08:00 - 10:00"
    PERIOD_2 = "10:00 - 12:00"
    PERIOD_3 = "12:00 - 14:00"
    PERIOD_4 = "14:00 - 16:00"
    PERIOD_5 = "16:00 - 18:00"
    PERIOD_6 = "18:00 - 20:00"

    @staticmethod
    def get_default_value():
        return TimePeriods.PERIOD_1

    @staticmethod
    def get_all_values() -> list:
        return [TimePeriods.PERIOD_1, TimePeriods.PERIOD_2, TimePeriods.PERIOD_3, TimePeriods.PERIOD_4,
                TimePeriods.PERIOD_5, TimePeriods.PERIOD_6]
