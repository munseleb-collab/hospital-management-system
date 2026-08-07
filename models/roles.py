from models.user import User


class Admin(User):

    def dashboard(self):
        return "Admin Dashboard: Manage users, doctors, and reports"


class DoctorUser(User):

    def dashboard(self):
        return "Doctor Dashboard: View patients and prescriptions"


class Receptionist(User):

    def dashboard(self):
        return "Receptionist Dashboard: Register patients and book appointments"