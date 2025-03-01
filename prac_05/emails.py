"""
estimated time: 20mins
actual time:
"""

def main():
    """create dict of emails_to_names"""
    email_to_name ={}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email) #TODO: write this func
        confirmation = input(f"Is your name {name}? (Y/n)")
        #press Enter to accept the default of (Y)es.
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email =input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} {email}")

def get_name_from_email(email):



