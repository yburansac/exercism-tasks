import re 

def add_ay(text):
    return text + "ay"

def translate(text):

    vowels = 'aeiou'
    results = ""

    
    for word in text.split(" "):

        if match := re.match(r'^([aeiou]+|xr|yt)([a-zA-Z]*)', word):
            results += add_ay(word)
        elif match := re.match(r'^([^aeiou]*qu)(.*)', word):
            results += add_ay(match.group(2) + match.group(1))
        elif match := re.match(r'^([^aeiou]+)([y])([a-zA-Z]*)', word):
            results += add_ay(match.group(2) + match.group(3) + match.group(1))
        elif match := re.match(r'^([^aeiou]+)([aeiou]+)([a-zA-Z]*)', word):
            results += add_ay(match.group(2) + match.group(3) + match.group(1))

        results += " "
    
    return results.strip()
    

    
    












        
        

    
    
