from models.person import Person
import sqlite3


class Doctor(Person):

    def __init__(self, first_name, last_name, specialization, phone):
        super().__init__(first_name, last_name)

        self.specialization = specialization
        self.phone = phone


    def save(self):

        connection = sqlite3.connect("hospital.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO doctors
        (first_name, last_name, specialization, phone)
        VALUES (?, ?, ?, ?)
        """, (
            self.first_name,
            self.last_name,
            self.specialization,
            self.phone
        ))

        connection.commit()
        connection.close()

        print("Doctor registered successfully!")