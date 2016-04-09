# Uses python3
import sys
from array import array

def get_fibonacci_last_digit(n):
    '''
    Returns the last digit of the nth
    fibonacci number
    '''
    assert (0 <= n <= 10**7)
    if (n == 0): return 0
    if (n == 1): return 1
    
    lasts = array('l', [0]*(n+1))
    lasts[0] = 0
    lasts[1] = 1
    for i in range(2, n+1):
        lasts[i] = (lasts[i-1] + lasts[i-2]) % 10
    return lasts[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
