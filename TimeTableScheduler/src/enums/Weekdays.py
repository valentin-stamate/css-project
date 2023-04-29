class Weekdays:
    MONDAY = "Luni"
    TUESDAY = "Marti"
    WEDNESDAY = "Miercuri"
    THURSDAY = "Joi"
    FRIDAY = "Vineri"
    SATURDAY = "Sambata"

    @staticmethod
    def get_default_value():
        return Weekdays.MONDAY

    @staticmethod
    def get_all_values():
        return [Weekdays.MONDAY, Weekdays.TUESDAY, Weekdays.WEDNESDAY, Weekdays.THURSDAY, Weekdays.FRIDAY, Weekdays.SATURDAY]
