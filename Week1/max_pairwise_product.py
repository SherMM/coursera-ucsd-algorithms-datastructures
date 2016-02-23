n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a.sort(reverse=True)
result = a[0]*a[1]

print(result)
