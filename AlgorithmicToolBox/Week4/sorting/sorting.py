# Uses python3
import sys
import random


def partition3(a, l, r):

    sub = a[l: r + 1]
    x = sub[0]

    low = [v for v in sub if v < x]
    equal = [v for v in sub if v == x]
    high = [v for v in sub if v > x]

    lt = l + len(low)
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
    randomized_quick_sort(a, l, lt - 1)
    randomized_quick_sort(a, gt + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    print()
