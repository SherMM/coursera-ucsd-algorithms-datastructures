# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, M, m, ops):
    min_val = float("inf")
    max_val = float("-inf")
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(m[i][k], m[k+1][j], ops[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(dataset):
    vals = []
    ops = []
    valid_ops = set(['+', '-', '*'])
    # get numbers and operations
    for item in dataset:
        if item in valid_ops:
            ops.append(item)
        else:
            vals.append(int(item))

    # need number of digits to get matrix dimension
    n = len(vals)
    M = [[0 for i in range(n)] for j in range(n)]
    m = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        m[i][i] = vals[i]
        M[i][i] = vals[i]

    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, M, m, ops)
    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
