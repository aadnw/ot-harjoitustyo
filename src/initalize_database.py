"""This module creates the tables for the database"""

from database_connection import get_database_connection


def remove_tables(connection):
    """If tables already exist, delete them"""
    cursor = connection.cursor()

    cursor.execute("drop table if exists users")
    cursor.execute("drop table if exists diary")

    connection.commit()


def create_tables(connection):
    """Creates the tables needed for the application"""
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
                   id integer primary key,
                   username text,
                   password text
        )''')
    cursor.execute('''
        create table diary (
                   id integer primary key autoincrement,
                   dream_id integer,
                   user_id integer,
                   content text,
                   created_at timestamp default current_timestamp,
                   foreign key (dream_id) references dreams (id) on delete cascade,
                   foreign key (user_id) references users (id) on delete cascade
        )''')
    connection.commit()


def initialize_database():
    """Creates the database"""
    connection = get_database_connection()

    remove_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
