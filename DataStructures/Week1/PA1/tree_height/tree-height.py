# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeHeight:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.length = [0 for i in range(self.n)]

    def height(self, node, length):
        # already handled
        if self.length[node] != 0:
            return

        # handle root node
        if self.parent[node] == -1:
            self.length[node] = 1
            return

        # move to parent and continue
        if self.length[self.parent[node]] == 0:
            self.height(self.parent[node], self.length)

        # update height
        self.length[node] = self.length[self.parent[node]] + 1

    def compute_height(self):
        # Replace this code with a faster implementation
        n = len(self.parent)
        for i in range(n):
            self.height(i, self.length)

        best = self.length[0]
        for i in range(1, n):
            best = max(best, self.length[i])
        return best


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
