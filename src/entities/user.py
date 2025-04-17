"""This module includes the User class that takes care of storing all user-related information"""
from dataclasses import dataclass

@dataclass
class User:
    """Class taking care of describing the users"""
    username: str
    password: str
    user_id: int = None
