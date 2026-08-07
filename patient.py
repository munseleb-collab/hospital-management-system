from models.patient import Patient

print("=== Patient Registration ===")

first_name = input("First Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
phone = input("Phone Number: ")
address = input("Address: ")
diagnosis = input("Diagnosis: ")

patient = Patient(
    first_name,
    last_name,
    age,
    gender,
    phone,
    address,
    diagnosis
)

patient.save()