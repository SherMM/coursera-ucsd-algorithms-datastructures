#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
