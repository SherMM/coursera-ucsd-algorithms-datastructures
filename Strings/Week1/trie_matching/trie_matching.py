# python3
import sys

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i in range(len(text)):
        res = prefix_trie_matching(text[i:], trie)
        if res:
            result.append(i)
    return result


def prefix_trie_matching(text, trie):
    pattern = []
    idx, root = 0, 0
    sym = text[idx]
    v = root
    while True:
        if len(trie[v]) == 0:
            return ''.join(pattern)
        elif sym in trie[v] and idx < len(text):
            pattern.append(sym)
            v = trie[v][sym]
            idx += 1
            if idx < len(text):
                sym = text[idx]
        else:
            return None


def build_trie(patterns):
    tree = dict()
    root, index = 0, 0
    tree[index] = dict()
    for patt in patterns:
        curr_node = root
        for i in range(len(patt)):
            sym = patt[i]
            if sym in tree[curr_node]:
                curr_node = tree[curr_node][sym]
            else:
                tree[index + 1] = dict()
                tree[curr_node][sym] = index + 1
                curr_node = index + 1
                index += 1
    return tree

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
