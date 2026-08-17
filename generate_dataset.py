import csv
import random
from datetime import datetime, timedelta

# -----------------------------
# DATA OPTIONS
# -----------------------------

first_names = [
    "John", "Mary", "Peter", "Grace", "David",
    "Esther", "James", "Ruth", "Michael", "Brenda",
    "Daniel", "Faith", "Joseph", "Patricia", "Brian",
    "Alice", "Andrew", "Joyce", "Samuel", "Linda",
    "Robert", "Martha", "William", "Agnes", "Charles",
    "Chanda", "Gift", "Blessing", "Mercy", "Collins"
]

last_names = [
    "Banda", "Phiri", "Mulenga", "Mwila", "Tembo",
    "Zulu", "Mwanza", "Chanda", "Mumba", "Ngoma",
    "Lungu", "Sakala", "Kabwe", "Musonda", "Daka",
    "Bwalya", "Kapembwa", "Chilufya", "Siame", "Nkole"
]

genders = ["Male", "Female"]

diagnoses = [
    "Malaria",
    "Pneumonia",
    "Bronchitis",
    "Hypertension",
    "Diabetes",
    "Flu",
    "Asthma",
    "Typhoid",
    "Migraine",
    "Gastritis",
    "Heartburn",
    "Back Pain",
    "Arthritis",
    "Anemia",
    "Skin Infection",
    "Urinary Tract Infection",
    "Common Cold",
    "Food Poisoning",
    "Tuberculosis",
    "Allergic Reaction"
]

towns = [
    "Kitwe",
    "Ndola",
    "Chingola",
    "Mufulira",
    "Luanshya",
    "Kalulushi",
    "Kabwe",
    "Lusaka"
]

# -----------------------------
# GENERATE 550 PATIENTS
# -----------------------------

patients = []

start_date = datetime(2024, 1, 1)

for patient_id in range(1, 551):

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    age = random.randint(1, 85)
    gender = random.choice(genders)

    phone = f"097{random.randint(1000000, 9999999)}"

    address = random.choice(towns)

    diagnosis = random.choice(diagnoses)

    # Generate a realistic registration date
    registration_date = start_date + timedelta(
        days=random.randint(0, 900)
    )

    patients.append([
        patient_id,
        first_name,
        last_name,
        age,
        gender,
        phone,
        address,
        diagnosis,
        registration_date.strftime("%Y-%m-%d")
    ])

# -----------------------------
# SAVE TO CSV
# -----------------------------

with open("patients.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "patient_id",
        "first_name",
        "last_name",
        "age",
        "gender",
        "phone",
        "address",
        "diagnosis",
        "registration_date"
    ])

    writer.writerows(patients)

print("=" * 45)
print("       HOSPITAL DATASET EXPORT")
print("=" * 45)
print("patients.csv created successfully")
print("Records:", len(patients))
print("=" * 45)