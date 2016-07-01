#Uses python3

import sys
import heapq as hp


def distance(graph, cost, s, t, infinity=float("inf")):
    dists, prev, verts = [], [], []
    for i in range(len(graph)):
        dists.append(infinity)
        prev.append(None)
        verts.append(i)
    dists[s] = 0
    queue = list(zip(dists, verts))
    hp.heapify(queue)
    while queue:
        d, u = hp.heappop(queue)
        for node in graph[u]:
            w = cost[(u, node)]
            if dists[node] > d + w:
                dists[node] = d + w
                prev[node] = u
                change_priority(queue, node, dists[node])
    if dists[t] == infinity:
        return -1
    return dists[t]


def change_priority(queue, node, d):
    for i, (dist, vert) in enumerate(queue):
        if vert == node:
            queue[i] = (d, node)
            break
    hp.heapify(queue)


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
    print(distance(graph, cost, s, t))
