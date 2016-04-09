# Uses python3
import sys


def optimal_weight(size, items):
    sack = [[0 for j in range(size + 1)] for i in range(2)]
    row = [0 for j in range(size+1)]
    counter = 1
    while counter < len(items)+1:
        for x in range(size+1):
            wght = items[counter-1]
            val = wght
            if wght > x:
                sack[1][x] = sack[0][x]
            else:
                sack[1][x] = max(sack[0][x], sack[0][x-wght] + val)
        counter += 1
        sack[0] = sack[1]
        sack[1] = row[:]
    return sack[0][size]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
