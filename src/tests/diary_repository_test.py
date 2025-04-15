"""This module tests the DiaryRepository functions"""

import unittest
from repositories.dream_repository import dream_repository
from repositories.diary_repository import diary_repository
from entities.dream import Dream
from entities.diary import Diary


class TestDiaryRepository(unittest.TestCase):
    """Class for testing the DiaryRepository-class"""

    def setUp(self):
        dream_repository.delete_all_dreams()
        diary_repository.delete_all_diaries()

        self.note_1 = Diary("Askel 1")
        self.note_2 = Diary("Askel 2")

    def test_add_diary_note(self):
        """Tests that adding a new note to the diary works as it should"""
        dream = dream_repository.create_new_dream(Dream("Haave 1"))
        diary_repository.add_diary_note(dream.id, self.note_1.content)
        result = diary_repository.get_diary(dream.id)

        self.assertEqual(result[0]['content'], "Askel 1")

    def test_get_diary(self):
        """Tests that get_diary-function returns the diary properly"""
        dream = dream_repository.create_new_dream(Dream("Haave 1"))
        diary_repository.add_diary_note(dream.id, self.note_1.content)
        diary_repository.add_diary_note(dream.id, self.note_2.content)
        result = diary_repository.get_diary(dream.id)

        self.assertEqual(len(result), 2)
