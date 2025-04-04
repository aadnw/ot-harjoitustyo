from entities.user import User
from entities.dream import Dream

from repositories.user_repository import (
    user_repository as default_user_repository)

from repositories.dream_repository import (
    dream_repository as default_dream_repository)

class InvalidCredentialsError(Exception):
    """Error message about invalid credentials"""
    
class UsernameTakenError(Exception):
    """Error message about username being already taken"""

class DreamlandLogic:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, user_repository=default_user_repository,
                 dream_repository=default_dream_repository):
        self._user = None
        self._user_repository = user_repository
        self._dream_repository = dream_repository

    def login(self, username, password):
        """Handle login, print error message if login fails"""
        user = self._user_repository.get_user_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError(
                "Virheellinen käyttäjänimi tai salasana")

        self._user = user
        return user

    def get_user(self):
        """Return the current user"""
        return self._user

    def logout(self):
        """Handle user logging out"""
        self._user = None

    def create_new_user(self, username, password, login=True):
        """Create new user that includes a unique username that is 3-20 characters long and
        a password that needs to be at least 5 characters long; if not, print error message"""
        username_exists = self._user_repository.get_user_by_username(username)

        if username_exists:
            raise UsernameTakenError("Tämä käyttäjänimi on jo käytetty")

        user = self._user_repository.create_user(User(username, password))

        if not 3 <= len(user.username) <= 20:
            raise InvalidCredentialsError(
                "Käyttäjänimen tulee olla 3-20 merkkiä")

        if len(user.password) < 5:
            raise InvalidCredentialsError(
                "Salasanan tulee olla vähintään 5 merkkiä")

        if login:
            self._user = user
        return user

    def new_dream(self, content):
        """Creates new dream throgh the sovelluslogiikka"""
        dream = Dream(content=content, user=self._user)
        return self._dream_repository.create_new_dream(dream)

    def get_unachieved_dreams(self):
        """Returns all the active dreams to show on homepage"""
        if not self._user:
            return []

        dreams = self._dream_repository.get_dreams_by_username(self._user.username)

        return list(filter(lambda dream: not dream.done, dreams))

    def dream_achieved(self, dream_id):
        """Dream achieved disappears from the homepage"""
        self._dream_repository.set_dream_achieved(dream_id)


dreamland_logic = DreamlandLogic()
