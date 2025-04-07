"""This module tests the DreamRepository functions"""

import unittest
from repositories.dream_repository import dream_repository
from repositories.user_repository import user_repository
from entities.dream import Dream
from entities.user import User

class TestDreamRepository(unittest.TestCase):
    """Class for testing the DreamRepository-class"""

    def setUp(self):
        dream_repository.delete_all_dreams()
        user_repository.delete_all_users()

        self.dream_1 = Dream("Haave 1")
        self.dream_2 = Dream("Haave 2")
        self.user_testaaja = User("testaaja", "testi123")
        self.user_kukka = User("kukkis", "kukk4")

    def test_get_all_dreams(self):
        """Tests that get_all_dreams returns all dreams"""
        dream_repository.create_new_dream(self.dream_1)
        dream_repository.create_new_dream(self.dream_2)
        result = dream_repository.get_all_dreams()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].content, self.dream_1.content)
        self.assertEqual(result[1].content, self.dream_2.content)

    def test_get_dreams_by_username(self):
        """Tests that get_dreams_by_username returns the correct dreams"""
        testaaja = user_repository.create_user(self.user_testaaja.username,
                                               self.user_testaaja.password)
        dream_repository.create_new_dream(Dream(content="Haave 1", user=testaaja))
        result = dream_repository.get_dreams_by_username(self.user_testaaja.username)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].content, "Haave 1")

    def test_create_new_dream(self):
        """Tests that dream creation works as it should"""
        result = dream_repository.create_new_dream(self.dream_1)

        self.assertEqual(result.content, "Haave 1")
        