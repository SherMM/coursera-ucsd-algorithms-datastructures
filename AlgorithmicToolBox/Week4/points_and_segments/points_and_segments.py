# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    l = [(s, 'l', None) for s in starts]
    r = [(e, 'r', None) for e in ends]
    p = [(pt, 'p', i) for i, pt in enumerate(points)]
    total = l + r + p
    total.sort()

    num_seen = 0
    for val, key, index in total:
        if key == 'l':
            num_seen += 1
        elif key == 'r':
            num_seen -= 1
        else:
            cnt[index] += num_seen
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
    print()
