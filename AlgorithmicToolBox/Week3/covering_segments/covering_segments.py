# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    curr = None
    segments.sort(key=lambda x: x[1])
    for s in segments:
        if curr is None:
            curr = s.end
        if not (s.start <= curr <= s.end):
            points.append(curr)
            curr = s.end
    points.append(curr)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
    print()
