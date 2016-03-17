# Uses python3
import sys
import random


def partition3(a, l, r):

    print("Left: " + str(l) + " Right: " + str(r))
    sub = a[l: r + 1]
    x = sub[0]
    print("pivot")
    print(x)

    low = [v for v in sub if v < x]
    equal = [v for v in sub if v == x]
    high = [v for v in sub if v > x]

    lt = len(low)
    gt = lt + len(equal)-1

    equal.extend(high)
    low.extend(equal)
    a[l: r + 1] = low

    return lt, gt


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    lt, gt = partition3(a, l, r)
    print("Low")
    print(a[l: lt])
    print("Equal")
    print(a[lt: gt+1])
    print("High")
    print(a[gt + 1: r + 1])
    print("A")
    print(a)
    randomized_quick_sort(a, l, lt - 1)
    randomized_quick_sort(a, gt + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print("Original")
    print(a)
    #randomized_quick_sort(a, 0, n - 1)
    '''
    for x in a:
        print(x, end=' ')
    print()
    '''

    print(partition3(a, 0, 21))
    print(a)
