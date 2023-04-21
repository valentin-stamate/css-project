-- Example INSERT statements for Teachers
INSERT INTO teachers (name, title)
VALUES ('John Doe', 'Professor');
INSERT INTO teachers (name, title)
VALUES ('Jane Smith', 'Associate Professor');
INSERT INTO teachers (name, title)
VALUES ('Bob Johnson', 'Assistant Professor');

-- Example INSERT statements for Disciplines
INSERT INTO disciplines (name, year, semester, has_course, has_laboratory, has_seminary)
VALUES ('Computer Science', 3, 1, 1, 1, 0);
INSERT INTO disciplines (name, year, semester, has_course, has_laboratory, has_seminary)
VALUES ('Mathematics', 2, 1, 1, 0, 1);
INSERT INTO disciplines (name, year, semester, has_course, has_laboratory, has_seminary)
VALUES ('English Literature', 1, 2, 1, 0, 0);

-- Example INSERT statements for Rooms
INSERT INTO rooms (name, can_host_course, can_host_laboratory, can_host_seminary)
VALUES ('C2', 1, 0, 0);
INSERT INTO rooms (name, can_host_course, can_host_laboratory, can_host_seminary)
VALUES ('C410', 0, 1, 1);
INSERT INTO rooms (name, can_host_course, can_host_laboratory, can_host_seminary)
VALUES ('C309', 1, 1, 1);

-- Example INSERT statements for TimeSlots
INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, students_id)
VALUES ('10:00-12:00', 'Monday', 1, 1, 1);
INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, students_id)
VALUES ('14:00-16:00', 'Wednesday', 2, 2, 2);
INSERT INTO TimeSlots (time, weekday, discipline_id, teacher_id, students_id)
VALUES ('09:00-11:00', 'Friday', 3, 3, 2);

-- Example INSERT statements for Students
INSERT INTO students (year, student_group, timeslots)
VALUES (3, 'A1', 1);
INSERT INTO students (year, student_group, timeslots)
VALUES (2, 'B2', 2);
INSERT INTO students (year, student_group, timeslots)
VALUES (1, 'E3', 3);
