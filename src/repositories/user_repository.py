from database_connection import get_database_connection
from entities.user import User


def get_users_by_row(row):
    """Returns all user information"""
    if row:
        return User(row["username"], row["password"])
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

        return get_users_by_row(cursor.fetchone())

    def create_user(self, user):
        """Adds a new user into the database table"""
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (user.username, user.password))
        self._connection.commit()
        return user

    def delete_all_users(self):
        """Deletes all users from the database table"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
