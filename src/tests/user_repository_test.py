"""This module tests the UserRepository functions"""

import unittest
from repositories.user_repository import user_repository, get_users_by_row
from entities.user import User

class TestUserRepository(unittest.TestCase):
    """Class for testing the UserRepository-class"""

    def setUp(self):
        user_repository.delete_all_users()
        self.user_testaaja = User("testaaja", "testi123", 1)
        self.user_kukka = User("kukkis", "kukk4", 1)

    def test_get_all_users(self):
        """Test if get_all_users-funcion works properly"""
        user_repository.create_user(
            self.user_testaaja.username, self.user_testaaja.password)
        user_repository.create_user(
            self.user_kukka.username, self.user_kukka.password)
        result = user_repository.get_all_users()

        self.assertEqual([result[0].username, result[1].username], [
                         'testaaja', 'kukkis'])

    def test_get_user_by_username(self):
        """Tests if get_user_by_username-function works properly"""
        user_repository.create_user(
            self.user_testaaja.username, self.user_testaaja.password)
        result = user_repository.get_user_by_username(
            self.user_testaaja.username)

        self.assertEqual(result.username, self.user_testaaja.username)

    def test_get_user_by_username_returns_nothing_if_there_are_no_users(self):
        """Test that if there are no users the get_user_by_username-function returns None"""
        result = user_repository.get_user_by_username(None)

        self.assertEqual(result, None)

    def test_get_user_by_id(self):
        """Tests that get_user_by_id-function works properly"""
        user_repository.create_user(
            self.user_testaaja.username, self.user_testaaja.password)
        result = user_repository.get_user_by_id(
            self.user_testaaja.user_id)

        self.assertEqual(result.user_id, self.user_testaaja.user_id)

    def test_get_user_by_id_returns_nothing_if_there_are_no_users(self):
        """Test that if there are no users the get_user_by_id-function returns None"""
        result = user_repository.get_user_by_id(None)

        self.assertEqual(result, None)

    def test_get_users_by_row_returns_nothing_if_there_are_no_users(self):
        """Test that if there are no users the get_users_by_row-function returns None"""
        result = get_users_by_row(None)

        self.assertEqual(result, None)

    def test_delete_this_user(self):
        """Tests that delete_this_user-function deletes the correct user"""
        user = user_repository.create_user(self.user_testaaja.username,
                                    self.user_testaaja.password)

        result = user_repository.get_all_users()

        self.assertEqual(len(result), 1)

        user_repository.delete_this_user(user.user_id)

        result = user_repository.get_all_users()

        self.assertEqual(len(result), 0)
