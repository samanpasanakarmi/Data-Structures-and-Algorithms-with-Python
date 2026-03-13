class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
     
        index = self._size - 1
        parent_index = (index - 1) // 2

        while index > 0 and self._heap[index] < self._heap[parent_index]:
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, value):
        self._heap.append(value)
        self._size += 1
        self._float()

    def _sink(self):
       
        index = 0

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < self._size and self._heap[left] < self._heap[smallest]:
                smallest = left

            if right < self._size and self._heap[right] < self._heap[smallest]:
                smallest = right

            if smallest != index:
                self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
                index = smallest
            else:
                break


h = Heap()
h._heap = [8, 6, 5, 9, 7]
h._size = 5
h._sink()
print(h._heap)