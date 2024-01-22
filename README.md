# Learn

<img width="231" alt="PoweredBySefaria" src="https://github.com/luvchurchill/learn/assets/46406654/74a25bc9-1650-4d08-838c-143faaf46e5f">


This program is designed to search and retrieve Jewish texts from the Sefaria database. Users can specify the book name, search for the correct spelling of the book, choose the language of the text (English or Hebrew), and interact with the program in an interactive mode.

- [Installation](#installation)
- [Usage](#usage)
- [Issues](#issues)
- [Credits](#credits)

## Installation

Clone the repo
```
git clone https://github.com/luvchurchill/learn.git
```
Change into the directory
```
cd learn
```
Create a virtual environment
```
python3 pip -m venv venv
```
Activate the virtual environment
```
source venv/bin/activate
```
Install the requirements
```
pip install -r requirements.txt
```
Done! you can now use the program.

To deactivate the virtual environment
```
deactivate
```


## Usage

To read a text use `python3 app.py -b book name -l language`
Please note that the spelling of the book name must be correct. In order to get the correct name use `python3 app.py -s possible book name`. This will return a few book names that are close to the correct spelling. For example, `python3 app.py -s "Ramban Genesis"` will return "Ramban on Genesis" among other possible books.
Some books are only in English or only in Hebrew so please take that into account if it returns "no text found".
To retrieve a specific chapter try to add numbers at the end of the book name `python3 app.py -b Ramban on Genesis 2 -l he` this *usually* works.

You can get a random text by using `python3 app.py -r`

There is also an interactive mode that you can use with `python3 app.py -i`. This might be easier to use but you lose the ability to pipe the output to any other program/file.

```
usage: app.py [-h] [-s SEARCH [SEARCH ...]] [-b BOOK [BOOK ...]] [-l {en,he}] [-r] [-i]

Search and retrieve Jewish texts.

options:
  -h, --help            show this help message and exit
  -s SEARCH [SEARCH ...], --search SEARCH [SEARCH ...]
                        search for the correct spelling of the book
  -b BOOK [BOOK ...], --book BOOK [BOOK ...]
                        Enter book name in English
  -l {en,he}, --language {en,he}
                        Choose language of the text
  -r, --random          Retrieve a random text
  -i, --interactive     Use the program interactively
  ```

------
## Issues
I tested it on two terminals, on one of them it returns hebrew text backwards. I wrote a fix for this but then it ruined it on the other terminal. If you are having this problem please open an issue.


### Credits

- [Sefaria](https://www.sefaria.org/)
- [Codeium](https://codeium.com/) 
