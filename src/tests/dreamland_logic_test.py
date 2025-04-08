"""This module tests the DreamlandLogic functions"""

import unittest
from entities.user import User
from entities.dream import Dream
from logic.dreamland_logic import InvalidCredentialsError, UsernameTakenError, DreamlandLogic

class FakeDreamRepositoryForTesting:
    """This is a fake DreamRepository created for testing the dreamland logics"""

    def __init__(self, dreams=None):
        self.dreams = dreams or []

    def get_all_dreams(self):
        """Returns all dreams"""
        return self.dreams

    def get_dreams_by_username(self, username):
        """Returns all dreams from a certain user (current user)"""
        return list(filter(lambda dream: dream.user and dream.user.username == username,
                           self.dreams))

    def create_new_dream(self, dream):
        """Creates a new dream"""
        self.dreams.append(dream)

        return dream

    def set_dream_achieved(self, dream_id, done=True):
        """Marks an achieved dream as done"""
        for dream in self.dreams:
            if dream.id == dream_id:
                dream.done = done
                break

    def delete_all_dreams(self):
        """Deletes all dreams"""
        self.dreams = []

class FakeUserRepositoryForTesting:
    """This is a fake DreamRepository created for testing the dreamland logics"""

    def __init__(self, users=None):
        self.users = users or []

    def get_all_users(self):
        """Returns all users"""
        return self.users

    def get_user_by_username(self, username):
        """Returns user with a specific username"""
        matches = list(filter(lambda user: user.username == username, self.users))

        if len(matches) > 0:
            return matches[0]
        return None

    def create_user(self, username, password):
        """Creates a new user"""
        user = User(username, password)
        self.users.append(user)
        
        return user

    def delete_all_users(self):
        """Deletes all users"""
        self.users = []

class TestDreamlandLogic(unittest.TestCase):
    """Class for testing the DreamlandLogic-class"""

    def setUp(self):
        self.fake_dream_repository = FakeDreamRepositoryForTesting()
        self.fake_user_repository = FakeUserRepositoryForTesting()

        self.dreamland_logic = DreamlandLogic(self.fake_user_repository,
                                              self.fake_dream_repository)

        self.dream_1 = Dream("Haave 1")
        self.dream_2 = Dream("Haave 2")
        self.user_testaaja = User("testaaja", "testi123")

    def login(self, user):
        """Logs in the user"""
        self.dreamland_logic.create_new_user(user.username, user.password)

    def test_login(self):
        """Tests that logging in with valid credentials works as it should"""
        self.dreamland_logic.create_new_user(self.user_testaaja.username,
                                             self.user_testaaja.password)
        result = self.dreamland_logic.login(self.user_testaaja.username,
                                            self.user_testaaja.password)

        self.assertEqual(result.username, self.user_testaaja.username)
