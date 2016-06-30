#Uses python3

import sys
from collections import deque

def bipartite(graph, infinity=float("inf")):
    dists = [infinity for _ in range(len(graph))]
    queue = deque()
    for node in graph:
        if dists[node] == infinity:
            dists[node] = 0
            queue.appendleft(node)
            while queue:
                curr = queue.pop()
                for adj in graph[curr]:
                    if dists[adj] == infinity:
                        dists[adj] = dists[curr] + 1
                        queue.appendleft(adj)
                    elif dists[adj] == dists[curr]:
                        return 0
    return 1

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
    print(bipartite(graph))
