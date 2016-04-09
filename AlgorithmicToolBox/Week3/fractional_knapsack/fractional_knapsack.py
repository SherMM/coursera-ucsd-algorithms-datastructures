# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0 # value of items in bag
    weight = 0 # weight of items in bag
    items = {v/w: (v,w) for v,w in zip(values, weights)}
    while weight != capacity and items:
        best = max(items)
        item_weight = items[best][1]
        item_value = items[best][0]
        if item_weight + weight <= capacity:
            weight += item_weight
            value += item_value
        else:
            diff = capacity - weight
            frac = diff*best
            weight += diff
            value += frac
        del items[best]
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
