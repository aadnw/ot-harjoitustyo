class Dream:
    """Haaveista ja unelmista vastaava luokka"""

    def __init__(self, content, done=False, user=None, dream_id=None):
        self.content = content
        self.done = done
        self.user = user
        self.id = dream_id
