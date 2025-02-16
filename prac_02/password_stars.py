import getpass

def get_password():
    password = getpass.getpass("Enter your password: ")
    return password

def main():
    password = get_password()
    if password == "123456wx":
        print("You have successfully logged in")
    else:
        print("Incorrect password!")

if __name__ == "__main__":
    main()

