import string

def encode(plain_text: str) -> str:
    letters = string.ascii_lowercase

    result = [
        letters[-letters.index(ch.lower()) - 1] if ch.isalpha() else ch
        for ch in plain_text
        if ch.isalnum() # filter out non-alphanumeric characters
    ]
    return ' '.join(''.join(result[i:i + 5]) for i in range(0, len(result), 5))

def decode(ciphered_text: str) -> str:

    letters = string.ascii_lowercase

    result = [
        letters[25 - letters.index(ch)] if ch.isalpha() else ch
        for ch in ciphered_text
        if ch.isalnum()
    ]
    return "".join(result)
