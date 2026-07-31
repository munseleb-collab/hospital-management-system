import sqlite3


def view_medical_history():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    patient_id = input("Enter Patient ID: ")

    # Patient Details
    cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    patient = cursor.fetchone()

    if not patient:
        print("Patient not found.")
        connection.close()
        return

    print("\n========== PATIENT DETAILS ==========")
    print(f"Patient ID : {patient[0]}")
    print(f"Name       : {patient[1]} {patient[2]}")
    print(f"Age        : {patient[3]}")
    print(f"Gender     : {patient[4]}")
    print(f"Phone      : {patient[5]}")
    print(f"Diagnosis  : {patient[7]}")

    # Appointments
    print("\n========== APPOINTMENTS ==========")

    cursor.execute("""
    SELECT 
        appointments.appointment_date,
        doctors.first_name || ' ' || doctors.last_name,
        appointments.reason
    FROM appointments
    JOIN doctors
    ON appointments.doctor_id = doctors.id
    WHERE appointments.patient_id=?
    """, (patient_id,))

    appointments = cursor.fetchall()

    if appointments:
        for appointment in appointments:
            print(f"Date: {appointment[0]}")
            print(f"Doctor: {appointment[1]}")
            print(f"Reason: {appointment[2]}")
            print("-" * 40)
    else:
        print("No appointments found.")

    # Prescriptions
    print("\n========== PRESCRIPTIONS ==========")

    cursor.execute(
        "SELECT medicine, dosage, instructions FROM prescriptions WHERE patient_id=?",
        (patient_id,)
    )

    prescriptions = cursor.fetchall()

    if prescriptions:
        for prescription in prescriptions:
            print(f"Medication : {prescription[0]}")
            print(f"Dosage     : {prescription[1]}")
            print(f"Instructions: {prescription[2]}")
            print("-" * 40)
    else:
        print("No prescriptions found.")

    # Bills
    print("\n========== BILLING ==========")

    cursor.execute(
        "SELECT amount, payment_status FROM bills WHERE patient_id=?",
        (patient_id,)
    )

    bills = cursor.fetchall()

    if bills:
        total = 0

        for bill in bills:
            print(f"Amount : K{bill[0]}")
            print(f"Status : {bill[1]}")
            total += bill[0]
            print("-" * 40)

        print(f"Total Amount Billed: K{total}")

    else:
        print("No billing records found.")

    connection.close()