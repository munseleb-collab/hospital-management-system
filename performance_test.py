import sqlite3
import time


connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()


# ==================================
# TEST 1: DATABASE CONNECTION SPEED
# ==================================

start_time = time.time()

connection.execute("SELECT * FROM patients")

end_time = time.time()

print("================================")
print(" SOFTWARE PERFORMANCE TEST")
print("================================")

print(
    "Database query time:",
    round(end_time - start_time, 6),
    "seconds"
)


# ==================================
# TEST 2: PATIENT SEARCH SPEED
# ==================================

patient_name = "Anita"

start_time = time.time()

cursor.execute(
    """
    SELECT *
    FROM patients
    WHERE first_name LIKE ?
    """,
    (f"%{patient_name}%",)
)

result = cursor.fetchall()

end_time = time.time()


print(
    "Patient search time:",
    round(end_time - start_time, 6),
    "seconds"
)

print(
    "Patients found:",
    len(result)
)


# ==================================
# TEST 3: COUNT RECORDS
# ==================================

start_time = time.time()

cursor.execute(
    "SELECT COUNT(*) FROM patients"
)

total = cursor.fetchone()[0]

end_time = time.time()


print(
    "Counting patients time:",
    round(end_time - start_time, 6),
    "seconds"
)

print(
    "Total patients:",
    total
)


connection.close()

print("================================")
print("Performance test completed")
print("================================")
