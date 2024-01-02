import argparse
from bs4 import BeautifulSoup as bs
import difflib
from hebrew import Hebrew
import json
import requests


class SpellChecker:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def find_similar_word(self, word):
        """
        Find similar words in the wordlist based on a given word.

        Parameters:
            word (str): The word to find similar matches for.

        Returns:
            List[str]: A list of up to 3 similar words from the wordlist.
        """
        return difflib.get_close_matches(word, self.wordlist, n=3)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Search and retrieve book texts.")
    parser.add_argument(
    "-s", "--search", type=str, nargs='+', help="Enable book search"
)
    parser.add_argument("-b", "--book", type=str, nargs='+', help="Enter book name in English")
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        choices=["en", "he"],
        help="Choose language of the book text",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.search:
        find_book(args.search)
    elif args.book and args.language:
        retrieve_text(args.book, args.language)
    else:
        print("Invalid arguments. Please use -h or --help for help.")


def retrieve_text(book, language):
    """
    Retrieves text from a book using the Sefaria API.

    :param book: The name of the book to retrieve text from.
    :type book: str
    :param language: The language of the text to retrieve ("en" for English, "he" for Hebrew).
    :type language: str
    """
    book_name = " ".join(book)
    base_url = "https://www.sefaria.org/api/texts/"
    response = requests.get(base_url + book_name)
    loaded_json = json.loads(response.text)
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
    except KeyError:
        print("The text was not found. use the search function to find the correct spelling")


def find_book(search):
    """
    Searches for a book in the Sefaria Database.

    Parameters:
        search (list): A list of words to search for.

    Returns:
        None
    """
    searched = " ".join(search)
    response = requests.get("https://www.sefaria.org/api/index/titles")
    all_titles = json.loads(response.text)
    wordlist = all_titles["books"]
    spell_checker = SpellChecker(wordlist)
    similar_word = spell_checker.find_similar_word(searched)
    print(f"did you mean one of these? {similar_word} ")


if __name__ == "__main__":
    main()
