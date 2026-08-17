
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect("hospital.db")


# ============================================================
# LOAD DATA
# ============================================================

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

bills = pd.read_sql_query(
    "SELECT * FROM bills",
    connection
)

prescriptions = pd.read_sql_query(
    "SELECT * FROM prescriptions",
    connection
)


# ============================================================
# GENERAL DATASET SUMMARY
# ============================================================

print("\n" + "=" * 55)
print("          HOSPITAL DATASET ANALYSIS")
print("=" * 55)

print("\nDATASET SUMMARY")
print("-" * 55)

print("Total Patients       :", len(patients))
print("Total Doctors        :", len(doctors))
print("Total Appointments   :", len(appointments))
print("Total Bills          :", len(bills))
print("Total Prescriptions  :", len(prescriptions))


# ============================================================
# PATIENT ANALYSIS
# ============================================================

print("\n" + "=" * 55)
print("             PATIENT ANALYSIS")
print("=" * 55)

if not patients.empty:

    print("\nTotal Patients:", len(patients))

    # Gender
    gender_count = patients["gender"].value_counts()

    print("\nPatients by Gender:")
    print(gender_count)

    # Age statistics
    print("\nAge Statistics:")
    print("Average Age :", round(patients["age"].mean(), 2))
    print("Youngest    :", patients["age"].min())
    print("Oldest      :", patients["age"].max())

    # Age groups
    patients["age_group"] = pd.cut(
        patients["age"],
        bins=[0, 12, 18, 35, 50, 65, 100],
        labels=[
            "Children",
            "Teenagers",
            "Young Adults",
            "Adults",
            "Older Adults",
            "Seniors"
        ]
    )

    age_group_count = patients["age_group"].value_counts().sort_index()

    print("\nPatients by Age Group:")
    print(age_group_count)

    # Diagnosis
    diagnosis_count = patients["diagnosis"].value_counts()

    print("\nPatients by Diagnosis:")
    print(diagnosis_count)

    print("\nMost Common Diagnosis:")
    print(diagnosis_count.idxmax(),
          "(", diagnosis_count.max(), "patients )")


# ============================================================
# DOCTOR ANALYSIS
# ============================================================

print("\n" + "=" * 55)
print("              DOCTOR ANALYSIS")
print("=" * 55)

print("\nTotal Doctors:", len(doctors))

if not doctors.empty:

    specialization_count = doctors["specialization"].value_counts()

    print("\nDoctors by Specialization:")
    print(specialization_count)


# ============================================================
# APPOINTMENT ANALYSIS
# ============================================================

print("\n" + "=" * 55)
print("           APPOINTMENT ANALYSIS")
print("=" * 55)

print("\nTotal Appointments:", len(appointments))

if not appointments.empty:

    reason_count = appointments["reason"].value_counts()

    print("\nAppointments by Reason:")
    print(reason_count)

    # Appointments per doctor
    appointments_per_doctor = (
        appointments["doctor_id"]
        .value_counts()
        .sort_index()
    )

    print("\nAppointments per Doctor:")
    print(appointments_per_doctor)


# ============================================================
# BILLING ANALYSIS
# ============================================================

print("\n" + "=" * 55)
print("              BILLING ANALYSIS")
print("=" * 55)

if not bills.empty:

    total_revenue = bills["amount"].sum()
    average_bill = bills["amount"].mean()

    print("\nTotal Revenue: ZMW", round(total_revenue, 2))
    print("Average Bill : ZMW", round(average_bill, 2))

    payment_status = bills["payment_status"].value_counts()

    print("\nPayment Status:")
    print(payment_status)

    service_count = bills["service"].value_counts()

    print("\nBills by Service:")
    print(service_count)


# ============================================================
# PRESCRIPTION ANALYSIS
# ============================================================

print("\n" + "=" * 55)
print("          PRESCRIPTION ANALYSIS")
print("=" * 55)

print("\nTotal Prescriptions:", len(prescriptions))

if not prescriptions.empty:

    medicine_count = prescriptions["medicine"].value_counts()

    print("\nMost Prescribed Medicines:")
    print(medicine_count)

    print("\nMost Prescribed Medicine:")
    print(
        medicine_count.idxmax(),
        "(",
        medicine_count.max(),
        "prescriptions )"
    )

    prescriptions_per_doctor = (
        prescriptions["doctor_id"]
        .value_counts()
        .sort_index()
    )

    print("\nPrescriptions per Doctor:")
    print(prescriptions_per_doctor)


# ============================================================
# VISUALIZATION 1
# PATIENTS BY GENDER
# ============================================================

if not patients.empty:

    gender_count.plot(
        kind="bar",
        title="Patients by Gender"
    )

    plt.xlabel("Gender")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 2
# PATIENTS BY DIAGNOSIS
# ============================================================

if not patients.empty:

    diagnosis_count.plot(
        kind="bar",
        title="Patients by Diagnosis"
    )

    plt.xlabel("Diagnosis")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 3
# PATIENTS BY AGE GROUP
# ============================================================

if not patients.empty:

    age_group_count.plot(
        kind="bar",
        title="Patients by Age Group"
    )

    plt.xlabel("Age Group")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 4
# DOCTORS BY SPECIALIZATION
# ============================================================

if not doctors.empty:

    specialization_count.plot(
        kind="bar",
        title="Doctors by Specialization"
    )

    plt.xlabel("Specialization")
    plt.ylabel("Number of Doctors")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 5
# APPOINTMENTS BY REASON
# ============================================================

if not appointments.empty:

    reason_count.plot(
        kind="bar",
        title="Appointments by Reason"
    )

    plt.xlabel("Appointment Reason")
    plt.ylabel("Number of Appointments")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 6
# PAYMENT STATUS
# ============================================================

if not bills.empty:

    payment_status.plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Payment Status"
    )

    plt.ylabel("")
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 7
# BILLS BY SERVICE
# ============================================================

if not bills.empty:

    service_count.plot(
        kind="bar",
        title="Bills by Service"
    )

    plt.xlabel("Service")
    plt.ylabel("Number of Bills")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# VISUALIZATION 8
# MOST PRESCRIBED MEDICINES
# ============================================================

if not prescriptions.empty:

    medicine_count.plot(
        kind="bar",
        title="Most Prescribed Medicines"
    )

    plt.xlabel("Medicine")
    plt.ylabel("Number of Prescriptions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================================
# CLOSE DATABASE
# ============================================================

connection.close()

print("\n" + "=" * 55)
print("          ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 55)
