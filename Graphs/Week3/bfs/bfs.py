#Uses python3

import sys
from collections import deque
def distance(graph, s, t, infinity=float("inf")):
    dists = [infinity for _ in range(len(graph))]
    queue = deque()
    queue.appendleft(s)
    dists[s] = 0
    while queue:
        curr = queue.pop()
        for node in graph[curr]:
            if dists[node] == infinity:
                queue.appendleft(node)
                dists[node] = dists[curr] + 1
    if dists[t] == infinity:
        return -1
    return dists[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(graph, s, t))
