import sqlite3

def view_patients():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Patient Records ===")

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    if len(patients) == 0:
        print("No patients found.")
    else:
        for patient in patients:
            print("\nPatient ID:", patient[0])
            print("First Name:", patient[1])
            print("Last Name:", patient[2])
            print("Age:", patient[3])
            print("Gender:", patient[4])
            print("Phone:", patient[5])
            print("Address:", patient[6])
            print("Diagnosis:", patient[7])

    connection.close()

