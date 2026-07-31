import sqlite3

def view_prescriptions():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Prescription Records ===")

    cursor.execute("""
    SELECT
        prescriptions.id,
        patients.first_name || ' ' || patients.last_name AS patient_name,
        doctors.first_name || ' ' || doctors.last_name AS doctor_name,
        prescriptions.medicine,
        prescriptions.dosage,
        prescriptions.instructions
    FROM prescriptions
    INNER JOIN patients
        ON prescriptions.patient_id = patients.id
    INNER JOIN doctors
        ON prescriptions.doctor_id = doctors.id
    """)

    prescriptions = cursor.fetchall()

    if len(prescriptions) == 0:
        print("No prescriptions found.")
    else:
        for prescription in prescriptions:
            print("\nPrescription ID:", prescription[0])
            print("Patient:", prescription[1])
            print("Doctor:", prescription[2])
            print("Medicine:", prescription[3])
            print("Dosage:", prescription[4])
            print("Instructions:", prescription[5])

    connection.close()


if __name__ == "__main__":
    view_prescriptions()