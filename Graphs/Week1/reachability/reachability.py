#Uses python3

import sys

def reach(graph, x, y):
    is_reachable = 0
    seen = set()
    stack = [x]
    while stack:
        curr = stack.pop()
        if curr == y:
            is_reachable = 1
            break
        if curr not in seen:
            seen.add(curr)
            stack.extend(graph[curr])
    return is_reachable

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    #adj = [[] for _ in range(n)]
    graph = {i: [] for i in range(n)}
    x, y = x - 1, y - 1
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    print(reach(graph, x, y))
