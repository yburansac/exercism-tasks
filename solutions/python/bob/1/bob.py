
def sentence_upper(sentence):
    if not any(letter.isalpha() for letter in sentence):
        return False

    for letter in sentence:
        if letter.isalpha() and not letter.isupper():
            return False
    return True



def response(hey_bob):

    if sentence_upper(hey_bob) and hey_bob.strip().endswith('?'): 
        return "Calm down, I know what I'm doing!"
    elif sentence_upper(hey_bob):
        return "Whoa, chill out!"
    elif hey_bob.strip().endswith('?'):
        return "Sure."
    elif hey_bob.strip() == "":
        return "Fine. Be that way!" 
    else: 
        return "Whatever."


    
    pass
