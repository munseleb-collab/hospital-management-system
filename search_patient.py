import sqlite3

def search_patient():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Search Patient ===")
    print("1. Search by Patient ID")
    print("2. Search by First Name")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")

        cursor.execute(
            "SELECT * FROM patients WHERE id = ?",
            (patient_id,)
        )

    elif choice == "2":
        first_name = input("Enter First Name: ")

        cursor.execute(
            "SELECT * FROM patients WHERE first_name LIKE ?",
            ('%' + first_name + '%',)
        )

    else:
        print("Invalid choice.")
        connection.close()
        return

    patients = cursor.fetchall()

    if patients:
        print("\nPatient Found:")

        for patient in patients:
            print("\nPatient ID:", patient[0])
            print("First Name:", patient[1])
            print("Last Name:", patient[2])
            print("Age:", patient[3])
            print("Gender:", patient[4])
            print("Phone:", patient[5])
            print("Address:", patient[6])
            print("Diagnosis:", patient[7])

    else:
        print("No patient found.")

    connection.close()


if __name__ == "__main__":
    search_patient()