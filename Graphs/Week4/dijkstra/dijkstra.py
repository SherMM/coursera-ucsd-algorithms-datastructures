#Uses python3

import sys
import queue


def distance(graph, cost, s, t, infinity=float("inf")):
    
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    graph = {i: [] for i in range(n)}
    cost = {}
    for ((a, b), w) in edges:
        graph[a - 1].append(b - 1)
        cost[(a-1, b-1)] = w
    s, t = data[0] - 1, data[1] - 1
    print(graph)
    print(cost)
    print(distance(graph, cost, s, t))
