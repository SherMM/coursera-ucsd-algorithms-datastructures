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
    patterns = []
    idx, root = 0, 0
    sym = text[idx]
    v = root
    while True:
        if len(trie[v]) == 0:
            return patterns
        elif sym in trie[v] and idx < len(text):
            patterns.append(sym)
            v, is_end_patt = trie[v][sym]
            if is_end_patt:
                return patterns
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
                curr_node, is_end_patt = tree[curr_node][sym]
            else:
                tree[index + 1] = dict()
                if i == len(patt) - 1:
                    data = (index + 1, True)
                else:
                    data = (index + 1, False)
                tree[curr_node][sym] = data
                curr_node = index + 1
                index += 1
    return tree


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

patterns.sort()

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
