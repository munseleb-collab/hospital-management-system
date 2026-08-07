from models.prescription import Prescription
import sqlite3

connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

print("=== Add Prescription ===")

patient_id = input("Patient ID: ")
doctor_id = input("Doctor ID: ")
medicine = input("Medicine: ")
dosage = input("Dosage: ")
instructions = input("Instructions: ")

connection.close()

prescription = Prescription(
    patient_id,
    doctor_id,
    medicine,
    dosage,
    instructions
)

prescription.save()
