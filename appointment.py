import sqlite3

def add_appointment():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Book Appointment ===")

    # Check Patient
    patient_id = input("Enter Patient ID: ")
    cursor.execute("SELECT first_name, last_name FROM patients WHERE id = ?", (patient_id,))
    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
        connection.close()
        return

    print(f"Patient: {patient[0]} {patient[1]}")

    # Check Doctor
    doctor_id = input("Enter Doctor ID: ")
    cursor.execute("SELECT first_name, last_name FROM doctors WHERE id = ?", (doctor_id,))
    doctor = cursor.fetchone()

    if doctor is None:
        print("Doctor not found.")
        connection.close()
        return

    print(f"Doctor: Dr. {doctor[0]} {doctor[1]}")

    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM): ")
    reason = input("Reason for Visit: ")

    cursor.execute("""
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date, appointment_time, reason)
        VALUES (?, ?, ?, ?, ?)
    """, (patient_id, doctor_id, appointment_date, appointment_time, reason))

    connection.commit()
    connection.close()

    print("\nAppointment booked successfully!")

if __name__ == "__main__":
    add_appointment()