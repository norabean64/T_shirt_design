import hashlib

class SecurityAgent:
    def __init__(self):
        self.users = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, username, password):
        self.users[username] = self.hash_password(password)

    def authenticate_user(self, username, password):
        hashed_password = self.hash_password(password)
        stored_password = self.users.get(username)
        return stored_password == hashed_password
