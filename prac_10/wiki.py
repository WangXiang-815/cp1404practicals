import wikipedia

def main():
    """A function to try wikipedia"""
    while True:
        title = input("Enter title page:").strip()
        if title == '':
            print("Thank you.")
            break