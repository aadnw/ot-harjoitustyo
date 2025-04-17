"""This module includes the Dream class that takes care of storing all dream-related information"""
from dataclasses import dataclass

@dataclass
class Dream():
    """Class taking care of describing dreams"""

    def __init__(self, content, done=False, user=None, dream_id=None, star=1):
        self.content = content
        self.done = done
        self.user = user
        self.id = dream_id
        self.star = star
