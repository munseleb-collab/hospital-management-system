import sqlite3

def register_user():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role: ")

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (username, password, role)
    )

    connection.commit()
    connection.close()

    print("User registered successfully!")


register_user()