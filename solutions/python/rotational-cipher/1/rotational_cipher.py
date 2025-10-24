def rotate(text, key):

    if key in [0,26]:
        return text

    result = []
    for char in text: 

        if not char.isalpha():
            result.append(char)
            continue
            
        start = ord("a") if char.islower() else ord("A")

        rotated_char = chr((ord(char) + key - start) % 26 + start)
        result.append(rotated_char)
    
    return "".join(result)
    
    
