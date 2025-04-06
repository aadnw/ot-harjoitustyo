from entities.dream import Dream
from pathlib import Path
from repositories.user_repository import user_repository
from config import DREAMS_FILE_PATH
from database_connection import get_database_connection


class DreamRepository:
    """Takes care of database functions related to the dreams"""

    def __init__(self, file_path):
        self._file_path = file_path
        self.connection = get_database_connection()

    def get_all_dreams(self):
        """Returns all added dreams"""
        return self._read()

    def get_dreams_by_username(self, username):
        """Returns all dreams of a specific user (the current user)"""
        dreams = self.get_all_dreams()

        return list(filter(lambda dream: dream.user and dream.user.username == username, dreams))

    def create_new_dream(self, dream):
        """Adds the new dream to the database table"""
        dreams = self.get_all_dreams()
        dream.id = max([int(dream.id) for dream in dreams], default=0) + 1
        dreams.append(dream)
        self._write(dreams)
        return dream

    def set_dream_achieved(self, dream_id, done=True):
        """Deletes the dream from the database table"""
        dreams = self.get_all_dreams()
        for dream in dreams:
            if dream.id == dream_id:
                dream.done = done
                break

        self._write(dreams)

    def delete_dream(self, dream_id):
        dreams = self.get_all_dreams()

        self._write(filter(lambda dream: dream.id != dream_id, dreams))

    def delete_all_dreams(self):
        self._write([])

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        dreams = []
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                dream_id = parts[0]
                content = parts[1]
                done = parts[2] == "1"
                username = parts[3]

                if username:
                    user = user_repository.get_user_by_username(username)
                else:
                    user = None

                dreams.append(Dream(content, done, user, dream_id))

        return dreams
    
    def _write(self, dreams):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for dream in dreams:
                done_string = "1" if dream.done else "0"

                if dream.user:
                    username = dream.user.username
                else:
                    username = ""

                row = f"{dream.id};{dream.content};{done_string};{username}"

                file.write(row+"\n")
                
dream_repository = DreamRepository(DREAMS_FILE_PATH)