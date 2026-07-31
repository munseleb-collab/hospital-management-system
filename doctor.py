import sqlite3

def add_doctor():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Doctor Registration ===")

    first_name = input("Doctor First Name: ")
    last_name = input("Doctor Last Name: ")
    specialization = input("Specialization: ")
    phone = input("Phone Number: ")

    cursor.execute("""
    INSERT INTO doctors
    (first_name, last_name, specialization, phone)
    VALUES (?, ?, ?, ?)
    """, (first_name, last_name, specialization, phone))

    connection.commit()
    connection.close()

    print("\nDoctor registered successfully!")
