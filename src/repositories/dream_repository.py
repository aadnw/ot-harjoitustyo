"""This module includes functions that are used for dream-related database operations"""

from pathlib import Path
from entities.dream import Dream
from repositories.user_repository import user_repository
from config import DREAMS_FILE_PATH
from database_connection import get_database_connection


class DreamRepository:
    """Takes care of database functions related to the dreams
    
    Attributes:
        file_path: Path to the file where all the dreams are stored
    """
    def __init__(self, file_path):
        """Class constructor
        
        Args:
            file_path: Path to the file where all the dreams are stored
            connection: Connection-object of the database connection
        """

        self._file_path = file_path
        self.connection = get_database_connection()

    def get_all_dreams(self):
        """Returns all added dreams
        
        Returns:
            List of Dream-objects
        """

        return self._read()

    def get_dream_by_id(self, dream_id):
        """Returns dream with the given id
        
        Args:
            dream_id: integer that describes the dream id
        Returns:
            Dream-object with the given id
        """

        dreams = self.get_all_dreams()

        for dream in dreams:
            if dream.id == dream_id:
                return dream
        return None

    def get_dreams_by_username(self, username):
        """Returns all dreams of a specific user (the current user)
        
        Args:
            username: string that describes the user of which dreams will be returned
        Returns:
            List of Dream-objects that belong tho the given user
        """

        dreams = self.get_all_dreams()

        return list(filter(lambda dream: dream.user and dream.user.username == username, dreams))

    def create_new_dream(self, dream):
        """Adds a new dream to the database table

        Args:
            dream: Dream-object that is the new dream
        Returns:
            Returns the new dream as a Dream-object
        """

        dreams = self.get_all_dreams()
        ids = [int(d.id) for d in dreams if d.id is not None]
        dream.id = max(ids, default=0) + 1
        dreams.append(dream)
        self._write(dreams)
        return dream

    def set_dream_achieved(self, dream_id, done=True):
        """Marks the dream as done (sets the done value to False)
        
        Args:
            dream_id: integer that describes the id of the dream that will be marked as achieved
            done: boolean value that is assumed to be True, will be set as False when dream is
            marked as achieved
        
        Returns:
            Returns the achieved dream as Dream-object
        """

        dreams = self.get_all_dreams()
        achieved_dream = None
        for dream in dreams:
            if dream.id == dream_id:
                dream.done = done
                achieved_dream = dream


        self._write(dreams)
        return achieved_dream

    def set_dream_star(self, dream_id, set_star):
        """Updates the star rating of a dream
        
        Args:
            dream_id: integer that describes the id of the dream of which star rating will be
            changed
            set_star: integer that describes the new star value
        """

        dreams = self.get_all_dreams()
        for dream in dreams:
            if dream.id == dream_id:
                dream.star = set_star

        self._write(dreams)


    def delete_this_dream(self, dream_id):
        """Deletes dream with a chosen id
        
        Args:
            dream_id: integer that describes the id of the dream that will be deleted
        """

        dreams = self.get_all_dreams()

        dream_deleted = filter(lambda dream: dream.id != dream_id, dreams)

        self._write(dream_deleted)

    def delete_all_dreams(self):
        """Deletes all dreams"""
        self._write([])

    def _ensure_file_exists(self):
        """Creates a file if it doesn't exist, to store data"""
        Path(self._file_path).touch()

    def _read(self):
        """Reads data from the csv file
        
        Returns:
            content in the csv file
        """
        dreams = []
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                dream_id = int(parts[0])
                content = parts[1]
                done = parts[2].strip() == "1"
                username = parts[3]
                star = f"{parts[4]}/5"

                if username:
                    user = user_repository.get_user_by_username(username)
                else:
                    user = None

                dreams.append(Dream(content, done, user, dream_id, star))

        return dreams

    def _write(self, dreams):
        """Updates/writes data in the csv file"""
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for dream in dreams:
                done_string = "1" if dream.done else "0"

                if dream.user:
                    username = dream.user.username
                else:
                    username = ""

                row = f"{dream.id};{dream.content};{done_string};{username};{dream.star}"

                file.write(row+"\n")


dream_repository = DreamRepository(DREAMS_FILE_PATH)
