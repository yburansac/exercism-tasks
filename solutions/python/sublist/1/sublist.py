"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def is_sublist(list_one, list_two):

    len_one = len(list_one)
    return any(list_one == list_two[i:i+len_one] for i in range(len(list_two) - len_one + 1))

def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL

    # empty list is always sublist of any other list
    if not list_one:
        return SUBLIST
    elif not list_two:
        return SUPERLIST

    if is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL

    
