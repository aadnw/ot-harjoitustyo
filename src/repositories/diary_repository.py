"""This module  includes functions that are used for diary-based database operations"""

from database_connection import get_database_connection

class DiaryRepository:
    """Takes care of database functions related to the diary markings"""

    def __init__(self):
        """Class constructor
        
        Args:
            connection: Connection-object of the database connection
        """

        self.connection = get_database_connection()

    def add_diary_note(self, dream_id, content):
        """Adds a new diary note for the dream
        
        Args:
            dream_id: integer that describes the dream id to which the new note will be connected to 
            content: string that describes the content of the new note
        """

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO diary (dream_id, content) VALUES (?, ?)",
                       (dream_id, content))
        self.connection.commit()

    def get_diary(self, dream_id):
        """Returns all diary notes related to a dream
        
        Args:
            dream_id: integer that describes the dream id of which diary will be returned
        Returns:
            Returns all diary notes (content and created at) related to the given dream id
        """

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
