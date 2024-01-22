import argparse
from bs4 import BeautifulSoup as bs
from hebrew import Hebrew
import json
import pyfiglet
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(description="Search and retrieve Jewish texts.")
    parser.add_argument(
        "-s",
        "--search",
        type=str,
        nargs="+",
        help="search for the correct spelling of the book",
    )
    parser.add_argument(
        "-b", "--book", type=str, nargs="+", help="Enter book name in English"
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        choices=["en", "he"],
        help="Choose language of the text",
    )
    parser.add_argument(
        "-r", "--random", action="store_true", help="Retrieve a random text"
    )
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Use the program interactively"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.interactive:
        interactive_mode()
    elif args.search:
        find_book(args.search)
    elif args.book and args.language:
        retrieve_text(args.book, args.language)
    elif args.random:
        retrieve_text("random", "he", random=True)
    else:
        print("Invalid arguments. Use -h or --help for more information.")


def retrieve_text(book, language, random=False):
    """
    Retrieves text from a book using the Sefaria API.

    :param book: The name of the book to retrieve text from.
    :type book: str
    :param language: The language of the text to retrieve ("en" for English, "he" for Hebrew).
    :type language: str
    :param random: Whether to retrieve a random text.
    :type random: bool
    """
    if type(book) == list:
        book_name = " ".join(book)
    else:
        book_name = book
    base_url = "https://www.sefaria.org/api/texts/"
    response = requests.get(base_url + book_name)
    loaded_json = json.loads(response.text)
    if random:
        try:
            print(loaded_json["heRef"])
            cleaned = bs(loaded_json["he"], "html.parser").get_text()
            print(cleaned)
        except Exception:
            print(f"{Exception} \n Something went wrong, sorry.")
    else:
        try:
            if language == "en":
                english_sentences = []
                for line in loaded_json["text"]:
                    english_sentences.append(bs(line, "html.parser").get_text())
                english_paragraph = "\n".join(english_sentences)
                print(english_paragraph)
            elif language == "he":
                hebrew_sentences = []
                for line in loaded_json["he"]:
                    hebrew_sentences.append(bs(line, "html.parser").get_text())
                hebrew_paragraph = "\n".join(hebrew_sentences)
                clean = Hebrew(hebrew_paragraph)
                text_only = clean.text_only()
                print(text_only)
            else:
                print("Invalid language. Please use 'en' or 'he'.")
        except KeyError:
            print(
                "The text was not found. use the search function to find the correct spelling"
            )


def find_book(search):
    """
    Searches for a book in the Sefaria Database.

    Parameters:
        search (list): A list of words to search for.

    Returns:
        None
    """
    if type(search) == list:
        searched = " ".join(search)
    else:
        searched = search
    response = requests.get("https://www.sefaria.org/api/name/" + searched)
    loaded_json = json.loads(response.text)
    if loaded_json["is_ref"] == True:
        print("It seems like you have the correct spelling")
    else:
        for completion in loaded_json["completions"]:
            print(completion)


def interactive_mode():
    name = "Learn"
    tagline = "Like a hacker"
    print(pyfiglet.figlet_format(name))
    print(pyfiglet.figlet_format(tagline, font="univers"))
    print("Do you know the correct spelling of the book? (y/n)")
    knows_spelling = input(">>> ")
    if knows_spelling not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.")
    elif knows_spelling == "n":
        help_searching()
    print("Enter the name of the book: ")
    book = input(">>> ")
    print(
        "Enter the language you want to read in ('en' for English, 'he' for Hebrew): "
    )
    language = input(">>> ")
    retrieve_text(book, language)


def help_searching():
    print("Enter a possible spelling: ")
    search = input(">>> ")
    print("Here are possible matches: ")
    find_book(search)
    print("did you find what you're looking for? (y/n)")
    found = input(">>> ")
    if found == "n":
        help_searching()


if __name__ == "__main__":
    main()
