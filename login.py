import sqlite3


def login_user():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("=== Hospital Management System Login ===")

    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        print("Login successful!")
        print("Welcome,", user[1])
        print("Role:", user[3])
    else:
        print("Invalid username or password")

    connection.close()


login_user()