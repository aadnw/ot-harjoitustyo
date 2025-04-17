"""This module includes the Diary class that takes care of storing all diary notes"""
from dataclasses import dataclass

@dataclass
class Diary:
    """Class taking care of describing diary notes"""
    content: str
    dream_id: int = None
