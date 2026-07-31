import sqlite3

def view_doctors():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()

    print("\n=== Doctor Records ===")

    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()

    if len(doctors) == 0:
        print("No doctors found.")
    else:
        for doctor in doctors:
            print("\nDoctor ID:", doctor[0])
            print("First Name:", doctor[1])
            print("Last Name:", doctor[2])
            print("Specialization:", doctor[3])
            print("Phone:", doctor[4])

    connection.close()

if __name__ == "__main__":
    view_doctors()