from functools import reduce
from typing import List, Union


# accumulator for temporary storing the operators
def evaluate(accum, element) -> List[Union[int, str]]:

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
    }

    try:
        if element in "+-*/":
            accum.append(element)  # storing the operator for later use to the beginning of the list
        else:
            if len(accum) == 1:  # first number
                accum[0] = int(element)
            elif accum[-1] in "+-*/":  # last number
                oper: str = accum.pop()
                val1: int = accum[0]
                val2: int = int(element)
                accum[0] = operations[oper](val1, val2)
            else:
                raise ValueError("syntax error")
        return accum
    except ValueError:
        raise ValueError("syntax error")


def answer(question: str) -> int:

    word_to_operator = {
        "plus": "+",
        "minus": "-",
        "multiplied": "*",
        "divided": "/",
    }

    if not question.startswith("What is") and not question.endswith("?"):
        raise ValueError("syntax error")

    t = question[8:-1].split()

    if len(t) == 0:
        raise ValueError("syntax error")

    # Ensure no two numbers appear consecutively in the parsed input
    for i in range(len(t) - 1):
        if t[i].lstrip("-").isdigit() and t[i + 1].lstrip("-").isdigit():
            raise ValueError("syntax error")

    # Replace words like 'plus', 'minus', etc., with their operator equivalents
    for index, item in enumerate(t):
        if item in word_to_operator:
            if item in ("multiplied", "divided"):
                if not (index + 1 < len(t) and t[index + 1] == "by"):
                    raise ValueError("syntax error")
                else:
                    t.pop(index + 1)
            t[index] = word_to_operator[item]
        elif not item.lstrip("-").isdigit() and item not in word_to_operator:
            raise ValueError("unknown operation")

    result = reduce(evaluate, t, [0])
    if len(result) != 1:
       raise ValueError("syntax error")
    return result[0]