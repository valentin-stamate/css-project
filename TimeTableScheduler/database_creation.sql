CREATE TABLE Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    title TEXT NOT NULL
);

CREATE TABLE Disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    for_year_1 BOOLEAN NOT NULL,
    for_year_2 BOOLEAN NOT NULL,
    for_year_3 BOOLEAN NOT NULL,
    for_year_4 BOOLEAN NOT NULL,
    for_year_5 BOOLEAN NOT NULL,
    semester INTEGER NOT NULL,
    has_course BOOLEAN NOT NULL,
    has_laboratory BOOLEAN NOT NULL,
    has_seminary BOOLEAN NOT NULL
);

CREATE TABLE Rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    can_host_course BOOLEAN NOT NULL,
    can_host_laboratory BOOLEAN NOT NULL,
    can_host_seminary BOOLEAN NOT NULL
);

CREATE TABLE StudentGroups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    group_name TEXT NOT NULL
);

CREATE TABLE TimeSlots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    weekday TEXT NOT NULL,
    discipline_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    student_group_id INTEGER NOT NULL,
    FOREIGN KEY (discipline_id) REFERENCES Disciplines(id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id),
    FOREIGN KEY (student_group_id) REFERENCES StudentGroups(id)
);
