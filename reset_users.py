import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM users")

connection.commit()
connection.close()

print("All users have been deleted.")