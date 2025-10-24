import math
from itertools import count

# pretty fast one https://en.wikipedia.org/wiki/Fast_inverse_square_root
def make_guess(number) -> int:

    L = len(str(number))
    d = math.ceil(L/2)

    guess2 = 2*10**(d-1)
    guess7 = 7*10**(d-1)

    if abs(guess2**2 - number) < abs(guess7**2 - number):
        return guess2
    return guess7



def square_root(number):

    if number == 0:
        return 0
    if number == 1:
        return 1


    x_i = make_guess(number)
    x_ii = 0


    while round(x_i, 2) != round(x_ii, 2):
        x_ii = x_i
        x_i = (x_ii + number / x_ii) / 2

    return round(x_i,0)