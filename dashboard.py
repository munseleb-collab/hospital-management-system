
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def dashboard():

    # ============================================================
    # CONNECT TO DATABASE
    # ============================================================

    connection = sqlite3.connect("hospital.db")

    # ============================================================
    # LOAD HOSPITAL DATA
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

    prescriptions = pd.read_sql_query(
        "SELECT * FROM prescriptions",
        connection
    )

    bills = pd.read_sql_query(
        "SELECT * FROM bills",
        connection
    )

    # ============================================================
    # CALCULATE MAIN STATISTICS
    # ============================================================

    total_patients = len(patients)
    total_doctors = len(doctors)
    total_appointments = len(appointments)
    total_prescriptions = len(prescriptions)
    total_bills = len(bills)

    if not bills.empty:
        total_revenue = bills["amount"].sum()
        average_bill = bills["amount"].mean()
    else:
        total_revenue = 0
        average_bill = 0

    # ============================================================
    # PATIENT STATISTICS
    # ============================================================

    if not patients.empty:

        valid_gender_data = patients[
            patients["gender"].isin(["Male", "Female"])
        ]

        gender_count = valid_gender_data["gender"].value_counts()

        diagnosis_count = patients["diagnosis"].value_counts()

        average_age = patients["age"].mean()

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

        age_group_count = (
            patients["age_group"]
            .value_counts()
            .sort_index()
        )

    # ============================================================
    # DOCTOR STATISTICS
    # ============================================================

    if not doctors.empty:

        specialization_count = (
            doctors["specialization"]
            .value_counts()
        )

    # ============================================================
    # APPOINTMENT STATISTICS
    # ============================================================

    if not appointments.empty:

        appointment_reason_count = (
            appointments["reason"]
            .value_counts()
        )

    # ============================================================
    # BILLING STATISTICS
    # ============================================================

    if not bills.empty:

        bills["payment_status"] = (
            bills["payment_status"]
            .str.strip()
            .str.capitalize()
        )

        payment_status = (
            bills["payment_status"]
            .value_counts()
        )

        service_revenue = (
            bills.groupby("service")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

    # ============================================================
    # PRESCRIPTION STATISTICS
    # ============================================================

    if not prescriptions.empty:

        medicine_count = (
            prescriptions["medicine"]
            .value_counts()
        )

    # ============================================================
    # DISPLAY DASHBOARD
    # ============================================================

    print("\n" + "=" * 60)
    print("             HOSPITAL ANALYTICS DASHBOARD")
    print("=" * 60)

    print("\nDATASET OVERVIEW")
    print("-" * 60)

    print(f"Total Patients       : {total_patients}")
    print(f"Total Doctors        : {total_doctors}")
    print(f"Total Appointments   : {total_appointments}")
    print(f"Total Bills          : {total_bills}")
    print(f"Total Prescriptions  : {total_prescriptions}")

    # ============================================================
    # PATIENT SUMMARY
    # ============================================================

    print("\n" + "-" * 60)
    print("PATIENT SUMMARY")
    print("-" * 60)

    print(f"Average Patient Age  : {average_age:.2f}")

    print("\nPatients by Gender:")
    print(gender_count)

    print("\nTop 5 Diagnoses:")
    print(diagnosis_count.head(5))

    print("\nPatients by Age Group:")
    print(age_group_count)

    # ============================================================
    # DOCTOR SUMMARY
    # ============================================================

    print("\n" + "-" * 60)
    print("DOCTOR SUMMARY")
    print("-" * 60)

    print(f"Total Doctors        : {total_doctors}")

    print("\nDoctors by Specialization:")
    print(specialization_count)

    # ============================================================
    # APPOINTMENT SUMMARY
    # ============================================================

    print("\n" + "-" * 60)
    print("APPOINTMENT SUMMARY")
    print("-" * 60)

    print(f"Total Appointments   : {total_appointments}")

    print("\nTop Appointment Reasons:")
    print(appointment_reason_count.head(5))

    # ============================================================
    # FINANCIAL SUMMARY
    # ============================================================

    print("\n" + "-" * 60)
    print("FINANCIAL SUMMARY")
    print("-" * 60)

    print(f"Total Bills          : {total_bills}")
    print(f"Total Revenue        : ZMW {total_revenue:,.2f}")
    print(f"Average Bill         : ZMW {average_bill:,.2f}")

    print("\nPayment Status:")
    print(payment_status)

    print("\nRevenue by Service:")
    print(service_revenue)

    # ============================================================
    # PRESCRIPTION SUMMARY
    # ============================================================

    print("\n" + "-" * 60)
    print("PRESCRIPTION SUMMARY")
    print("-" * 60)

    print(f"Total Prescriptions  : {total_prescriptions}")

    print("\nTop 5 Prescribed Medicines:")
    print(medicine_count.head(5))

    print("\n" + "=" * 60)
    print("          DASHBOARD DATA LOADED SUCCESSFULLY")
    print("=" * 60)

    # ============================================================
    # CLOSE DATABASE
    # ============================================================

    connection.close()

    # ============================================================
    # CHART 1 — PATIENTS BY GENDER
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
    # CHART 2 — TOP 5 DIAGNOSES
    # ============================================================

    if not patients.empty:

        diagnosis_count.head(5).plot(
            kind="bar",
            title="Top 5 Patient Diagnoses"
        )

        plt.xlabel("Diagnosis")
        plt.ylabel("Number of Patients")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    # ============================================================
    # CHART 3 — PATIENTS BY AGE GROUP
    # ============================================================

    if not patients.empty:

        age_group_count.plot(
            kind="bar",
            title="Patients by Age Group"
        )

        plt.xlabel("Age Group")
        plt.ylabel("Number of Patients")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    # ============================================================
    # CHART 4 — DOCTORS BY SPECIALIZATION
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
    # CHART 5 — APPOINTMENTS BY REASON
    # ============================================================

    if not appointments.empty:

        appointment_reason_count.plot(
            kind="bar",
            title="Appointments by Reason"
        )

        plt.xlabel("Appointment Reason")
        plt.ylabel("Number of Appointments")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # ============================================================
    # CHART 6 — PAYMENT STATUS
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
    # CHART 7 — REVENUE BY SERVICE
    # ============================================================

    if not bills.empty:

        service_revenue.plot(
            kind="bar",
            title="Revenue by Hospital Service"
        )

        plt.xlabel("Service")
        plt.ylabel("Revenue (ZMW)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # ============================================================
    # CHART 8 — TOP PRESCRIBED MEDICINES
    # ============================================================

    if not prescriptions.empty:

        medicine_count.head(5).plot(
            kind="bar",
            title="Top 5 Prescribed Medicines"
        )

        plt.xlabel("Medicine")
        plt.ylabel("Number of Prescriptions")
        plt.tight_layout()
        plt.show()

