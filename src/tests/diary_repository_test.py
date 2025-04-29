"""This module tests the DiaryRepository functions"""

import unittest
from repositories.dream_repository import dream_repository
from repositories.diary_repository import diary_repository
from repositories.user_repository import user_repository
from entities.dream import Dream
from entities.diary import Diary
from entities.user import User

class TestDiaryRepository(unittest.TestCase):
    """Class for testing the DiaryRepository-class"""

    def setUp(self):
        dream_repository.delete_all_dreams()
        diary_repository.delete_all_diaries()

        self.note_1 = Diary("Askel 1")
        self.note_2 = Diary("Askel 2")
        self.user_testaaja = User("testaaja", "testi123")

    def test_add_diary_note(self):
        """Tests that adding a new note to the diary works as it should"""
        user = user_repository.create_user(self.user_testaaja.username,
                                           self.user_testaaja.password)
        dream = dream_repository.create_new_dream(Dream("Haave 1"))
        diary_repository.add_diary_note(dream.id, user.user_id, self.note_1.content)
        result = diary_repository.get_diary(dream.id)

        self.assertEqual(result[0]['content'], "Askel 1")

    def test_get_diary(self):
        """Tests that get_diary-function returns the diary properly"""
        user = user_repository.create_user(self.user_testaaja.username,
                                           self.user_testaaja.password)
        dream = dream_repository.create_new_dream(Dream("Haave 1"))
        diary_repository.add_diary_note(dream.id, user.user_id, self.note_1.content)
        diary_repository.add_diary_note(dream.id, user.user_id, self.note_2.content)
        result = diary_repository.get_diary(dream.id)

        self.assertEqual(len(result), 2)

    def test_delete_dream_diary(self):
        """Tests that the delete_dream_diary-function deletes the correct diary properly"""
        user = user_repository.create_user(self.user_testaaja.username,
                                           self.user_testaaja.password)
        dream = dream_repository.create_new_dream(Dream("Haave 1"))
        diary_repository.add_diary_note(dream.id, user.user_id, self.note_1.content)

        result = diary_repository.get_diary(dream.id)

        self.assertEqual(len(result), 1)

        diary_repository.delete_dream_diary(dream.id)
        result = diary_repository.get_diary(dream.id)

        self.assertEqual(len(result), 0)

    def test_delete_users_diary(self):
        """Tests that the delete_users_diary-function deletes the correct diary properly"""
        user = user_repository.create_user(self.user_testaaja.username,
                                           self.user_testaaja.password)
        dream = dream_repository.create_new_dream(Dream("Haave 1"))
        diary_repository.add_diary_note(dream.id, user.user_id, self.note_1.content)

        result = diary_repository.get_diary(dream.id)

        self.assertEqual(len(result), 1)

        diary_repository.delete_users_diary(user.user_id)
        result = diary_repository.get_diary(dream.id)

        self.assertEqual(len(result), 0)
