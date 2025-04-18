"""This module makes connection with the database"""

import sqlite3
from config import DATABASE_FILE_PATH


def get_database_connection():
    """Returns connection to the database"""
    connection = sqlite3.connect(DATABASE_FILE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
