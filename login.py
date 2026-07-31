import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n===== Hospital Login =====")

    username = input("Username: ")
    password = input("Password: ")

    hashed_password = hash_password(password)

    cursor.execute("""
    SELECT * FROM users
    WHERE username = ? AND password = ?
    """, (username, hashed_password))

    user = cursor.fetchone()

    connection.close()

    if user:
        print("\nLogin Successful!")
        print("Role:", user[3])
        return True
    else:
        print("\nInvalid username or password.")
        return False


if __name__ == "__main__":
    login()