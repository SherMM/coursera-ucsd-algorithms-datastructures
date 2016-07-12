#Uses python3
import sys
import math
import heapq as hp
from collections import defaultdict
from random import choice

def minimum_distance(x, y):
    graph, weights = generate_graph_and_link_weights(list(zip(x, y)))
    return prim(graph, weights)
    #return kruskal(graph, weights)

def generate_graph_and_link_weights(points):
    graph = defaultdict(list)
    weights = defaultdict(float)
    if len(points) == 1:
        graph[points[0]].append(None)
    for i, (ix, iy) in enumerate(points):
        for j, (jx, jy) in enumerate(points[i+1:]):
            graph[(ix, iy)].append((jx, jy))
            graph[(jx, jy)].append((ix, iy))
            pt1, pt2 = (ix, iy), (jx, jy)
            wght = distance(pt1, pt2)
            weights[(pt1, pt2)] = wght
            weights[(pt2, pt1)] = wght
    return graph, weights


def prim(graph, weights, infinity=float("inf")):
    # one point in graph
    if len(graph) == 1:
        return 0
    cost = dict()
    for node in graph:
        cost[node] = infinity
    
    start = choice(list(graph.keys()))
    cost[start] = 0
    queue = []
    # add vertexes and costs to queue
    for node, c in cost.items():
        hp.heappush(queue, (c, node))
    
    total = 0
    seen = set() 
    processed = set()
    while queue:
        c, head = hp.heappop(queue)
        if head not in processed:
            processed.add(head)
            seen.add(head)
            total += c
            for tail in graph[head]:
                if tail not in seen and weights[(head, tail)] < cost[tail]:
                    cost[tail] = weights[(head, tail)]
                    #index = priority_index(queue, tail)
                    #queue[index] = (cost[tail], tail)
                    #hp.heapify(queue)
                    hp.heappush(queue, (cost[tail], tail))
    return total


def kruskal(graph, weights):
    sets = dict()
    for node in graph:
        sets[node] = set([node])

    mst = set()
    edges = sorted(weights.items(), key=lambda x: x[1])
    for (head, tail), cost in edges:
        if (tail, head) not in mst:
            # separate sets, so know they need union
            head_set = find_set(sets, head)
            tail_set = find_set(sets, tail)
            if head_set != tail_set:
                sets[head_set] = sets[head_set].union(sets[tail_set])
                del sets[tail_set]
                mst.add((head, tail))
    
    total = 0
    for edge in mst:
        total += weights[edge]
    return total

def find_set(sets, node):
    for vert, group in sets.items():
        if node in group:
            return vert
    return None

               

def priority_index(queue, node):
    for i, (c, vertex) in enumerate(queue):
        if vertex == node:
            return i

def distance(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
         

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
