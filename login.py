from models.user import User


print("=== Login ===")

username = input("Username: ")
password = input("Password: ")


user = User(
    username,
    password
)


result = user.login()


if result:
    print("Login successful!")
else:
    print("Invalid username or password")