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

def sort_on_char(char_dict):
    order = []
    for char in char_dict:
        if char.isalpha():
             order.append({"char": char, "num": char_dict[char]})
    order.sort(reverse=True, key=sort_on)
    return order

def sort_on(item):
    return item["num"]