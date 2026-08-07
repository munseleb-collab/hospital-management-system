from models.person import Person

import sqlite3


class Patient(Person):

    def __init__(self, first_name, last_name, age, gender, phone, address, diagnosis):

     super().__init__(first_name, last_name)

     self.age = age
     self.gender = gender
     self.phone = phone
     self.address = address
     self.diagnosis = diagnosis


    def save(self):

        connection = sqlite3.connect("hospital.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO patients
        (first_name, last_name, age, gender, phone, address, diagnosis)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            self.first_name,
            self.last_name,
            self.age,
            self.gender,
            self.phone,
            self.address,
            self.diagnosis
        ))

        connection.commit()
        connection.close()

        print("Patient registered successfully!")