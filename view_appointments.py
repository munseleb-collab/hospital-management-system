import sqlite3

def view_appointments():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Appointment Records ===")

    cursor.execute("""
    SELECT
        appointments.id,
        patients.first_name || ' ' || patients.last_name AS patient_name,
        doctors.first_name || ' ' || doctors.last_name AS doctor_name,
        appointments.appointment_date,
        appointments.appointment_time,
        appointments.reason
    FROM appointments
    INNER JOIN patients
        ON appointments.patient_id = patients.id
    INNER JOIN doctors
        ON appointments.doctor_id = doctors.id
    """)

    appointments = cursor.fetchall()

    if len(appointments) == 0:
        print("No appointments found.")
    else:
        for appointment in appointments:
            print("\nAppointment ID:", appointment[0])
            print("Patient:", appointment[1])
            print("Doctor:", appointment[2])
            print("Date:", appointment[3])
            print("Time:", appointment[4])
            print("Reason:", appointment[5])

    connection.close()

if __name__ == "__main__":
    view_appointments()