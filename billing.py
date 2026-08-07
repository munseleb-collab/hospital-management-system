from models.billing import Bill


print("=== Generate Bill ===")

patient_id = input("Patient ID: ")
amount = float(input("Amount: "))
payment_status = input("Payment Status (Paid/Unpaid): ")


bill = Bill(
    patient_id,
    amount,
    payment_status
)


bill.save()
