class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Add an item to the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the last item
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def size(self):
        return len(self.items)  # Return the number of items in the stack


def is_paired(input_string):
    
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    stack = Stack()
    
    for item in input_string:
        if item in "[({":
            stack.push(item)

        if item in "]})":
            if stack.pop() != matching_parentheses[item]:
                return False

    return stack.is_empty()            





    
    
