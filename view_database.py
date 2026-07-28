import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

for user in cursor.fetchall():
    print(user)

connection.close()