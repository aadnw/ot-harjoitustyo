"""This module  includes functions that are used for diary-based database operations"""

from database_connection import get_database_connection

class DiaryRepository:
    """Takes care of database functions related to the diary markings"""

    def __init__(self):
        """Class constructor"""

        self.connection = get_database_connection()

    def add_diary_note(self, dream_id, user_id, content):
        """Adds a new diary note for the dream
        
        Args:
            dream_id: integer that describes the dream id to which the new note will be connected to 
            user_id: integer that describes the id of the user that created the new note
            content: string that describes the content of the new note
        """

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO diary (dream_id, user_id, content) VALUES (?, ?, ?)",
                       (dream_id, user_id, content))
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

    def delete_dream_diary(self, dream_id):
        """Deletes a dream's diary when a dream is deleted
        
        Args:
            dream_id: integer that describes the id of the dream of which diary will be deleted
        """

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM diary WHERE dream_id = ?", (dream_id,))
        self.connection.commit()

    def delete_users_diary(self, user_id):
        """Deletes given user's entire diary
        
        Args:
            user_id: integer that describes the id of the user whose diary will be deleted
        """

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM diary WHERE user_id = ?", (user_id,))
        self.connection.commit()

    def delete_all_diaries(self):
        """Deletes all diary notes from the database table"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM diary")
        self.connection.commit()

diary_repository = DiaryRepository()
