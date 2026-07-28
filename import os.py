from sqlite3 import Cursor

from matplotlib.pylab import cond


class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def __str__(self):
        return (
            f"Patient: {self.patient.name} | "
            f"Doctor: {self.doctor.name} | "
            f"Date: {self.date}"
        )


class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")

        self.patients[pid] = Patient(pid, name, age, gender)
        print("Patient added successfully!")

    def add_doctor(self):
        did = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")

        self.doctors[did] = Doctor(did, name, specialization)
        print("Doctor added successfully!")

    def book_appointment(self):
        pid = input("Enter Patient ID: ")
        did = input("Enter Doctor ID: ")
        date = input("Enter Appointment Date (YYYY-MM-DD): ")

        if pid not in self.patients:
            print("Patient not found!")
            return

        if did not in self.doctors:
            print("Doctor not found!")
            return

        appointment = Appointment(
            self.patients[pid],
            self.doctors[did],
            date
        )

        self.appointments.append(appointment)
        print("Appointment booked successfully!")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
            return

        print("\nPatients")
        print("-" * 40)
        for patient in self.patients.values():
            print(patient)

    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return

        print("\nDoctors")
        print("-" * 40)
        for doctor in self.doctors.values():
            print(doctor)

    def view_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return

        print("\nAppointments")
        print("-" * 40)
        for appointment in self.appointments:
            print(appointment)


def main():
    hms = HospitalManagementSystem()

    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hms.add_patient()

        elif choice == "2":
            hms.add_doctor()

        elif choice == "3":
            hms.book_appointment()

        elif choice == "4":
            hms.view_patients()

        elif choice == "5":
            hms.view_doctors()

        elif choice == "6":
            hms.view_appointments()

        elif choice == "7":
            print("Thank you for using the Hospital Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
    class Cursor:
     def add_patient(name, age, gender, phone):
      Cursor.execute(
          "INSERT INTO patients(name, age, gender, phone) VALUES(?,?,?,?)",
        (name, age, gender, phone)
      ) 
    cond.commit()
      
    Cursor.execute("SELECT * FROM patients")
for row in Cursor.fetchall():
    print(row)
    def search_patient(name):
      Cursor.execute(
        "SELECT * FROM patients WHERE name LIKE ?",
        ("%" + name + "%",),
    )

    result = Cursor.fetchall()

    if result:
        for patient in result:
            print(patient)
    else:
        print("Patient not found.")
        def update_patient(patient_id, phone):
         Cursor.execute(
        "UPDATE patients SET phone=? WHERE id=?",
        (phone, patient_id),
    )
    cond.commit()
    
    def delete_patient(patient_id):
     Cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,),
    )
    cond.commit()
    class Bill:
     def __init__(self, patient, consultation, medicine):
        self.patient = patient
        self.consultation = consultation
        self.medicine = medicine

    @property
    def total(self):
        return self.consultation + self.medicine

    def print_bill(self):
        print("\n----- BILL -----")
        print("Patient:", self.patient)
        print("Consultation:", self.consultation)
        print("Medicine:", self.medicine)
        print("Total:", self.total)
        
        bill = Bill("John", 300, 150)
Bill.print_bill()

users = {
    "admin": "1234",
    "doctor": "abcd"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login successful.")
else:
    print("Invalid username or password.")
    
    import uuid

appointment_id = str(uuid.uuid4())[:8]

print("Appointment ID:", appointment_id)

Cursor.execute("""
CREATE TABLE IF NOT EXISTS bills(
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient TEXT,
    amount REAL
)
""")

Cursor.execute(
    "INSERT INTO bills(patient, amount) VALUES(?, ?)",
    ("John", 450)
)

cond.commit()

Cursor.execute("SELECT COUNT(*) FROM patients")
print("Total Patients:", Cursor.fetchone()[0])

Cursor.execute("SELECT COUNT(*) FROM doctors")
print("Total Doctors:", Cursor.fetchone()[0])

Cursor.execute("SELECT COUNT(*) FROM appointments")
print("Total Appointments:", Cursor.fetchone()[0])

from tkinter import *

root = Tk()
root.title("Hospital Management System")
root.geometry("600x400")

Label(root, text="Hospital Management System", font=("Arial", 18)).pack(pady=20)

Button(root, text="Add Patient").pack(pady=5);
Button(root, text="View Patients").pack(pady=5);
Button(root, text="Appointments").pack(pady=5);

root.mainloop()