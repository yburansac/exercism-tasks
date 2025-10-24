def reverse(text):

    reversed_text = []
    for i in range(1, len(text)+1):
        reversed_text.append(text[-i])
    
    return "".join(reversed_text)
