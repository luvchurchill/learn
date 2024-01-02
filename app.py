from bs4 import BeautifulSoup as bs
import difflib
from hebrew import Hebrew
import json
import requests
from spellchecker import SpellChecker

class SpellChecker:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def find_similar_word(self, word):
        return difflib.get_close_matches(word, self.wordlist, n=3)


def main():
    """
    Retrieves and displays the text of a book from the Sefaria API based on user input.

    Returns:
    None
    """
    base_url = "https://www.sefaria.org/api/texts/"
    search = input("Search? y/n: ")
    if search == "y":
        find_text()
    book = input("Enter book name in english: ")
    response = requests.get(base_url + book)
    loaded_json = json.loads(response.text)
    lang = input("Enter language: ")
    if lang == "en":
        english_sentences = []
        for line in loaded_json["text"]:
            english_sentences.append(bs(line, "html.parser").get_text())
        english_paragraph = "\n".join(english_sentences)
        print(english_paragraph)
    elif lang == "he":
        hebrew_sentences = []
        for line in loaded_json["he"]:
            hebrew_sentences.append(bs(line, "html.parser").get_text())
        hebrew_paragraph = "\n".join(hebrew_sentences)
        clean = Hebrew(hebrew_paragraph)
        print(clean.text_only())

def find_text():
    response = requests.get("https://www.sefaria.org/api/index/titles")
    all_titles = json.loads(response.text)
    search = input("what book are you looking for? ")

    wordlist = all_titles['books']
    checker = SpellChecker(wordlist)
    similar_word = checker.find_similar_word(search)
    print(f"did you mean one of these? {similar_word} ")  


main()
