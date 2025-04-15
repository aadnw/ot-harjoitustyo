"""This module  includes functions that are used for diary-based database operations"""

from database_connection import get_database_connection

class DiaryRepository:
    """Takes care of database functions related to the diary markings"""
    def __init__(self):
        self.connection = get_database_connection()

    def add_diary_note(self, dream_id, content):
        """Add new diary note for the dream"""

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO diary (dream_id, content) VALUES (?, ?)",
                       (dream_id, content))
        self.connection.commit()

    def get_diary(self, dream_id):
        """Get all diary notes related to a dream"""
        cursor = self.connection.cursor()
        cursor.execute("""SELECT content, created_at FROM diary WHERE dream_id = ?
                       ORDER BY created_at""",
                       (dream_id,))
        return cursor.fetchall()

    def delete_all_diaries(self):
        """Deletes all diary notes from the database table"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM diary")
        self.connection.commit()

diary_repository = DiaryRepository()
