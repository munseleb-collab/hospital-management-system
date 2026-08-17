from models.prescription import Prescription


def add_prescription():

    print("=== Add Prescription ===")

    patient_id = input("Patient ID: ")
    doctor_id = input("Doctor ID: ")
    medicine = input("Medicine: ")
    dosage = input("Dosage: ")
    instructions = input("Instructions: ")

    prescription = Prescription(
        patient_id,
        doctor_id,
        medicine,
        dosage,
        instructions
    )

    prescription.save()


