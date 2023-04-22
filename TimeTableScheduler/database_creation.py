import csv
import os.path
import sqlite3


def execute_insert_statement(statement: str, conn):
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()


def insert_teachers(conn):
    rows = []
    file_path = os.path.join(os.getcwd(), "data", "teachers.csv")
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            rows.append(row)

    rows = rows[1:]
    for row in rows:
        sql = "INSERT INTO Teachers(name,title) VALUES('%s', '%s')" % (row[0], row[1])
        execute_insert_statement(sql, conn)


def insert_student_groups(conn):
    rows = []
    file_path = os.path.join(os.getcwd(), "data", "studentgroups.csv")
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            rows.append(row)

    rows = rows[1:]
    for row in rows:
        sql = "INSERT INTO StudentGroups(year,group_name) VALUES('%s', '%s')" % (row[0], row[1])
        execute_insert_statement(sql, conn)


def insert_rooms(conn):
    rows = []
    file_path = os.path.join(os.getcwd(), "data", "rooms.csv")
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            rows.append(row)

    rows = rows[1:]
    for row in rows:
        sql = "INSERT INTO Rooms(name,can_host_course,can_host_laboratory,can_host_seminary) VALUES('%s', %s, %s, %s)" % \
                    (row[0], row[1], row[2], row[3])
        execute_insert_statement(sql, conn)


def insert_disciplines(conn):
    rows = []
    file_path = os.path.join(os.getcwd(), "data", "disciplines.csv")
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            rows.append(row)

    rows = rows[1:]
    for row in rows:
        sql = "INSERT INTO Disciplines(name,for_year_1,for_year_2,for_year_3,for_year_4,for_year_5,semester," \
                    "has_course,has_laboratory,has_seminary) VALUES('%s', %s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
                    (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        execute_insert_statement(sql, conn)


def main():
    db_name = "db.sqlite3"
    db_path = os.path.join(os.getcwd(), db_name)
    sql_script = "database_creation.sql"

    if os.path.exists(db_path):
        os.remove(db_path)

    with open(sql_script, 'r') as sql_file:
        sql_script_content = sql_file.read()

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    cursor.executescript(sql_script_content)
    conn.commit()

    insert_teachers(conn)
    insert_disciplines(conn)
    insert_rooms(conn)
    insert_student_groups(conn)


    conn.close()


if __name__ == "__main__":
    main()