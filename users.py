import sqlite3
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

username = input("Enter username: ")
password = input("Enter password: ")
role = input("Enter role: ")

hashed_password = hash_password(password)

cursor.execute(
    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
    (username, hashed_password, role)
)

connection.commit()
connection.close()

print("User registered successfully!")