from models.appointment import Appointment
import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

print("=== Book Appointment ===")

patient_id = input("Enter Patient ID: ")

cursor.execute(
    "SELECT first_name, last_name FROM patients WHERE id = ?",
    (patient_id,)
)

patient = cursor.fetchone()

if patient is None:
    print("Patient not found.")
    connection.close()
    exit()

print(f"Patient: {patient[0]} {patient[1]}")

doctor_id = input("Enter Doctor ID: ")

cursor.execute(
    "SELECT first_name, last_name FROM doctors WHERE id = ?",
    (doctor_id,)
)

doctor = cursor.fetchone()

if doctor is None:
    print("Doctor not found.")
    connection.close()
    exit()

print(f"Doctor: Dr. {doctor[0]} {doctor[1]}")

appointment_date = input("Appointment Date (YYYY-MM-DD): ")
appointment_time = input("Appointment Time (HH:MM): ")
reason = input("Reason for Visit: ")

connection.close()

appointment = Appointment(
    patient_id,
    doctor_id,
    appointment_date,
    appointment_time,
    reason
)

appointment.save()
