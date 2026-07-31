import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print(users)

connection.close()