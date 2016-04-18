# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    if rank[realDestination] > rank[realSource]:
        # merge source into destination table
        lines[realDestination] += lines[realSource]
        lines[realDestination] = 0
        parent[realSource] = realDestination
    else:
        # merge destination into source table
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        parent[realDestination] = realSource
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
