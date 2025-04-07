"""This module tests the user_repository functions"""

import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    """Class for testing the UserRepository-class"""

    def setUp(self):
        user_repository.delete_all_users()
        self.user_testaaja = User("testaaja", "testi123")
        self.user_kukka = User("kukkis", "kukk4")

    def test_get_all_users(self):
        """Test if get_all_users-funcion works properly"""
        user_repository.create_user(
            self.user_testaaja.username, self.user_testaaja.password)
        user_repository.create_user(
            self.user_kukka.username, self.user_kukka.password)
        result = user_repository.get_all_users()

        self.assertEqual([result[0].username, result[1].username], [
                         'testaaja', 'kukkis'])
