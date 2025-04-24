"""This module includes the User class that takes care of storing all user-related information"""
from dataclasses import dataclass

@dataclass
class User:
    """Class taking care of describing the users
    
    Attributes:
        username: string that describes the username of the user
        password: string that describes the password of the user
        user_id: integer that describes the id of the user
    """
    username: str
    password: str
    user_id: int = None
