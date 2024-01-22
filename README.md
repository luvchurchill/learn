# Learn

<img width="231" alt="PoweredBySefaria" src="https://github.com/luvchurchill/learn/assets/46406654/74a25bc9-1650-4d08-838c-143faaf46e5f">


This program is designed to search and retrieve Jewish texts from the Sefaria database. Users can specify the book name, search for the correct spelling of the book, choose the language of the text (English or Hebrew), and interact with the program in an interactive mode.

## Installation

```
git clone https://github.com/luvchurchill/learn.git
```
```
cd learn
```
```
python3 pip -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```


## Usage

```
usage: app.py [-h] [-s SEARCH [SEARCH ...]] [-b BOOK [BOOK ...]] [-l {en,he}]
              [-i]

Search and retrieve Jewish texts.

options:
  -h, --help            show this help message and exit
  -s SEARCH [SEARCH ...], --search SEARCH [SEARCH ...]
                        search for the correct spelling of the book
  -b BOOK [BOOK ...], --book BOOK [BOOK ...]
                        Enter book name in English
  -l {en,he}, --language {en,he}
                        Choose language of the text
  -i, --interactive     Use the program interactively
  ```

------
### Credits

- [Sefaria](https://www.sefaria.org/)
- [Codeium](https://codeium.com/) 
