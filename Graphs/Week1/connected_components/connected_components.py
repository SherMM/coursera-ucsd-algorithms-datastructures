#Uses python3

import sys


def number_of_components(graph):
    result = 0
    seen = set()
    for vertex in graph:
        if vertex not in seen:
            stack = [vertex]
            result += 1
            while stack:
                curr = stack.pop()
                if curr not in seen:
                    seen.add(curr)
                    stack.extend(graph[curr])
    return result

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
    print(number_of_components(graph))
