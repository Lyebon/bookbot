def get_book_text(relative_path):
    with open(relative_path) as f:
        content = f.read()
        return content


def main():
    content = get_book_text("books/frankenstein.txt")
    print(content)


main()
