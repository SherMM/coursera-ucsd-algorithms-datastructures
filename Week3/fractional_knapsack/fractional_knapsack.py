# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0 # value of items in bag
    weight = 0 # weight of items in bag
    vals = sorted(values)
    items = dict(zip(values, weights))
    best = values[-1]
    while items[best] + weight <= capacity:
        value += best
        weight += items[best]
        vals.pop()
        if not vals:
            break
        best = vals[-1]
        while items[best] + weight > capacity:
            vals.pop()
            if not vals:
                break
            best = vals[-1]
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
