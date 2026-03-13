class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
       
        i = self._size - 1   # index of last element

        while i > 0:
            parent = (i - 1) // 2

            if self._heap[i] < self._heap[parent]:
               
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
                i = parent
            else:
                break