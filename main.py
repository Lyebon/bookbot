from stats import *
import sys

def get_book_text(relative_path):
    with open(relative_path) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    content = get_book_text(book)
    count = count_words(content)
    letters = count_letters(content)
    sort_letters = sort_on_char(letters)
    

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...\n")
    print(f"----------- Word Count ----------\n    Found {count} total words\n--------- Character Count -------")
    for letter in sort_letters:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")



main()