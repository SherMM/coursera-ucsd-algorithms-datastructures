# python3


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def Size(self):
        return len(self._data)

    def Parent(self, i):
        return (i - 1) // 2

    def LeftChild(self, i):
        return 2 * i + 1

    def RightChild(self, i):
        return 2 * i + 2

    def Swap(self, i, j):
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp

    def SiftUp(self, i):
        while i > 0 and self._data[self.Parent(i)] > self._data[i]:
            self._swaps.append((self.Parent(i), i))
            self.Swap(self.Parent(i), i)
            i = self.Parent(i)

    def SiftDown(self, i):
        maxIdx = i
        left = self.LeftChild(i)
        if left < self.Size() and self._data[left] < self._data[maxIdx]:
            maxIdx = left
        right = self.RightChild(i)
        if right < self.Size() and self._data[right] < self._data[maxIdx]:
            maxIdx = right
        if i != maxIdx:
            self._swaps.append((i, maxIdx))
            self.Swap(i, maxIdx)
            self.SiftDown(maxIdx)

    def BuildHeap(self):
        n = self.Size() // 2
        for i in range(n, -1, -1):
            self.SiftDown(i)

    def GenerateSwaps(self):
        self.BuildHeap()

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
