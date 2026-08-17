
from medical_history import view_medical_history
from dashboard import dashboard
from login import login
from patient import add_patient
from view_patients import view_patients
from update_patient import update_patient
from delete_patient import delete_patient
from search_patient import search_patient
from doctor import add_doctor
from view_doctors import view_doctors
from appointment import add_appointment
from view_appointments import view_appointments
from billing import create_bill
from view_bills import view_bills
from prescription import add_prescription
from view_prescriptions import view_prescriptions
from reports import billing_report


def menu():

    while True:

        print("\n=== Hospital Management System ===")
        print("1. Dashboard")
        print("2. Register Patient")
        print("3. View Patients")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Search Patient")
        print("7. Register Doctor")
        print("8. View Doctors")
        print("9. Book Appointment")
        print("10. View Appointments")
        print("11. Create Bill")
        print("12. View Bills")
        print("13. Add Prescription")
        print("14. View Prescription")
        print("15. Billing Report")
        print("16. View Medical History")
        print("17. Generate Patient Report")
        print("18. Backup Database")
        print("19. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dashboard()

        elif choice == "2":
            add_patient()

        elif choice == "3":
            view_patients()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            search_patient()

        elif choice == "7":
            add_doctor()

        elif choice == "8":
            view_doctors()

        elif choice == "9":
            add_appointment()

        elif choice == "10":
            view_appointments()

        elif choice == "11":
            create_bill()

        elif choice == "12":
            view_bills()

        elif choice == "13":
            add_prescription()

        elif choice == "14":
            view_prescriptions()

        elif choice == "15":
            billing_report()

        elif choice == "16":
            view_medical_history()

        elif choice == "17":
            from patient_report import generate_patient_report
            generate_patient_report()

        elif choice == "18":
            from database_backup import backup_database
            backup_database()

        elif choice == "19":
            print("Thank you for using the Hospital Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if login():
    menu()
else:
    print("Access denied.")
