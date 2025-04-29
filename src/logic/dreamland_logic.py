"""This module includes functions that are used for the application logics"""

from entities.dream import Dream
from entities.diary import Diary

from repositories.user_repository import (
    user_repository as default_user_repository)

from repositories.dream_repository import (
    dream_repository as default_dream_repository)

from repositories.diary_repository import (
    diary_repository as default_diary_repository)


class InvalidCredentialsError(Exception):
    """Error message about invalid credentials"""


class UsernameTakenError(Exception):
    """Error message about username being already taken"""


class DreamlandLogic:
    """Class taking care of the application logics
    
    Attributes:
        user: describes who is the user
        user_repository: UserRepository object that has the same methods as the UserRepository-class
        dream_repository: DreamRepository object that has the same methods as the
        DreamRepository-class
        diary_repository: DiaryRepository object that has the same methods as the
        DiaryRepository-class
    """

    def __init__(self, user_repository=default_user_repository,
                 dream_repository=default_dream_repository,
                 diary_repository=default_diary_repository):
        """Class constructor that creates a new service to take care of the application logic
        
        Args:
            user_repository: UserRepository object that has the same methods as the
            UserRepository-class
            dream_repository: DreamRepository object that has the same methods as the
            DreamRepository-class
            diary_repository: DiaryRepository object that has the same methods as the
            DiaryRepository-class
        """

        self._user = None
        self._user_repository = user_repository
        self._dream_repository = dream_repository
        self._diary_repository = diary_repository

    def login(self, username, password):
        """Logs in the user, prints error message if login fails
        
        Args:
            username: string that describes the user that is about to login
            passwors: string that describes the user's password that is about to login
        Returns:
            Logged in user as a User-object
        Raises:
            InvalidCredentialsError: error that occurs when the username and/or password don't match
        """

        user = self._user_repository.get_user_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError(
                "Virheellinen käyttäjänimi tai salasana")

        self._user = user
        return user

    def get_user(self):
        """Returns the current user
        
        Returns:
            Current logged in user as a User-object
        """

        return self._user

    def logout(self):
        """Logs out the current user"""
        self._user = None

    def create_new_user(self, username, password, login=True):
        """Creates a new user that includes a unique username that is 3-20 characters long and
        a password that needs to be at least 5 characters long; if not, prints error messag
        
        Args:
            username: string that describes the new username
            password: string that describes the new password
            login: optional boolean value that is assumed as True, tells whether the registration
            succeeded (True) or not (False), (does the new user get logged in or not)

        Raises:
            UsernameTakenError: error that occurs when the username is already in use by another
            user
            InvalidCredentialsError: error that occurs when the username and/or password length
            isn't following the given length

        Returns:
            New user as a User-object

        """

        username_exists = self._user_repository.get_user_by_username(username)

        if username_exists:
            login = False
            raise UsernameTakenError("Tämä käyttäjänimi on jo käytetty")

        if len(username) < 3 or len(username) > 20:
            login = False
            raise InvalidCredentialsError(
                "Käyttäjänimen tulee olla 3-20 merkkiä")

        if len(password) < 5:
            login = False
            raise InvalidCredentialsError(
                "Salasanan tulee olla vähintään 5 merkkiä")

        user = self._user_repository.create_user(username, password)

        if login:
            self._user = user
        return user

    def delete_user(self, user_id):
        """Deletes user and all information (dreams and diary) related to them
        
        Args:
            user_id: integer that describes the user's id that is to be deleted
        """

        user = self._user_repository.get_user_by_id(user_id)

        if user:
            self._dream_repository.delete_all_users_dreams(user.username)
            self._user_repository.delete_this_user(user_id)

    def new_dream(self, content, due_date):
        """Creates a new dream
        
        Args: 
            content: string that describes the content of the dream to be created
            due_date: string that describes the due date of the dream to be created
        Returns:
            Created dream as Dream-object
        """

        dream = Dream(content=content, user=self._user, due_date=due_date)
        self._dream_repository.create_new_dream(dream)

        return dream

    def get_unachieved_dreams(self):
        """Returns all the active dreams to show on homepage
        
        Returns:
            Returns all the unachieved dreams of a user as a list of Dream-objects.
            If there's not user logged in, returns an empty list
        """

        if not self._user:
            return []

        dreams = self._dream_repository.get_dreams_by_username(
            self._user.username)

        return list(filter(lambda dream: not dream.done, dreams))

    def dream_achieved(self, dream_id):
        """Marks a certain dream as achieved
        
        Args:
            dream_id: integer that describes the id of the dream to be achieved
        """

        self._dream_repository.set_dream_achieved(dream_id)

    def dream_star(self, dream_id, set_star):
        """Sets the star value for a dream
        
        Args:
            dream_id: integer that describes the id of the dream that will get the star value
            set_star: integer that describes the star amount to be set for the dream
        """

        self._dream_repository.set_dream_star(dream_id, set_star)

    def delete_dream(self, dream_id):
        """Deletes a certain dream
        
        Args:
            dream_id: integer that describes the id of the dream to be deleted
        """

        self._dream_repository.delete_this_dream(dream_id)

    def get_dream_diary(self, dream_id):
        """Returns all diary notes related to a dream on the dream page
        
        Args:
            dream_id: integer that describes the id of the dream of which diary will be returned
        Returns:
            Returns a list of notes related to the given dream as Diary-objects
        """

        notes = self._diary_repository.get_diary(dream_id)

        return list(notes)

    def new_diary_note(self, dream_id, content):
        """Adds a new note to the dream diary
        
        Args:
            dream_id: integer that describes the dream id to which the new note will be connected
            content: string that describes the content of the new note
        
        Returns:
            Returns the new note as Diary-object
        """

        dream_id = int(dream_id)
        note = Diary(content=content)
        self._diary_repository.add_diary_note(dream_id, note.content)
        return note



dreamland_logic = DreamlandLogic()
