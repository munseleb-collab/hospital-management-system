import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_patient_report():

    patient_id = input("Enter Patient ID: ")

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    # Get patient details
    cursor.execute(
        "SELECT * FROM patients WHERE id=?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    if not patient:
        print("Patient not found.")
        connection.close()
        return

    file_name = f"patient_{patient_id}_report.pdf"

    pdf = canvas.Canvas(file_name, pagesize=letter)

    y = 750

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(150, y, "PATIENT MEDICAL REPORT")

    y -= 40

    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, y, f"Patient ID: {patient[0]}")
    y -= 20
    pdf.drawString(50, y, f"Name: {patient[1]} {patient[2]}")
    y -= 20
    pdf.drawString(50, y, f"Age: {patient[3]}")
    y -= 20
    pdf.drawString(50, y, f"Gender: {patient[4]}")
    y -= 20
    pdf.drawString(50, y, f"Phone: {patient[5]}")
    y -= 20
    pdf.drawString(50, y, f"Diagnosis: {patient[7]}")

    y -= 40

    # Appointments
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Appointments")
    y -= 20

    pdf.setFont("Helvetica", 11)

    cursor.execute("""
    SELECT appointment_date, reason
    FROM appointments
    WHERE patient_id=?
    """, (patient_id,))

    appointments = cursor.fetchall()

    for appointment in appointments:
        pdf.drawString(
            60,
            y,
            f"{appointment[0]} - {appointment[1]}"
        )
        y -= 20

    y -= 20

    # Prescriptions
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Prescriptions")
    y -= 20

    pdf.setFont("Helvetica", 11)

    cursor.execute("""
    SELECT medicine, dosage, instructions
    FROM prescriptions
    WHERE patient_id=?
    """, (patient_id,))

    prescriptions = cursor.fetchall()

    for prescription in prescriptions:
        pdf.drawString(
            60,
            y,
            f"{prescription[0]} - {prescription[1]}"
        )
        y -= 20

    pdf.save()

    connection.close()

    print("Patient report generated successfully!")
    print(f"Saved as: {file_name}")
    