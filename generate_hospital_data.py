import sqlite3
import random
from datetime import datetime, timedelta

DB_NAME = "hospital.db"

# -------------------------------------------------
# DATA OPTIONS
# -------------------------------------------------

first_names = [
    "John", "Mary", "Peter", "Grace", "David",
    "Esther", "James", "Ruth", "Michael", "Brenda",
    "Daniel", "Faith", "Joseph", "Patricia", "Brian",
    "Alice", "Andrew", "Joyce", "Samuel", "Linda"
]

last_names = [
    "Banda", "Phiri", "Mulenga", "Mwila", "Tembo",
    "Zulu", "Mwanza", "Chanda", "Mumba", "Ngoma",
    "Lungu", "Sakala", "Kabwe", "Musonda", "Daka",
    "Bwalya", "Kapembwa", "Chilufya", "Siame", "Nkole"
]

specializations = [
    "General Medicine",
    "Pediatrics",
    "Cardiology",
    "Dermatology",
    "Gynecology",
    "Orthopedics",
    "Neurology",
    "Psychiatry",
    "Dentistry",
    "Ophthalmology",
    "Radiology",
    "Surgery",
    "Internal Medicine",
    "Urology",
    "ENT"
]

appointment_reasons = [
    "Routine Checkup",
    "Follow-up",
    "Malaria Symptoms",
    "Fever",
    "Cough",
    "Headache",
    "Stomach Pain",
    "Back Pain",
    "Blood Pressure Check",
    "Diabetes Check",
    "Skin Problem",
    "Medical Consultation",
    "General Examination"
]

services = [
    "Consultation",
    "Laboratory Test",
    "Blood Test",
    "X-Ray",
    "Ultrasound",
    "Medication",
    "Emergency Treatment",
    "Medical Examination",
    "Dental Treatment",
    "Follow-up Consultation"
]

medicines = [
    "Paracetamol",
    "Amoxicillin",
    "Ibuprofen",
    "Metformin",
    "Amlodipine",
    "Omeprazole",
    "Azithromycin",
    "Ciprofloxacin",
    "Cetirizine",
    "Diclofenac",
    "Artemether",
    "Loratadine",
    "ORS"
]

dosages = [
    "500mg",
    "250mg",
    "100mg",
    "10mg",
    "20mg",
    "5mg",
    "1 tablet",
    "2 tablets"
]

instructions = [
    "Take once daily after meals",
    "Take twice daily",
    "Take three times daily",
    "Take before meals",
    "Take after meals",
    "Take with plenty of water",
    "Use as directed by the doctor"
]

payment_statuses = [
    "Paid",
    "Pending",
    "Partially Paid"
]


# -------------------------------------------------
# CONNECT TO DATABASE
# -------------------------------------------------

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

print("=" * 50)
print("       HOSPITAL DATA GENERATOR")
print("=" * 50)


# -------------------------------------------------
# BACKUP EXISTING SUPPORTING DATA
# -------------------------------------------------

cursor.execute("DROP TABLE IF EXISTS doctors_backup")
cursor.execute("""
    CREATE TABLE doctors_backup AS
    SELECT * FROM doctors
""")

cursor.execute("DROP TABLE IF EXISTS appointments_backup")
cursor.execute("""
    CREATE TABLE appointments_backup AS
    SELECT * FROM appointments
""")

cursor.execute("DROP TABLE IF EXISTS bills_backup")
cursor.execute("""
    CREATE TABLE bills_backup AS
    SELECT * FROM bills
""")

cursor.execute("DROP TABLE IF EXISTS prescriptions_backup")
cursor.execute("""
    CREATE TABLE prescriptions_backup AS
    SELECT * FROM prescriptions
""")

print("Backup of supporting data created.")


# -------------------------------------------------
# CLEAR EXISTING SUPPORTING DATA
# -------------------------------------------------

cursor.execute("DELETE FROM appointments")
cursor.execute("DELETE FROM bills")
cursor.execute("DELETE FROM prescriptions")
cursor.execute("DELETE FROM doctors")

cursor.execute("DELETE FROM sqlite_sequence WHERE name='appointments'")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='bills'")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='prescriptions'")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='doctors'")


# -------------------------------------------------
# GENERATE 20 DOCTORS
# -------------------------------------------------

doctors = []

for i in range(20):
    first_name = first_names[i]
    last_name = last_names[i]

    specialization = random.choice(specializations)

    phone = f"096{random.randint(1000000, 9999999)}"

    doctors.append((
        first_name,
        last_name,
        specialization,
        phone
    ))

cursor.executemany("""
    INSERT INTO doctors
    (first_name, last_name, specialization, phone)
    VALUES (?, ?, ?, ?)
""", doctors)

print("Doctors created: 20")


# -------------------------------------------------
# GENERATE 550 APPOINTMENTS
# -------------------------------------------------

appointments = []

start_date = datetime(2026, 1, 1)

for i in range(550):

    patient_id = random.randint(1, 550)
    doctor_id = random.randint(1, 20)

    appointment_date = start_date + timedelta(
        days=random.randint(0, 365)
    )

    appointment_time = random.choice([
        "08:00",
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "14:00",
        "15:00",
        "16:00"
    ])

    reason = random.choice(appointment_reasons)

    appointments.append((
        patient_id,
        doctor_id,
        appointment_date.strftime("%Y-%m-%d"),
        appointment_time,
        reason
    ))

cursor.executemany("""
    INSERT INTO appointments
    (patient_id, doctor_id, appointment_date,
     appointment_time, reason)
    VALUES (?, ?, ?, ?, ?)
""", appointments)

print("Appointments created: 550")


# -------------------------------------------------
# GENERATE 550 BILLS
# -------------------------------------------------

bills = []

for i in range(550):

    patient_id = random.randint(1, 550)

    service = random.choice(services)

    amount = round(random.uniform(50, 2500), 2)

    payment_status = random.choice(payment_statuses)

    bills.append((
        patient_id,
        service,
        amount,
        payment_status
    ))

cursor.executemany("""
    INSERT INTO bills
    (patient_id, service, amount, payment_status)
    VALUES (?, ?, ?, ?)
""", bills)

print("Bills created: 550")


# -------------------------------------------------
# GENERATE 550 PRESCRIPTIONS
# -------------------------------------------------

prescriptions = []

for i in range(550):

    patient_id = random.randint(1, 550)
    doctor_id = random.randint(1, 20)

    medicine = random.choice(medicines)
    dosage = random.choice(dosages)
    instruction = random.choice(instructions)

    prescriptions.append((
        patient_id,
        doctor_id,
        medicine,
        dosage,
        instruction
    ))

cursor.executemany("""
    INSERT INTO prescriptions
    (patient_id, doctor_id, medicine,
     dosage, instructions)
    VALUES (?, ?, ?, ?, ?)
""", prescriptions)


print("Prescriptions created: 550")


# -------------------------------------------------
# SAVE EVERYTHING
# -------------------------------------------------

connection.commit()


# -------------------------------------------------
# VERIFY COUNTS
# -------------------------------------------------

print()
print("-" * 50)
print("DATABASE VERIFICATION")
print("-" * 50)

tables = [
    "patients",
    "doctors",
    "appointments",
    "bills",
    "prescriptions"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]

    print(f"{table.capitalize():20} : {count}")

print("-" * 50)

connection.close()

print("Hospital dataset generated successfully!")
print("=" * 50)