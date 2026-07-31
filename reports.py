import sqlite3

def billing_report():

    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    # Total Revenue
    cursor.execute("SELECT SUM(amount) FROM bills")
    total_revenue = cursor.fetchone()[0]

    if total_revenue is None:
        total_revenue = 0

    # Paid Bills
    cursor.execute("""
    SELECT COUNT(*)
    FROM bills
    WHERE LOWER(payment_status) = 'paid'
    """)
    paid_bills = cursor.fetchone()[0]

    # Pending Bills
    cursor.execute("""
    SELECT COUNT(*)
    FROM bills
    WHERE LOWER(payment_status) = 'pending'
    """)
    pending_bills = cursor.fetchone()[0]

    connection.close()

    print("\n" + "=" * 45)
    print("         BILLING REPORT")
    print("=" * 45)
    print(f"Total Revenue : {total_revenue}")
    print(f"Paid Bills    : {paid_bills}")
    print(f"Pending Bills : {pending_bills}")
    print("=" * 45)


if __name__ == "__main__":
    billing_report()