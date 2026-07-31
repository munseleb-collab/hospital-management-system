import sqlite3

def delete_patient():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    patient_id = input("Enter Patient ID to delete: ")

    cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
    else:
        confirm = input(f"Are you sure you want to delete {patient[1]} {patient[2]}? (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
            connection.commit()
            print("Patient deleted successfully!")
        else:
            print("Deletion cancelled.")

    connection.close()

if __name__ == "__main__":
    delete_patient()