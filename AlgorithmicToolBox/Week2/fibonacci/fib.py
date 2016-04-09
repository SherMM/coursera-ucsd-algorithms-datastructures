# Uses python3
from array import array

def calc_fib(n):
    '''
    Returns the nth fibonacci number
    '''
    assert (0 <= n <= 45)
    if (n == 0): return 0
    if (n == 1): return 1

    fibs = array('l', [0]*(n+1))
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]

n = int(input())
print(calc_fib(n))
