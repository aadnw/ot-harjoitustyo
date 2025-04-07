"""This module includes functions used for user-related database operations"""

from database_connection import get_database_connection
from entities.user import User


def get_users_by_row(row):
    """Returns all user information"""
    if row:
        return User(row["username"], row["password"], user_id=row["id"])
    return None


class UserRepository:
    """Takes care of database functions related to the users"""
    def __init__(self, connection):
        self._connection = connection

    def get_all_users(self):
        """Returns all users"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")

        return list(map(get_users_by_row, cursor.fetchall()))

    def get_user_by_username(self, username):
        """Returns a specific user (current user)"""
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        if row:
            return get_users_by_row(row)
        return None

    def create_user(self, username, password):
        """Adds a new user into the database table"""
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        self._connection.commit()

        user_id = cursor.lastrowid

        return User(username, password, user_id=user_id)

    def delete_all_users(self):
        """Deletes all users from the database table"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
