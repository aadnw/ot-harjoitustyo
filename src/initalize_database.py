from database_connection import get_database_connection


def remove_tables(connection):
    cursor = connection.cursor()

    cursor.execute("drop table if exists users")
    cursor.execute("drop table if exists dreams")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
                   id integer primary key,
                   username text,
                   password text
        )''')
    cursor.execute('''
        create table dreams (
                   id integer primary key,
                   content text
        )''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    remove_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
