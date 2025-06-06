

def count_words(content):
    split = content.split()
    count = 0
    for word in split:
        if len(word) != 0:
            count += 1
    return count

def count_letters(content):
    words = content.lower().split()
    letter_count = {}
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] = 1+letter_count[letter]
            else:
                letter_count[letter] = 1
    return letter_count

def sort_on(letter_count):
    sort_letters = {}
    for letter in letter_count:
        if letter.isalpha():
            sort_letters[letter] = letter_count[letter]
    return sort_letters