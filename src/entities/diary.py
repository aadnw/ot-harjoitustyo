"""This module includes the Diary class that takes care of storing all diary notes"""


class Diary:
    """Class taking care of describing diary notes"""

    def __init__(self, content, dream_id=None):
        self.content = content
        self.dream_id = dream_id
