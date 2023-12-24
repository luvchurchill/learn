import requests
import json
from bs4 import BeautifulSoup as bs 

def extract_hebrew_text(loaded_json):
        """Extract Hebrew text from loaded JSON while parsing HTML content.

        Args:
        - loaded_json: dict, the JSON object loaded from the request response

        Returns:
        - str, the Hebrew text with HTML tags removed
        """
        hebrew_html = loaded_json
        soup = bs(hebrew_html, 'html.parser')
        return soup.get_text()[::-1]

# In main function, call the new extract_hebrew_text function
def main():
    base_url = "https://www.sefaria.org/api/texts/"
    # Add Hebrew book name as parameter
    book = input("Enter book name in english: ")
    response = requests.get(base_url + book)
    loaded_json = json.loads(response.text)
    hebrew_sentences = []
    for line in loaded_json['he']:
        hebrew_sentences.append(extract_hebrew_text(line))
    hebrew_paragraph = '\n'.join(hebrew_sentences)
    print(hebrew_paragraph)

def extract_hebrew_text(loaded_json):
    """Extract Hebrew text from loaded JSON while parsing HTML content.

    Args:
    - loaded_json: dict, the JSON object loaded from the request response

    Returns:
    - str, the Hebrew text with HTML tags removed
    """
    hebrew_html = loaded_json
    soup = bs(hebrew_html, 'html.parser')
    return soup.get_text()[::-1]


main()

