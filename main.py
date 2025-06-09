from stats import *


def get_book_text(relative_path):
    with open(relative_path) as f:
        content = f.read()
        return content

def main():
    content = get_book_text("books/frankenstein.txt")
    count = count_words(content)
    letters = count_letters(content)
    sort_letters = sort_on_char(letters)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n")
    print(f"----------- Word Count ----------\n    Found {count} total words\n--------- Character Count -------")
    for letter in sort_letters:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")



main()
