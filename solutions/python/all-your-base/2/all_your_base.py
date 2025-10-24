#https://www.youtube.com/watch?v=hIs3A6gGz2w

def to_10base(input_base, digits) -> int:
    result = 0
    
    for index, item in enumerate(reversed(digits)):

        if item < 0 or item >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
        result += item*pow(input_base, index)
        
    return result 

def to_anybase(base, value) -> list[int]:

    if value == 0:
        return [0]

    remainders = list()

    while(value != 0):
        remainders.append(value % base)
        value = value // base 
            
    return remainders[::-1]
    
    
        
    
def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not digits:
        return [0]
        

    interstate = to_10base(input_base, digits)
    return to_anybase(output_base, interstate)
    
