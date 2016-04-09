# Uses python3
import sys

def gcd(a, b):
    '''
    Returns the greatest common divisor
    of two numbers, a & b
    '''
    assert (1 <= a <= 2*10**9)
    assert (1 <= b <= 2*10**9)
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
    '''
    Returns the least common multiple
    of two number a & b
    '''
    assert (1 <= a <= 2*10**9)
    assert (1 <= b <= 2*10**9)
    return (a*b) // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
