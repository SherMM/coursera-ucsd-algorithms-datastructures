# Uses python3
import sys

def optimal_summands(n):
    summands = set()
    if n == 1:
        return set([1])
    m = n
    start = 1
    while m-start not in summands and m-start > 0 and m-start != start:
        summands.add(start)
        m -= start
        start += 1
    summands.add(m)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
