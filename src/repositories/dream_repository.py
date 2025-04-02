from entities.dream import Dream
from repositories.user_repository import user_repository
from database_connection import get_database_connection


class DreamRepository:
    """Takes care of database functions related to the dreams"""

    def __init__(self):
        self._connection = get_database_connection()

    def get_all_dreams(self):
        """Returns all added dreams"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, content, user_id FROM dreams")
        rows = cursor.fetchall()

        dreams = []
        for row in rows:
            dream_id, content, user_id = row
            user = user_repository.get_user_by_user_id(user_id) if user_id else None
            dreams.append(Dream(content, False, user, dream_id))

        return dreams
    
    def find_dream_by_username(self, username):
        """Returns all dreams of a specific user (the current user)"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT d.id, d.content, d.done, d.user_id FROM dreams d LEFT JOIN users u ON d.user_id = u.id WHERE u.username = ?", (username,))
        rows = cursor.fetchall()

        dreams = []
        for row in rows:
            dream_id, content, done, user_id = row
            user = user_repository.get_user_by_user_id(user_id)
            dreams.append(Dream(content, done, user, dream_id))

        return dreams

    def create_new_dream(self, dream):
        """Adds the new dream to the database table"""
        cursor = self._connection.cursor()
        if dream.user:
            dream_user_id = dream.user.id
        else:
            dream_user_id = None

        cursor.execute(
            "INSERT INTO dreams (content, user_id, done) VALUES (?, ?, ?)",
            (dream.content, dream_user_id, dream.done)
            )
        self._connection.commit()

        dream_id = cursor.lastrowid
        dream.id = dream_id

        return dream

    def set_dream_achieved(self, dream_id, done=True):
        """Deletes the dream from the database table"""
        cursor = self._connection.cursor()
        
        dreams = self.get_all_dreams()
        for dream in dreams:
            if dream.id == dream_id:
                dream.done = done
                cursor.execute("UPDATE dreams SET done = ? WHERE id = ?", (True, dream_id))
                break
        self._connection.commit()
   
dream_repository = DreamRepository()