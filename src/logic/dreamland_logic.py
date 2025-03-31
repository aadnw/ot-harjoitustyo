from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)


class InvalidCredentialsError(Exception):
    pass


class UsernameTakenError(Exception):
    pass


class DreamlandLogic:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.get_user_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError(
                "Virheellinen käyttäjänimi tai salasana")

        self._user = user
        return user

    def get_user(self):
        return self._user

    def logout(self):
        self._user = None

    def create_new_user(self, username, password, login=True):
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


dreamland_logic = DreamlandLogic()
