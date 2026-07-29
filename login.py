import sqlite3
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

hashed_password = hash_password(password)

cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, hashed_password)
)

user = cursor.fetchone()

if user:
    print("Login successful!")
    print("Welcome:", user[1])
    print("Role:", user[3])
else:
    print("Invalid username or password")

connection.close()