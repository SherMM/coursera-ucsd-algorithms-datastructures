#Uses python3

import sys


def acyclic(graph):
    stack = set()
    seen = set()

    def visit(vertex):
        if vertex in seen:
            return 0
        seen.add(vertex)
        stack.add(vertex)
        for adj in graph.get(vertex, []):
            if adj in stack or visit(adj):
                return 1
        stack.remove(vertex)
        return 0
    
    for vertex in graph:
        if visit(vertex):
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a - 1].append(b - 1)
    print(acyclic(graph))
