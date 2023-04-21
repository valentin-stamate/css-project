-- Example INSERT statements for Teachers
INSERT INTO teachers (name, title)
VALUES ('John Doe', 'Professor');
INSERT INTO teachers (name, title)
VALUES ('Jane Smith', 'Associate Professor');
INSERT INTO teachers (name, title)
VALUES ('Bob Johnson', 'Assistant Professor');

-- Example INSERT statements for Disciplines
INSERT INTO disciplines (name, year, semester, has_course, has_laboratory, has_seminary)
VALUES ('Computer Science', 2023, 'Spring', 1, 1, 0);
INSERT INTO disciplines (name, year, semester, has_course, has_laboratory, has_seminary)
VALUES ('Mathematics', 2023, 'Fall', 1, 0, 1);
INSERT INTO disciplines (name, year, semester, has_course, has_laboratory, has_seminary)
VALUES ('English Literature', 2024, 'Spring', 1, 0, 0);

-- Example INSERT statements for Rooms
INSERT INTO rooms (name, can_host_course, can_host_laboratory, can_host_seminary)
VALUES ('Room 101', 1, 0, 0);
INSERT INTO rooms (name, can_host_course, can_host_laboratory, can_host_seminary)
VALUES ('Lab 201', 0, 1, 0);
INSERT INTO rooms (name, can_host_course, can_host_laboratory, can_host_seminary)
VALUES ('Seminar Room A', 0, 0, 1);

-- Example INSERT statements for TimeSlots
INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, students)
VALUES ('10:00-12:00', 'Monday', 1, 1, 'John Doe');
INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, students)
VALUES ('14:00-16:00', 'Wednesday', 2, 2, 'Jane Smith');
INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, students)
VALUES ('09:00-11:00', 'Friday', 3, 3, 'Bob Johnson');

-- Example INSERT statements for Students
INSERT INTO students (year, student_group, timeslots)
VALUES (2023, 'CS101', 1);
INSERT INTO students (year, student_group, timeslots)
VALUES (2023, 'MATH201', 2);
INSERT INTO students (year, student_group, timeslots)
VALUES (2024, 'LIT101', 3);
