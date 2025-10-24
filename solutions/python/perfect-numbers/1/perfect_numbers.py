

def  aliquot_sum(number):

    # determine proper divisions of the number (any divisors less than number itself)
    divisors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.add(i)
            if i != number // i and i != 1 : # Add the paired divisor, if distinct and not n itself
                divisors.add(number // i)

    return sum(divisors)


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1: 
        return "deficient" # exception of prime numbers which are deficient by default 

    a_s = aliquot_sum(number)
    
    if a_s == number:
        return "perfect"
    if a_s < number:
        return "deficient"
    return "abundant"
        