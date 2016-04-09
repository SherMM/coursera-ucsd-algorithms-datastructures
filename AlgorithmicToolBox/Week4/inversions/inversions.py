# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions

    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a, b, left, ave, right)
    return number_of_inversions


def merge(a, b, low, mid, high):
    count = 0
    i, j = low, mid
    k = 0
    while i < mid and j < high:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            count += (mid - i)
            b[k] = a[j]
            j += 1
        k += 1

    # handle remaining elements
    if i < mid:
        b[k: k+(mid-i)] = a[i: mid]
    else:
        b[k: k+(high-j)] = a[j: high]
    # update a
    a[low: high] = b[:(high-low)]
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
