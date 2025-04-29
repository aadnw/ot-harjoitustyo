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

    def test_get_dream_by_id(self):
        """Tests that get_dream_by_id-function returns the correct dream"""
        dream_repository.create_new_dream(self.dream_2)
        dream = dream_repository.create_new_dream(self.dream_1)

        result = dream_repository.get_dream_by_id(dream.id)

        self.assertEqual(result.content, "Haave 1")

    def test_get_dream_by_id_returns_none_if_id_doesnt_match_a_dream(self):
        """Tests that get_dream_by_id-function returns None if there's no matches"""
        dream_repository.create_new_dream(self.dream_1)
        dream_repository.create_new_dream(self.dream_2)

        result = dream_repository.get_dream_by_id(5)

        self.assertEqual(result, None)

    def test_get_dreams_by_username(self):
        """Tests that get_dreams_by_username returns the correct dreams"""
        testaaja = user_repository.create_user(self.user_testaaja.username,
                                               self.user_testaaja.password)
        dream_repository.create_new_dream(
            Dream(content="Haave 1", user=testaaja))
        result = dream_repository.get_dreams_by_username(
            self.user_testaaja.username)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].content, "Haave 1")

    def test_create_new_dream(self):
        """Tests that dream creation works as it should"""
        result = dream_repository.create_new_dream(self.dream_1)

        self.assertEqual(result.content, "Haave 1")

    def test_set_dream_achieved(self):
        """Tests that setting a dream as achieved works as it should"""
        dream = dream_repository.create_new_dream(self.dream_1)
        dream_repository.create_new_dream(self.dream_2)

        self.assertEqual(dream.done, False)

        achieved = dream_repository.set_dream_achieved(dream.id)

        self.assertEqual(achieved.done, True)

    def test_set_dream_star(self):
        """Tests that changing the star rating of a dream works properly"""
        dream = dream_repository.create_new_dream(self.dream_1)
        dream_repository.create_new_dream(self.dream_2)

        self.assertEqual(dream.star, 1)

        dream_repository.set_dream_star(dream.id, 4)
        dream = dream_repository.get_dream_by_id(dream.id)

        self.assertEqual(dream.star, 4)

    def test_delete_this_dream(self):
        """Tests that deleting the given dream actually deletes it"""
        dream_1 = dream_repository.create_new_dream(self.dream_1)
        dream_repository.create_new_dream(self.dream_2)
        result = dream_repository.get_all_dreams()

        self.assertEqual(len(result), 2)

        dream_repository.delete_this_dream(dream_1.id)
        result = dream_repository.get_all_dreams()

        self.assertEqual(len(result), 1)

    def test_delete_all_users_dreams(self):
        """Tests that deleting all given user's dreams get deleted properly"""
        testaaja = user_repository.create_user(self.user_testaaja.username,
                                               self.user_testaaja.password)
        kukka = user_repository.create_user(self.user_kukka.username,
                                               self.user_kukka.password)
        dream_repository.create_new_dream(
            Dream(content="Haave 1", user=testaaja))
        dream_repository.create_new_dream(
            Dream(content="Haave 2", user=kukka))

        dream_repository.delete_all_users_dreams(testaaja.username)

        result = dream_repository.get_all_dreams()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].content, "Haave 2")
