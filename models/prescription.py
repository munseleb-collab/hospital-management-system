import sqlite3


class Prescription:

    def __init__(self, patient_id, doctor_id, medicine, dosage, instructions):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medicine = medicine
        self.dosage = dosage
        self.instructions = instructions

    def save(self):

        connection = sqlite3.connect("hospital.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO prescriptions
        (patient_id, doctor_id, medicine, dosage, instructions)
        VALUES (?, ?, ?, ?, ?)
        """, (
            self.patient_id,
            self.doctor_id,
            self.medicine,
            self.dosage,
            self.instructions
        ))

        connection.commit()
        connection.close()

        print("Prescription added successfully!")