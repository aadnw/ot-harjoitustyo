"""This module includes the Dream class that takes care of storing all dream-related information"""
from dataclasses import dataclass

@dataclass
class Dream:
    """Class taking care of describing dreams
    
    Attributes:
        content: string that describes the content of the dream
        done: boolean value that describes whether the dream has been achieved or not
        user: string that describes who is the user that created the dream
        id: integer that describes the id of the dream
        star: integer that describes the importancy of the dream (star rating)
    """
    content: str
    done: bool = False
    user: str = None
    id: int = None
    star: int = 1
