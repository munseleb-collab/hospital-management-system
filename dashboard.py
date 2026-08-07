import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connect to database
connection = sqlite3.connect("hospital.db")


# ==============================
# GET HOSPITAL DATA
# ==============================

patients = pd.read_sql_query(
    "SELECT * FROM patients",
    connection
)

doctors = pd.read_sql_query(
    "SELECT * FROM doctors",
    connection
)

appointments = pd.read_sql_query(
    "SELECT * FROM appointments",
    connection
)

prescriptions = pd.read_sql_query(
    "SELECT * FROM prescriptions",
    connection
)

bills = pd.read_sql_query(
    "SELECT * FROM bills",
    connection
)


# ==============================
# CALCULATE STATISTICS
# ==============================

total_patients = len(patients)
total_doctors = len(doctors)
total_appointments = len(appointments)
total_prescriptions = len(prescriptions)

if not bills.empty:
    total_revenue = bills["amount"].sum()
else:
    total_revenue = 0


# ==============================
# DISPLAY DASHBOARD
# ==============================

print("\n==============================================")
print("          HOSPITAL ANALYTICS DASHBOARD")
print("==============================================")

print(f"Total Patients       : {total_patients}")
print(f"Total Doctors        : {total_doctors}")
print(f"Total Appointments   : {total_appointments}")
print(f"Total Prescriptions  : {total_prescriptions}")
print(f"Total Revenue        : K{total_revenue:.2f}")

print("==============================================")


# ==============================
# PATIENT ANALYSIS
# ==============================

if not patients.empty:

    # Only count valid genders
    valid_gender_data = patients[
        patients["gender"].isin(["Male", "Female"])
    ]

    gender_count = valid_gender_data["gender"].value_counts()

    print("\nPatients by Gender:")
    print(gender_count)

    diagnosis_count = patients["diagnosis"].value_counts()

    print("\nTop Diagnoses:")
    print(diagnosis_count.head(5))


# ==============================
# DOCTOR ANALYSIS
# ==============================

if not doctors.empty:

    specialization_count = doctors["specialization"].value_counts()

    print("\nDoctors by Specialization:")
    print(specialization_count)


# ==============================
# BILLING ANALYSIS
# ==============================

if not bills.empty:

    # Standardize payment status
    bills["payment_status"] = (
        bills["payment_status"]
        .str.strip()
        .str.capitalize()
    )

    payment_status = bills["payment_status"].value_counts()

    print("\nPayment Status:")
    print(payment_status)


connection.close()


# ==============================
# CHART 1
# PATIENTS BY GENDER
# ==============================

if not patients.empty:

    gender_count.plot(
        kind="bar",
        title="Patients by Gender"
    )

    plt.xlabel("Gender")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()


# ==============================
# CHART 2
# TOP 5 DIAGNOSES
# ==============================

if not patients.empty:

    diagnosis_count.head(5).plot(
        kind="bar",
        title="Top 5 Patient Diagnoses"
    )

    plt.xlabel("Diagnosis")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()


# ==============================
# CHART 3
# DOCTORS BY SPECIALIZATION
# ==============================

if not doctors.empty:

    specialization_count.plot(
        kind="bar",
        title="Doctors by Specialization"
    )

    plt.xlabel("Specialization")
    plt.ylabel("Number of Doctors")
    plt.tight_layout()
    plt.show()


# ==============================
# CHART 4
# PAYMENT STATUS
# ==============================

if not bills.empty:

    payment_status.plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Payment Status"
    )

    plt.ylabel("")
    plt.tight_layout()
    plt.show()


# ==============================
# CHART 5
# REVENUE
# ==============================

if not bills.empty:

    bills["amount"].plot(
        kind="bar",
        title="Hospital Bill Amounts"
    )

    plt.xlabel("Bill")
    plt.ylabel("Amount (K)")
    plt.tight_layout()
    plt.show()