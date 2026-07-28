# User Registration System

users = []

def register_user():
    print("=== User Registration ===")

    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (Admin/Doctor/Receptionist): ")

    user = {
        "username": username,
        "password": password,
        "role": role
    }

    users.append(user)

    print("User registered successfully!")


# Test registration
register_user()

print("\nRegistered Users:")
for user in users:
    print(user)