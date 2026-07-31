import sqlite3
import os

print("Current folder:", os.getcwd())

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

connection.close()