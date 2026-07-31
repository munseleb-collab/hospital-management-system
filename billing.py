import sqlite3

def create_bill():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Create Patient Bill ===")

    patient_id = input("Enter Patient ID: ")

    cursor.execute(
        "SELECT first_name, last_name FROM patients WHERE id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    if patient is None:
        print("Patient not found.")
        connection.close()
        return

    print("Patient:", patient[0], patient[1])

    service = input("Service Provided: ")
    amount = float(input("Amount: "))
    payment_status = input("Payment Status (Paid/Pending): ")

    cursor.execute("""
    INSERT INTO bills
    (patient_id, service, amount, payment_status)
    VALUES (?, ?, ?, ?)
    """,
    (patient_id, service, amount, payment_status))

    connection.commit()
    connection.close()

    print("Bill created successfully!")


if __name__ == "__main__":
    create_bill()