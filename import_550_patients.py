import sqlite3
import csv

DB_NAME = "hospital.db"
CSV_FILE = "patients.csv"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# Clear existing patient records
cursor.execute("DELETE FROM patients")

# Reset the patient ID counter
cursor.execute("DELETE FROM sqlite_sequence WHERE name='patients'")

# Read the 550 patients from CSV
with open(CSV_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    patients = []

    for row in reader:
        patients.append((
            row["first_name"],
            row["last_name"],
            int(row["age"]),
            row["gender"],
            row["phone"],
            row["address"],
            row["diagnosis"]
        ))

# Insert patients
cursor.executemany("""
    INSERT INTO patients
    (first_name, last_name, age, gender, phone, address, diagnosis)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", patients)

connection.commit()

# Verify the number of records
cursor.execute("SELECT COUNT(*) FROM patients")
count = cursor.fetchone()[0]

connection.close()

print("=" * 45)
print("       PATIENT DATA IMPORT")
print("=" * 45)
print("Patients imported:", count)
print("=" * 45)