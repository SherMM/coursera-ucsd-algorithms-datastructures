#Uses python3

import sys
from collections import deque


def negative_cycle(graph, cost):
    for node in graph:
        is_cycle = has_cycle(graph, cost, node)
        if is_cycle:
            return 1
    return 0



def has_cycle(graph, cost, s, infinity=float("inf")):
    dists, prev, count, seen = [], [], [], []
    for _ in range(len(graph)):
        dists.append(infinity)
        prev.append(None)
        count.append(0)
        seen.append(False)
    dists[s] = 0
    seen[s] = True
    
    queue = deque()
    queue.appendleft(s)
    while queue:
        curr = queue.pop()
        seen[curr] = False
        count[curr] += 1

        # cycle detected
        if count[curr] >= len(graph):
            return 1

        for node in graph[curr]:
            if dists[node] > dists[curr] + cost[(curr, node)]:
                dists[node] = dists[curr] + cost[(curr, node)]
                prev[node] = curr
                if not seen[node]:
                    queue.appendleft(node)
                    seen[node] = True
    return 0


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
    print(negative_cycle(graph, cost))
