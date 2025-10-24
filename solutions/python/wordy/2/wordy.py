from functools import reduce
from typing import List, Union


# accumulator for temporary storing the operators
def evaluate(accum, element) -> List[Union[int, str]]:

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
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

    question = question.removeprefix("What is")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    question = question.strip().split()

    if len(question) == 0:
         raise ValueError("syntax error") # "What is?"
        

    # Ensure no two numbers or operators appear consecutively in the parsed input
    for a, b in zip(question, question[1:]):
        if ((a in word_to_operator.keys() and b in word_to_operator.keys()) or
                (a.lstrip("-").isdigit() and b.lstrip("-").isdigit())): ## Python cannot handle negative numbers as isdigit()
            raise ValueError("syntax error")

    # Replace words with operators and numbers; check validity of operation
    translated_question = []
    for word in question:
        if word in word_to_operator:
            translated_question.append(word_to_operator[word])
        elif word.lstrip("-").isdigit():
            translated_question.append(word)
        else:
            raise ValueError("unknown operation")

    result = reduce(evaluate, translated_question, [0])
    if len(result) != 1:
        raise ValueError("syntax error") # "What is 1 plus?" --> ["1", "+"] -> 1
    return result[0]