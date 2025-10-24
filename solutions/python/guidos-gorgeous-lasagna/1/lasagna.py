"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_times: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_times

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate how many minutes you spend by preparing lasagna based on number of their layers.

    :param number_of_layers: int - number of layers you want to add to the lasagna 
    :return: int - how many minutes you would spend making them
    
    """

    return LAYER_PREPARATION_TIME*number_of_layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    
    :param number_of_layers: int - number of layers you want to add to the lasagna 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int -  total number of minutes you've been cooking
    
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


