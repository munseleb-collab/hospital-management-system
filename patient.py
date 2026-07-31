import sqlite3

def add_patient():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Patient Registration ===")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Please enter a valid age.")

    gender = input("Gender: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    diagnosis = input("Diagnosis: ")

    cursor.execute("""
    INSERT INTO patients
    (first_name, last_name, age, gender, phone, address, diagnosis)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (first_name, last_name, age, gender, phone, address, diagnosis))

    connection.commit()
    connection.close()

    print("\nPatient registered successfully!")
