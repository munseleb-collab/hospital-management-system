from models.roles import Admin, DoctorUser, Receptionist


users = [
    Admin("Admin", "1234"),
    DoctorUser("James", "1234"),
    Receptionist("Mary", "1234")
]


for user in users:
    print(user.dashboard())