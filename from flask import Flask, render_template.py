import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


# ---------------- DATABASE ----------------

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient TEXT,
    doctor TEXT,
    date TEXT
)
""")

conn.commit()


# ---------------- MAIN APP ----------------

class HospitalApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("800x500")

        title = tk.Label(
            root,
            text="Hospital Management System",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        # Buttons

        tk.Button(
            root,
            text="Add Patient",
            width=25,
            command=self.patient_window
        ).pack(pady=5)

        tk.Button(
            root,
            text="Add Doctor",
            width=25,
            command=self.doctor_window
        ).pack(pady=5)

        tk.Button(
            root,
            text="Book Appointment",
            width=25,
            command=self.appointment_window
        ).pack(pady=5)

        tk.Button(
            root,
            text="View Patients",
            width=25,
            command=self.view_patients
        ).pack(pady=5)

        tk.Button(
            root,
            text="View Doctors",
            width=25,
            command=self.view_doctors
        ).pack(pady=5)

        tk.Button(
            root,
            text="View Appointments",
            width=25,
            command=self.view_appointments
        ).pack(pady=5)


    # ---------------- PATIENT ----------------

    def patient_window(self):

        win = tk.Toplevel(self.root)
        win.title("Add Patient")

        tk.Label(win,text="Name").pack()
        name = tk.Entry(win)
        name.pack()

        tk.Label(win,text="Age").pack()
        age = tk.Entry(win)
        age.pack()

        tk.Label(win,text="Gender").pack()
        gender = tk.Entry(win)
        gender.pack()


        def save():

            cursor.execute(
                "INSERT INTO patients(name,age,gender) VALUES(?,?,?)",
                (
                    name.get(),
                    age.get(),
                    gender.get()
                )
            )

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Patient Added"
            )

            win.destroy()


        tk.Button(
            win,
            text="Save",
            command=save
        ).pack(pady=10)



    # ---------------- DOCTOR ----------------


    def doctor_window(self):

        win=tk.Toplevel(self.root)
        win.title("Add Doctor")


        tk.Label(win,text="Doctor Name").pack()
        name=tk.Entry(win)
        name.pack()


        tk.Label(win,text="Specialization").pack()
        spec=tk.Entry(win)
        spec.pack()


        def save():

            cursor.execute(
                "INSERT INTO doctors(name,specialization) VALUES(?,?)",
                (
                    name.get(),
                    spec.get()
                )
            )

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Doctor Added"
            )

            win.destroy()


        tk.Button(
            win,
            text="Save",
            command=save
        ).pack()



    # ---------------- APPOINTMENT ----------------


    def appointment_window(self):

        win=tk.Toplevel(self.root)
        win.title("Appointment")


        tk.Label(win,text="Patient Name").pack()
        patient=tk.Entry(win)
        patient.pack()


        tk.Label(win,text="Doctor Name").pack()
        doctor=tk.Entry(win)
        doctor.pack()


        tk.Label(win,text="Date").pack()
        date=tk.Entry(win)
        date.pack()


        def save():

            cursor.execute(
                """
                INSERT INTO appointments(patient,doctor,date)
                VALUES(?,?,?)
                """,
                (
                    patient.get(),
                    doctor.get(),
                    date.get()
                )
            )

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Appointment Booked"
            )

            win.destroy()



        tk.Button(
            win,
            text="Book",
            command=save
        ).pack()



    # ---------------- DISPLAY ----------------


    def display(self,title,data):

        win=tk.Toplevel(self.root)
        win.title(title)

        table=ttk.Treeview(win)

        table.pack(fill="both",expand=True)


        for row in data:
            table.insert(
                "",
                tk.END,
                values=row
            )


    def view_patients(self):

        cursor.execute(
            "SELECT * FROM patients"
        )

        self.display(
            "Patients",
            cursor.fetchall()
        )


    def view_doctors(self):

        cursor.execute(
            "SELECT * FROM doctors"
        )

        self.display(
            "Doctors",
            cursor.fetchall()
        )


    def view_appointments(self):

        cursor.execute(
            "SELECT * FROM appointments"
        )

        self.display(
            "Appointments",
            cursor.fetchall()
        )



# ---------------- RUN ----------------

root=tk.Tk()

app=HospitalApp(root)

root.mainloop()