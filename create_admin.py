import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

try:
    cursor.execute("""
    INSERT INTO users (username, password)
    VALUES (?, ?)
    """, ("admin", "admin123"))

    connection.commit()
    print("Admin account created successfully!")

except sqlite3.IntegrityError:
    print("Admin account already exists.")

connection.close()