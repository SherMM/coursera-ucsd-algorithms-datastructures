import sys

def isInRange(number, low, high):
    '''
    Returns true if number is in between
    low and high
    '''
    return number >= low and number <= high

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
if isInRange(a, 0, 9) and isInRange(b, 0, 9):
    print(a + b)
