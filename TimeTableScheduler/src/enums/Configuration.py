class Configuration:
    WIDTH = 1200
    HEIGHT = 600
    TABS = 5
    HEADINGS = {
        "Student Groups": ["ID", "Year", "Name"],
        "Teachers": ["ID", "Name", "Title"],
        "Disciplines": ["ID", "Name", "Year", "Semester", "Has Course", "Has Laboratory", "Has Seminary"],
        "Rooms": ["ID", "Name", "Can Host Course", "Can Host Laboratory", "Can Host Seminary"],
        "Schedules": ["ID", "Time", "Weekday", "Discipline", "Teacher", "Students"],
    }
    COLUMN_WIDTHS = {
        "Student Groups": {"ID": 50, "Year": 100, "Name": 100},
        "Teachers": {"ID": 50, "Name": 350, "Title": 150},
        "Disciplines": {"ID": 50, "Name": 500, "Year": 100, "Semester": 100, "Has Course": 100, "Has Laboratory": 100,
                        "Has Seminary": 100},
        "Rooms": {"ID": 50, "Name": 100, "Can Host Course": 100, "Can Host Laboratory": 100, "Can Host Seminary": 100},
        "Schedules": {"ID": 50, "Time": 100, "Weekday": 100, "Discipline": 450, "Teacher": 350, "Students": 100},
    }
    CONVERSION_BOOLEAN_FOR_DB = {
        1: "Yes",
        0: "No"
    }
    CONVERSION_YEARS_FOR_UI = {
        "Anul 1": 1,
        "Anul 2": 2,
        "Anul 3": 3,
        "Master Anul 1": 4,
        "Master Anul 2": 5
    }
    CONVERSION_YEARS_FOR_DB = {
        1: "Anul 1",
        2: "Anul 2",
        3: "Anul 3",
        4: "Master Anul 1",
        5: "Master Anul 2",
    }
