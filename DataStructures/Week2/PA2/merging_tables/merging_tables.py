# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    return parent[table]

def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return False
    lines[realDestination] += lines[realSource]
    lines[realSource] = 0
    parent[realSource] = realDestination
    ans = max(lines)
    return True

for i in range(m):
    #print(parent)
    #print(lines)
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
