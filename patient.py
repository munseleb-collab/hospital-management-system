
from models.patient import Patient


def add_patient():

    print("=== Patient Registration ===")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    while True:
        try:
            age = int(input("Age: "))

            if age < 0 or age > 120:
                print("Please enter a valid age.")
                continue

            break

        except ValueError:
            print("Please enter a valid number for age.")

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
