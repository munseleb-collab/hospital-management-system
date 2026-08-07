import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(doctors)")

columns = cursor.fetchall()

for column in columns:
    print(column)

connection.close()