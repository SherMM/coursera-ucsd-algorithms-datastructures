# python3
import sys

def BWT(text):
    rotations = []
    items = list(text)
    for i in range(len(items)):
        r = ''.join(items[i:] + items[:i])
        rotations.append(r)
    rotations.sort()
    return ''.join(list(zip(*rotations))[-1])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
