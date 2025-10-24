def is_isogram(string):
    word = string.lower()

    for letter in word:
        if letter == " " or letter == "-":
            pass
        elif word.count(letter) > 1:
            return False

    return True