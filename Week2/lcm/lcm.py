# Uses python3
import sys

def gcd(a, b):
    '''
    Returns the greatest common divisor
    of two numbers, a & b
    '''
    # simulate denominator and numerator
    d = b
    n = a
    while d != 0:
        # get remainder
        rem = n % d
        # swap numerator and denominator
        n = d
        d = rem
    return n

def lcm(a, b):
    #write your code here
    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
