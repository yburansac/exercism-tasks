def steps(number):

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    result = number
    counter = 0
    while (result != 1):
        if result % 2 != 0:
            result = 3*result +1
        else:
            result = result / 2
        counter +=1

    
    return counter
