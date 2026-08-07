from models.doctor import Doctor


print("=== Doctor Registration ===")

first_name = input("First Name: ")
last_name = input("Last Name: ")
specialization = input("Specialization: ")
phone = input("Phone Number: ")


doctor = Doctor(
    first_name,
    last_name,
    specialization,
    phone
)


doctor.save()