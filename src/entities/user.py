class User:
    def __init__(self, username, password, user_id=None):
        """Käyttäjistä vastaava luokka"""
        self.username = username
        self.password = password
        self.id = user_id
