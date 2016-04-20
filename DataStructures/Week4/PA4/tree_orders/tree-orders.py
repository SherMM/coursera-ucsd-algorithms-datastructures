# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        root = 0 # index of root
        stack = []
        done = False
        while not done:
            if root != -1:
                # traverse to leftmost node
                stack.append(root)
                root = self.left[root]
            else:
                if len(stack) > 0:
                    root = stack.pop()
                    self.result.append(self.key[root])
                    root = self.right[root]
                else:
                    done = True
        return self.result

    def preOrder(self):
        self.result = []
        root = 0 # index of root
        stack = [root]
        while len(stack) != 0:
            curr = stack.pop()
            self.result.append(self.key[curr])
            if self.right[curr] != -1:
                stack.append(self.right[curr])
            if self.left[curr] != -1:
                stack.append(self.left[curr])
        return self.result

    def postOrder(self):
        self.result = []
        root = 0 # index of root
        stack1 = [root]
        stack2 = []
        while len(stack1) > 0:
            curr = stack1.pop()
            stack2.append(curr)

            if self.left[curr] != -1:
                stack1.append(self.left[curr])
            if self.right[curr] != -1:
                stack1.append(self.right[curr])

        while len(stack2) > 0:
            curr = stack2.pop()
            self.result.append(self.key[curr])
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
