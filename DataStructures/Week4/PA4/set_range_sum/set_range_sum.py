# python3

from sys import stdin
from collections import deque
# Splay tree implementation

# Vertex of a splay tree
class Vertex:

    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right,
         self.parent) = (key, sum, left, right, parent)


def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + \
        (v.right.sum if v.right != None else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v


def smallRotation(v):
    # zig
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.


def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            # zig case
            smallRotation(v)
        else:
            # all others
            bigRotation(v)
    return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.


def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    result, root = find(root, key)
    if result == None:
        return (root, None)
    root = splay(result)
    right_subt = root.right
    left_subt = root.left
    # result key will be >= search key
    # (result == None -> case already handled)
    if left_subt:
        left_subt.parent = None
        root.left = None
        update(root)
    return left_subt, root


def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    # find biggest node in left subtree
    result, v = find(left, find_max_key(left))
    v = splay(result)
    v.right = right
    update(v)
    return v


def find_max_key(root):
    v = root
    while v.right:
        if v.right.key > v.key:
            v = v.right
    return v.key

# Code that uses splay tree to solve the problem

root = None

def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)

def erase(x):
    global root
    if root == None:
        # empty tree
        return
    if root.key == x and (root.left == None and root.right == None):
        # one node (only a root)
        root = None
        return
    result, root = find(root, x)
    if result and result.key == x:
        # item x was found
        successor = find_successor(result)
        root = splay(successor)
        # splay the node we want to remove to top
        root = splay(result)
        # get subtrees
        lsub = root.left
        rsub = root.right
        if rsub:
            root = None
            rsub.parent = None
            root = rsub
            root.left = lsub
            update(root)
        else:
            root = None
            lsub.parent = None
            root = lsub
            update(root)

def find_successor(node):
    successor = node.right
    if successor:
        while successor.left:
            successor = successor.left
    else:
        successor = node.parent
    return successor


def search(x):
    global root
    result, root = find(root, x)
    if result and result.key == x:
        return True
    return False


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    # sum elements in middle tree
    ans = 0
    if middle:
        ans = middle.sum
    # merge tree back together
    sub = merge(left, middle)
    root = merge(sub, right)
    return ans

def splayprint(root):
    v = root
    if v:
        nodes = []
        nodes.append(v)
        while len(nodes) > 0:
            e = nodes.pop(0)
            print(e.key if e is not None else "-")
            print(e.left.key if e.left is not None else "-",
                  e.right.key if e.right is not None else "-")
            if e.left is not None:
                nodes.append(e.left)
            if e.right is not None:
                nodes.append(e.right)
    else:
        print(None)

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) %
                  MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
