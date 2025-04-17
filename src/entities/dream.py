"""This module includes the Dream class that takes care of storing all dream-related information"""
from dataclasses import dataclass

@dataclass
class Dream():
    """Class taking care of describing dreams"""
    content: str
    done: bool = False
    user: str = None
    id: int = None
    star: int = 1
