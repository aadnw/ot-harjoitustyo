"""This module includes the Dream class that takes care of storing all dream-related information"""


class Dream:
    """Class taking care of describing dreams"""

    def __init__(self, content, done=False, user=None, dream_id=None):
        self.content = content
        self.done = done
        self.user = user
        self.id = dream_id
