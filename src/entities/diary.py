"""This module includes the Diary class that takes care of storing all diary notes"""
from dataclasses import dataclass

@dataclass
class Diary:
    """Class taking care of describing diary notes
    
    Attributes:
        content: string that describes the diary note
        dream_id: integer that is the dream id the diary note is related to
    """
    content: str
    dream_id: int = None
