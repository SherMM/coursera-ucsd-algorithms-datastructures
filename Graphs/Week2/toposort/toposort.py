#Uses python3

import sys

def dfs_post(graph):
    '''
    Performs dfs and returns 
    post order of visited nodes
    '''
    post = []
    seen = set()
    
    def dfs(graph, vertex):
        seen.add(vertex)
        for v in graph[vertex]:
            if v not in seen:
                dfs(graph, v)
        post.append(vertex)

    for vertex in graph:
        if vertex not in seen:
            dfs(graph, vertex)
    return post


def toposort(graph):
    order = dfs_post(graph) 
    return order[::-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a - 1].append(b - 1)
    order = toposort(graph)
    for x in order:
        print(x + 1, end=' ')
    print()
