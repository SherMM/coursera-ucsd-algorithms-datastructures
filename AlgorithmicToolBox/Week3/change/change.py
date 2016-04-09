# Uses python3
import sys

def get_change(n):
    '''
    Returns minimum number of 1, 5, 10 denomination
    coins to make change for n
    '''
    assert (1 <= n <= 10**3)
    total = n
    count = 0
    while total != 0:
        if total >= 10:
            count += total // 10
            total %= 10
        elif total >= 5:
            count += total // 5
            total %= 5
        else:
            count += total // 1
            total %= 1
    return count

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
