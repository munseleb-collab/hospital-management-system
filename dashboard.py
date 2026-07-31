import sqlite3

def dashboard():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    # Total Patients
    cursor.execute("SELECT COUNT(*) FROM patients")
    total_patients = cursor.fetchone()[0]

    # Total Doctors
    cursor.execute("SELECT COUNT(*) FROM doctors")
    total_doctors = cursor.fetchone()[0]

    # Total Appointments
    cursor.execute("SELECT COUNT(*) FROM appointments")
    total_appointments = cursor.fetchone()[0]

    # Total Bills
    cursor.execute("SELECT COUNT(*) FROM bills")
    total_bills = cursor.fetchone()[0]

    # Total Prescriptions
    cursor.execute("SELECT COUNT(*) FROM prescriptions")
    total_prescriptions = cursor.fetchone()[0]

    connection.close()

    print("\n" + "=" * 45)
    print("      HOSPITAL MANAGEMENT DASHBOARD")
    print("=" * 45)
    print(f"Total Patients      : {total_patients}")
    print(f"Total Doctors       : {total_doctors}")
    print(f"Total Appointments  : {total_appointments}")
    print(f"Total Bills         : {total_bills}")
    print(f"Total Prescriptions : {total_prescriptions}")
    print("=" * 45)