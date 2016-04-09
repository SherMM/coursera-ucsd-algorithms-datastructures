# Uses python3
import sys

def get_majority_element(a, left, right):
    majority = (right - left) // 2
    ints = dict()
    for val in a:
        ints[val] = ints.get(val, 0) + 1

    for val in ints:
        if ints[val] > majority:
            return val
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
