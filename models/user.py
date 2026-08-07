import sqlite3
import hashlib


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def login(self):

        connection = sqlite3.connect("hospital.db")
        cursor = connection.cursor()

        hashed_password = hashlib.sha256(
            self.password.encode()
        ).hexdigest()

        cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password = ?
        """, (
            self.username,
            hashed_password
        ))

        user = cursor.fetchone()

        connection.close()

        return user