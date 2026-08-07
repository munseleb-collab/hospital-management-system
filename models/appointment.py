import sqlite3


class Appointment:

    def __init__(self, patient_id, doctor_id, appointment_date, appointment_time, reason):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason

    def save(self):

        connection = sqlite3.connect("hospital.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date, appointment_time, reason)
        VALUES (?, ?, ?, ?, ?)
        """, (
            self.patient_id,
            self.doctor_id,
            self.appointment_date,
            self.appointment_time,
            self.reason
        ))

        connection.commit()
        connection.close()

        print("Appointment booked successfully!")