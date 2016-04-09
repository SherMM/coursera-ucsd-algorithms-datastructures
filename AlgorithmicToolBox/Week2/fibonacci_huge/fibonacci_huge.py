# Uses python3
import sys
from array import array

def get_fibonaccihuge(n, m):
    '''
    Returns nth fibo number mod m
    '''
    if n == 0: return 0
    if n == 1: return 1

    # we know pisano sequence starts with 0,1
    pisano = [0, 1]
    for i in range(2, n+1):
        one = (pisano[i-1] + pisano[i-2]) % m
        two = (one + pisano[i-1]) % m
        # pisano sequence has restarted, end iteration
        if (one == 0 and two == 1):
            # calculate index in pisano to return
            k = (n // len(pisano))*len(pisano)
            return pisano[n - k]
        pisano.append(one)
    return pisano[n]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
