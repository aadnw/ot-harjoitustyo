"""This module includes the Diary class that takes care of storing all diary notes"""
from dataclasses import dataclass

@dataclass
class Diary:
    """Class taking care of describing diary notes
    
    Attributes:
        content: string that describes the diary note
        dream_id: integer that is the dream id the diary note is related to
        user_id: integer that is the user's id who created the diary note
    """
    content: str
    dream_id: int = None
    user_id: int = None
