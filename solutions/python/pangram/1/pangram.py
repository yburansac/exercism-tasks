def is_pangram(sentence):

    sentence = sentence.strip()

    letters = set()
    for word in sentence:
        if word.isalpha():
            letters.add(word.lower())

    if len(letters) == 26:
        return True
    return False


    

