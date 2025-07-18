import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """A function to try wikipedia"""
    while True:
        title = input("Enter title page:").strip()
        if not title:
            print("Thank you.")
            break

    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(DisambiguationError.options[:5],"...")
    except PageError:
        print(f"Page id {title} does not match any pages. Try another id!")

main()
