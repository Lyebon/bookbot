from stats import *


def get_book_text(relative_path):
    with open(relative_path) as f:
        content = f.read()
        return content

def main():
    content = get_book_text("books/frankenstein.txt")
    count = count_words(content)
    letters = count_letters(content)
    sort_letters = sort_on(letters)
    print(f"{count} words found in the document")
    print (letters)
    print (sort_letters)


main()
