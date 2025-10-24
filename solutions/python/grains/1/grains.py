def square(number):

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    grains_on_square = pow(2, (number-1))
    
    return grains_on_square
    


def total():
    total = 0
    
    for i in range (0,64):
        
        total += pow(2,i)

    return total

    
