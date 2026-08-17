import sqlite3
import pandas as pd

# Connect to hospital database
connection = sqlite3.connect("hospital.db")

# Tables to export
tables = [
    "patients",
    "doctors",
    "appointments",
    "prescriptions",
    "bills"
]

print("========================================")
print("       HOSPITAL DATASET EXPORT")
print("========================================")

for table in tables:

    # Read table from SQLite
    data = pd.read_sql_query(
        f"SELECT * FROM {table}",
        connection
    )

    # Export to CSV
    filename = f"{table}.csv"
    data.to_csv(filename, index=False)

    print(f"{table}.csv created successfully")
    print(f"Records: {len(data)}")

connection.close()

print("========================================")
print("Dataset export completed!")
print("========================================")