import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connect to database
connection = sqlite3.connect("hospital.db")


# ==============================
# PATIENT ANALYSIS
# ==============================

patients = pd.read_sql_query(
    "SELECT * FROM patients",
    connection
)

print("\n================================")
print("      PATIENT DATA ANALYSIS")
print("================================")

print("\nTotal Patients:", len(patients))


# Patients by gender
if not patients.empty:
    gender_count = patients["gender"].value_counts()

    print("\nPatients by Gender:")
    print(gender_count)


# Patients by diagnosis
if not patients.empty:
    diagnosis_count = patients["diagnosis"].value_counts()

    print("\nPatients by Diagnosis:")
    print(diagnosis_count)


# ==============================
# DOCTOR ANALYSIS
# ==============================

doctors = pd.read_sql_query(
    "SELECT * FROM doctors",
    connection
)

print("\n================================")
print("       DOCTOR DATA ANALYSIS")
print("================================")

print("\nTotal Doctors:", len(doctors))

if not doctors.empty:
    specialization_count = doctors["specialization"].value_counts()

    print("\nDoctors by Specialization:")
    print(specialization_count)


# ==============================
# BILLING ANALYSIS
# ==============================

bills = pd.read_sql_query(
    "SELECT * FROM bills",
    connection
)

print("\n================================")
print("       BILLING DATA ANALYSIS")
print("================================")

if not bills.empty:

    total_revenue = bills["amount"].sum()

    print("\nTotal Revenue:", total_revenue)

    payment_status = bills["payment_status"].value_counts()

    print("\nPayment Status:")
    print(payment_status)


connection.close()


# ==============================
# VISUALIZATION 1
# PATIENTS BY GENDER
# ==============================

if not patients.empty:

    gender_count = patients["gender"].value_counts()

    gender_count.plot(
        kind="bar",
        title="Patients by Gender"
    )

    plt.xlabel("Gender")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()


# ==============================
# VISUALIZATION 2
# PATIENTS BY DIAGNOSIS
# ==============================

if not patients.empty:

    diagnosis_count = patients["diagnosis"].value_counts()

    diagnosis_count.plot(
        kind="bar",
        title="Patients by Diagnosis"
    )

    plt.xlabel("Diagnosis")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()


# ==============================
# VISUALIZATION 3
# DOCTORS BY SPECIALIZATION
# ==============================

if not doctors.empty:

    specialization_count = doctors["specialization"].value_counts()

    specialization_count.plot(
        kind="bar",
        title="Doctors by Specialization"
    )

    plt.xlabel("Specialization")
    plt.ylabel("Number of Doctors")
    plt.tight_layout()
    plt.show()


# ==============================
# VISUALIZATION 4
# PAYMENT STATUS
# ==============================

if not bills.empty:

    payment_status = bills["payment_status"].value_counts()

    payment_status.plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Payment Status"
    )

    plt.ylabel("")
    plt.show()