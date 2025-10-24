def is_armstrong_number(number):

    number_as_string = str(number)
    
    power = len(number_as_string)

    base = 0
    for i in number_as_string:
        base += pow(int(i), power)

    return base == number
    
    
