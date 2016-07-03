#Uses python3
import sys
import math
from collections import defaultdict

def minimum_distance(x, y):
    result = 0.
    #write your code here
    print(generate_graph_and_link_weights(list(zip(x,y))))
    return result

def generate_graph_and_link_weights(points):
    graph = defaultdict(list)
    weights = defaultdict(float)
    for i, (ix, iy) in enumerate(points):
        for j, (jx, jy) in enumerate(points[i:]):
            if (ix, iy) != (jx, jy):
                graph[(ix, iy)].append((jx, jy))
                graph[(jx, jy)].append((ix, iy))
                wght = distance(ix, jx, iy, jy)
                pt1, pt2 = (ix, iy), (jx, jy)
                weights[(pt1, pt2)] = wght
                weights[(pt2, pt1)] = wght
    return graph, weights

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
                                           
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
