import sqlite3

def view_bills():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Patient Bills ===")

    cursor.execute("""
    SELECT
        bills.id,
        patients.first_name || ' ' || patients.last_name,
        bills.service,
        bills.amount,
        bills.payment_status
    FROM bills
    INNER JOIN patients
        ON bills.patient_id = patients.id
    """)

    bills = cursor.fetchall()

    if len(bills) == 0:
        print("No bills found.")
    else:
        for bill in bills:
            print("\nBill ID:", bill[0])
            print("Patient:", bill[1])
            print("Service:", bill[2])
            print("Amount:", bill[3])
            print("Payment Status:", bill[4])

    connection.close()


if __name__ == "__main__":
    view_bills()