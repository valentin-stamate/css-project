class Configuration:
    WIDTH = 1200
    HEIGHT = 600
    TABS = 5
    HEADINGS = {
        "StudentGroups": ["ID", "An", "Nume"],
        "Teachers": ["ID", "Nume", "Titlu"],
        "Disciplines": ["ID", "Nume", "An", "Semesteru", "Curs", "Laborator", "Seminar"],
        "Rooms": ["ID", "Nume", "Pentru Curs", "Pentru Laborator", "Pentru Seminar"],
        "TimeSlots": ["ID", "Ora", "Zi", "Disciplina", "Profesor", "Grupa"],
    }
    COLUMN_WIDTHS = {
        "StudentGroups": {"ID": 50, "An": 100, "Nume": 100},
        "Teachers": {"ID": 50, "Nume": 350, "Titlu": 150},
        "Disciplines": {"ID": 50, "Nume": 500, "An": 100, "Semesteru": 100, "Curs": 100, "Laborator": 100,
                        "Seminar": 100},
        "Rooms": {"ID": 50, "Nume": 100, "Pentru Curs": 100, "Pentru Laborator": 100, "Pentru Seminar": 100},
        "TimeSlots": {"ID": 50, "Ora": 100, "Zi": 100, "Disciplina": 450, "Profesor": 350, "Grupa": 100},
    }
    CONVERSION_BOOLEAN_FOR_DB = {
        1: "Da",
        0: "Nu"
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
