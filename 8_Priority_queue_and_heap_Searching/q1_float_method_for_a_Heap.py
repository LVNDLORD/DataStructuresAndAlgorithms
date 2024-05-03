"""
Implement a float method for a Heap
Given the information you have received in the course about floating, implement a _float() method
that takes the last element of the heap and "float" it until the structure follow heap requirements.


Given a heap like: [3, 6, 5, 9, 7, 8, 2], the new heap would be: [2, 6, 3, 9, 7, 8, 5]
"""


class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        index = self._size - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]  # Swap
                index = parent_index
            else:
                break


h = Heap()
h._heap = [3, 6, 5, 9, 7, 8, 2]
h._size = 7
h._float()
print(h._heap)  # [2, 6, 3, 9, 7, 8, 5]
