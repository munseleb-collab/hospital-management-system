import sqlite3


class Bill:

    def __init__(self, patient_id, amount, payment_status):
        self.patient_id = patient_id
        self.amount = amount
        self.payment_status = payment_status


    def save(self):

        connection = sqlite3.connect("hospital.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO bills
        (patient_id, amount, payment_status)
        VALUES (?, ?, ?)
        """, (
            self.patient_id,
            self.amount,
            self.payment_status
        ))

        connection.commit()
        connection.close()

        print("Bill generated successfully!")