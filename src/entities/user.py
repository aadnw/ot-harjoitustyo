"""This module includes the User class that takes care of storing all user-related information"""
from dataclasses import dataclass

@dataclass
class User:
    """Class taking care of describing the users"""

    def __init__(self, username, password, user_id=None):
        self.username = username
        self.password = password
        self.id = user_id
