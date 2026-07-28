import tkinter as ctk
from tkinter import messagebox, ttk
import sqlite3


# ================= DATABASE =================

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()


def create_database():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age TEXT,
        gender TEXT,
        phone TEXT
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

    cursor.execute("""
    INSERT OR IGNORE INTO users(username,password,role)
    VALUES('admin','1234','Administrator')
    """)

    conn.commit()


# ================= LOGIN =================


class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("Hospital Login")
        self.root.geometry("400x300")


        tk.Label(
            root,
            text="Hospital Management System",
            font=("Arial",18,"bold")
        ).pack(pady=20)


        tk.Label(root,text="Username").pack()

        self.username = tk.Entry(root)
        self.username.pack()


        tk.Label(root,text="Password").pack()

        self.password = tk.Entry(
            root,
            show="*"
        )

        self.password.pack()


        tk.Button(
            root,
            text="Login",
            command=self.check_login
        ).pack(pady=20)



    def check_login(self):

        cursor.execute(
            """
            SELECT role FROM users
            WHERE username=? AND password=?
            """,
            (
                self.username.get(),
                self.password.get()
            )
        )


        result = cursor.fetchone()


        if result:

            self.root.destroy()

            dashboard = tk.Tk()

            Dashboard(
                dashboard,
                result[0]
            )

            dashboard.mainloop()

        else:

            messagebox.showerror(
                "Login Failed",
                "Wrong username or password"
            )



# ================= DASHBOARD =================


class Dashboard:


    def __init__(self,root,role):

        self.root=root

        self.root.title(
            "Hospital Dashboard"
        )

        self.root.geometry(
            "700x500"
        )


        tk.Label(
            root,
            text=f"Welcome {role}",
            font=("Arial",20,"bold")
        ).pack(pady=20)


        buttons = [

            ("Add Patient",self.add_patient),

            ("Add Doctor",self.add_doctor),

            ("Book Appointment",self.add_appointment),

            ("View Patients",self.view_patients),

            ("View Doctors",self.view_doctors),

            ("View Appointments",self.view_appointments)

        ]


        for text,command in buttons:

            tk.Button(
                root,
                text=text,
                width=25,
                command=command
            ).pack(pady=5)



# ================= PATIENT =================


    def add_patient(self):

        win=tk.Toplevel(self.root)

        win.title("Add Patient")


        entries=[]

        for label in [
            "Name",
            "Age",
            "Gender",
            "Phone"
        ]:

            tk.Label(
                win,
                text=label
            ).pack()

            e=tk.Entry(win)

            e.pack()

            entries.append(e)



        def save():

            cursor.execute(
                """
                INSERT INTO patients
                (name,age,gender,phone)
                VALUES(?,?,?,?)
                """,
                (
                    entries[0].get(),
                    entries[1].get(),
                    entries[2].get(),
                    entries[3].get()
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



# ================= DOCTOR =================


    def add_doctor(self):

        win=tk.Toplevel(self.root)

        win.title("Add Doctor")


        name=tk.Entry(win)
        spec=tk.Entry(win)


        tk.Label(
            win,
            text="Doctor Name"
        ).pack()

        name.pack()


        tk.Label(
            win,
            text="Specialization"
        ).pack()

        spec.pack()


        def save():

            cursor.execute(
                """
                INSERT INTO doctors
                (name,specialization)
                VALUES(?,?)
                """,
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



# ================= APPOINTMENT =================


    def add_appointment(self):

        win=tk.Toplevel(self.root)

        win.title("Appointment")


        patient=tk.Entry(win)
        doctor=tk.Entry(win)
        date=tk.Entry(win)


        for label,entry in [
            ("Patient",patient),
            ("Doctor",doctor),
            ("Date",date)
        ]:

            tk.Label(
                win,
                text=label
            ).pack()

            entry.pack()



        def save():

            cursor.execute(
                """
                INSERT INTO appointments
                (patient,doctor,date)
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
                "Appointment Saved"
            )

            win.destroy()



        tk.Button(
            win,
            text="Save",
            command=save
        ).pack()



# ================= VIEW DATA =================


    def show_table(self,title,query):

        win=tk.Toplevel(self.root)

        win.title(title)


        table=ttk.Treeview(win)

        table.pack(
            fill="both",
            expand=True
        )


        cursor.execute(query)


        for row in cursor.fetchall():

            table.insert(
                "",
                tk.END,
                values=row
            )



    def view_patients(self):

        self.show_table(
            "Patients",
            "SELECT * FROM patients"
        )


    def view_doctors(self):

        self.show_table(
            "Doctors",
            "SELECT * FROM doctors"
        )


    def view_appointments(self):

        self.show_table(
            "Appointments",
            "SELECT * FROM appointments"
        )



# ================= START =================


create_database()


root=tk.Tk()

Login(root)

root.mainloop()