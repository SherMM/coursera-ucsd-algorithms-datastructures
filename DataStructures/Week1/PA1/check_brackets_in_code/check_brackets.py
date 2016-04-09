# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    index = None
    for i, next in enumerate(text):
        #print(i, next)
        bracket = Bracket(next, i+1)
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket
            opening_brackets_stack.append(bracket)
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket
            if len(opening_brackets_stack) == 0:
                index = i+1
                break
            top = opening_brackets_stack.pop()
            if not top.Match(next):
                index = i+1
                break
    # Printing answer
    if index:
        print(index)
    elif len(opening_brackets_stack) != 0:
        index = opening_brackets_stack.pop().position
        print(index)
    else:
        print("Success")
