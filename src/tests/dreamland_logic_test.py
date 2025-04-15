"""This module tests the DreamlandLogic functions"""

import unittest
from entities.user import User
from entities.dream import Dream
from entities.diary import Diary
from logic.dreamland_logic import InvalidCredentialsError, UsernameTakenError, DreamlandLogic


class FakeDreamRepositoryForTesting:
    """This is a fake DreamRepository created for testing the dreamland logics"""

    def __init__(self, dreams=None):
        self.dreams = dreams or []
        self._ids = 1

    def get_all_dreams(self):
        """Returns all dreams"""
        return self.dreams

    def get_dreams_by_username(self, username):
        """Returns all dreams from a certain user (current user)"""
        return list(filter(lambda dream: dream.user and dream.user.username == username,
                           self.dreams))

    def create_new_dream(self, dream):
        """Creates a new dream"""
        dream.id = self._ids
        self._ids += 1
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
        matches = list(
            filter(lambda user: user.username == username, self.users))

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

class FakeDiaryRepositoryForTesting:
    """This is a fake DiaryRepository created for testing the dreamland logics"""

    def __init__(self, diary=None):
        self.diary = diary or []

    def get_diary(self, dream_id):
        """Returns all diary notes related to a dream"""
        return list(note for note in self.diary if note.dream_id == dream_id)

    def add_diary_note(self, dream_id, note):
        """"Adds a new note to the diary"""
        note = Diary(content=note, dream_id=dream_id)
        self.diary.append(note)
        return note



class TestDreamlandLogic(unittest.TestCase):
    """Class for testing the DreamlandLogic-class"""

    def setUp(self):
        self.fake_dream_repository = FakeDreamRepositoryForTesting()
        self.fake_user_repository = FakeUserRepositoryForTesting()
        self.fake_diary_repository = FakeDiaryRepositoryForTesting()

        self.dreamland_logic = DreamlandLogic(self.fake_user_repository,
                                              self.fake_dream_repository,
                                              self.fake_diary_repository)

        self.dream_1 = Dream("Haave 1")
        self.dream_2 = Dream("Haave 2")
        self.user_testaaja = User("testaaja", "testi123")

    def login(self):
        """Logs in the user"""
        self.dreamland_logic.create_new_user(self.user_testaaja.username,
                                             self.user_testaaja.password)
        self.dreamland_logic.login(self.user_testaaja.username,
                                   self.user_testaaja.password)

        return self.user_testaaja

    def test_login(self):
        """Tests that logging in with valid credentials works as it should"""
        result = self.login()

        self.assertEqual(result.username, self.user_testaaja.username)

    def test_login_fails(self):
        """Tests that logging in with invalid credentials prints an error message"""
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.dreamland_logic.login("testaaja", "testi1"))

    def test_get_user(self):
        """Tests that get_user function returns the current user"""
        self.login()

        result = self.dreamland_logic.get_user()

        self.assertEqual(result.username, "testaaja")

    def test_logout(self):
        """Tests that logging out works as it should"""
        self.login()

        self.assertEqual(self.dreamland_logic.logout(), None)

    def test_create_new_user(self):
        """Tests that creating a new user with valid credentials works as it should"""
        self.login()

        result = self.dreamland_logic.get_user()
        self.assertEqual(result.username, "testaaja")

    def test_create_new_user_with_taken_username_fails(self):
        """Tests that user can't register with a taken username"""
        self.dreamland_logic.create_new_user(self.user_testaaja.username,
                                             self.user_testaaja.password)

        self.assertRaises(UsernameTakenError, lambda: self.dreamland_logic.create_new_user(
            self.user_testaaja.username, "erisalasana"))

    def test_create_new_user_with_too_short_username_fails(self):
        """Tests that user can't register with a too short username"""
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.dreamland_logic.create_new_user("te", "salasana"))

    def test_create_new_user_with_too_long_username_fails(self):
        """Tests that user can't register with a too long username"""
        self.assertRaises(InvalidCredentialsError, lambda: self.dreamland_logic.create_new_user(
            "Tämä on aivan liian pitkä", "salasana"))

    def test_create_new_user_with_too_short_password_fails(self):
        """Tests that user can't register with a too short password"""
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.dreamland_logic.create_new_user("testaaja", "sala"))

    def test_new_dream(self):
        """Tests that adding a new dream works properly"""
        self.login()

        self.dreamland_logic.new_dream("Testi")
        dreams = self.dreamland_logic.get_unachieved_dreams()

        self.assertEqual(len(dreams), 1)
        self.assertEqual(dreams[0].content, "Testi")
        self.assertEqual(dreams[0].user.username, self.user_testaaja.username)

    def test_get_unachieved_dreams(self):
        """Tests that the function returns the correct dreams (unachieved ones)"""
        self.login()

        self.dreamland_logic.new_dream("Testi")
        result = self.dreamland_logic.get_unachieved_dreams()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].content, "Testi")

    def test_if_user_not_logged_in_no_dreams_are_returned(self):
        """Tests that get_unachieved_dreams -function doesn't work if user's not logged in"""
        self.dreamland_logic.new_dream("Testi")
        result = self.dreamland_logic.get_unachieved_dreams()

        self.assertEqual(result, [])

    def test_dream_achieved(self):
        """Tests that marking a dream achieved works as it should"""
        self.login()

        self.dreamland_logic.new_dream("Testi")
        result = self.dreamland_logic.get_unachieved_dreams()
        self.dreamland_logic.dream_achieved(result[0].id)

        self.assertEqual(len(self.dreamland_logic.get_unachieved_dreams()), 0)

    def test_new_diary_note(self):
        """Tests that the adding a new note to the diary works properly"""
        self.login()

        self.dreamland_logic.new_dream("Testi")
        dream = self.dreamland_logic.get_unachieved_dreams()
        result = self.dreamland_logic.new_diary_note(dream[0].id, "Testasin haavetta")

        self.assertEqual(result.content, "Testasin haavetta")

    def test_get_diary(self):
        """Tests that the get_diary-function returns the correct diary"""
        self.login()

        self.dreamland_logic.new_dream("Testi")
        dream = self.dreamland_logic.get_unachieved_dreams()
        self.dreamland_logic.new_diary_note(dream[0].id, "Testasin haavetta")
        self.dreamland_logic.new_diary_note(dream[0].id, "Toinen muistiinpano")
        result = self.dreamland_logic.get_dream_diary(dream[0].id)

        self.assertEqual(len(result), 2)
        