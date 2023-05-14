import unittest

from src.enums.ClassTypes import ClassTypes
from src.enums.Semesters import Semesters
from src.enums.TimePeriods import TimePeriods
from src.enums.Weekdays import Weekdays
from src.enums.Years import Years


class EnumsTest(unittest.TestCase):
    def test_get_class_default_value(self):
        expected_value = 'Curs'
        result = ClassTypes.get_default_value()
        self.assertEqual(result, expected_value)

    def test_get_class_all_values(self):
        expected_value = ['Curs', 'Laborator', 'Seminar']
        result = ClassTypes.get_all_values()
        self.assertEqual(result, expected_value)

    def test_is_course(self):
        expected_value = True
        result = ClassTypes.is_course('Curs')
        self.assertEqual(result, expected_value)

    def test_is_laboratory(self):
        expected_value = True
        result = ClassTypes.is_laboratory('Laborator')
        self.assertEqual(result, expected_value)

    def test_is_seminary(self):
        expected_value = True
        result = ClassTypes.is_seminary('Seminar')
        self.assertEqual(result, expected_value)

    def test_get_semester_default_value(self):
        expected_value = 'Semestrul 1'
        result = Semesters.get_default_value()
        self.assertEqual(result, expected_value)

    def test_get_semester_all_values(self):
        expected_value = ['Semestrul 1', 'Semestrul 2']
        result = Semesters.get_all_values()
        self.assertEqual(result, expected_value)

    def test_is_first_semester(self):
        expected_value = True
        result = Semesters.is_first_semester('Semestrul 1')
        self.assertEqual(result, expected_value)

    def test_is_first_second(self):
        expected_value = True
        result = Semesters.is_second_semester('Semestrul 2')
        self.assertEqual(result, expected_value)

    def test_get_time_period_default_value(self):
        expected_value = "08:00 - 10:00"
        result = TimePeriods.get_default_value()
        self.assertEqual(result, expected_value)

    def test_get_time_period_all_values(self):
        expected_value = ["08:00 - 10:00", "10:00 - 12:00", "12:00 - 14:00",
                          "14:00 - 16:00", "16:00 - 18:00", "18:00 - 20:00"]
        result = TimePeriods.get_all_values()
        self.assertEqual(result, expected_value)

    def test_get_weekdays_default_value(self):
        expected_value = "Luni"
        result = Weekdays.get_default_value()
        self.assertEqual(result, expected_value)

    def test_get_weekdays_all_values(self):
        expected_value = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata"]
        result = Weekdays.get_all_values()
        self.assertEqual(result, expected_value)

    def test_get_years_default_value(self):
        expected_value = "Anul 1"
        result = Years.get_default_value()
        self.assertEqual(result, expected_value)

    def test_get_years_index(self):
        expected_value = 1
        result = Years.get_year_index('Anul 1')
        self.assertEqual(result, expected_value)
        expected_value = 2
        result = Years.get_year_index('Anul 2')
        self.assertEqual(result, expected_value)
        expected_value = 3
        result = Years.get_year_index('Anul 3')
        self.assertEqual(result, expected_value)
        expected_value = 4
        result = Years.get_year_index('Master Anul 1')
        self.assertEqual(result, expected_value)
        expected_value = 5
        result = Years.get_year_index('Master Anul 2')
        self.assertEqual(result, expected_value)
        expected_value = 0
        result = Years.get_year_index('Invalid')
        self.assertEqual(result, expected_value)
