import unittest

import test_database_connection
import test_enums_methods
import test_filter_service
import test_graphic_interface
import test_html_service
import test_timetable_service
import test_utils


class SequentialByClassTestRunner(unittest.TextTestRunner):
    def run(self, test):
        # Sort the test cases by class name
        tests_by_class = {}
        for test_case in test:
            test_class = type(test_case).__name__
            tests_by_class.setdefault(test_class, []).append(test_case)
        sorted_tests = []
        for class_name in sorted(tests_by_class.keys()):
            sorted_tests.extend(tests_by_class[class_name])

        # Run the tests sequentially by class
        result = super().run(unittest.TestSuite(sorted_tests))
        return result


modules = [test_filter_service, test_utils, test_database_connection, test_enums_methods, test_graphic_interface,
           test_html_service, test_timetable_service]

loader = unittest.TestLoader()
suite = unittest.TestSuite()

for module in modules:
    suite.addTests(loader.loadTestsFromModule(module))

runner = SequentialByClassTestRunner()
runner.run(suite)
