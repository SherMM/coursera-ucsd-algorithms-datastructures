#Uses python3

import sys

sys.setrecursionlimit(200000)

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


def reverse_graph(graph):
    reverse = {i: [] for i in range(n)}
    for v, adj in graph.items():
        for u in adj:
            reverse[u].append(v)
    return reverse


def number_of_strongly_connected_components(graph):
    result = 0
    seen = set()

    def component_search(graph, vertex):
        seen.add(vertex)
        component = set()
        for v in graph[vertex]:
            if v not in seen:
                component.add(v)
                component_search(graph, v)
        return component

    order = toposort(reverse_graph(graph))
    comps = []
    for vertex in order:
        if vertex not in seen:
            c = component_search(graph, vertex)
            comps.append(c)
            result += 1
    return result, comps


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(graph)[0])
