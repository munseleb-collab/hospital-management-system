
from models.user import User


def login():

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
        return True

    else:
        print("Invalid username or password")
        return False
from models.user import User


def login():

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
        return True

    else:
        print("Invalid username or password")
        return False


if __name__ == "__main__":
    login()