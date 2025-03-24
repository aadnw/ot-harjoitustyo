import os
import sqlite3
from config import DATABASE_FILE_PATH

dirname = os.path.dirname(__file__)
os.makedirs(os.path.dirname(DATABASE_FILE_PATH), exist_ok=True)
connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection









