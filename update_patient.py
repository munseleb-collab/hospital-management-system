import sqlite3

def update_patient():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    patient_id = input("Enter Patient ID to update: ")

    cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
    else:
        print("\nLeave a field blank to keep the current value.")

        first_name = input(f"First Name ({patient[1]}): ") or patient[1]
        last_name = input(f"Last Name ({patient[2]}): ") or patient[2]

        age_input = input(f"Age ({patient[3]}): ")
        age = int(age_input) if age_input else patient[3]

        gender = input(f"Gender ({patient[4]}): ") or patient[4]
        phone = input(f"Phone ({patient[5]}): ") or patient[5]
        address = input(f"Address ({patient[6]}): ") or patient[6]
        diagnosis = input(f"Diagnosis ({patient[7]}): ") or patient[7]

        cursor.execute("""
            UPDATE patients
            SET first_name = ?, last_name = ?, age = ?, gender = ?,
                phone = ?, address = ?, diagnosis = ?
            WHERE id = ?
        """, (first_name, last_name, age, gender, phone, address, diagnosis, patient_id))

        connection.commit()
        print("Patient updated successfully!")

    connection.close()

if __name__ == "__main__":
    update_patient()