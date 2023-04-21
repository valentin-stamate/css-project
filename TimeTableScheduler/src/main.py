from src.database_connection import DatabaseConnection


def main():
    pass


if __name__ == '__main__':
    conn = DatabaseConnection().get_instance()
    print(conn.get_all_rows('Rooms'))
