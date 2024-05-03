"""
Implement a sink method for a Heap
Given the information you have received in the course about extraction and sink, implement a _sink() method that sinks the Root node value if necessary.

Given a heap like: [8, 6, 5, 9, 7], the new heap would be: [5, 6, 8, 9, 7]

"""


class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index - 1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        index = 0
        # While node has at least one child
        while index * 2 + 1 < self._size:
            if index * 2 + 2 < self._size:
                # If two children
                child_index = min(index * 2 + 1, index * 2 + 2, key=lambda x: self._heap[x])
            else:
                # If only one child
                child_index = index * 2 + 1
            # Swap values if parent is bigger than child
            if self._heap[index] > self._heap[child_index]:
                self._heap[index], self._heap[child_index] = self._heap[child_index], self._heap[index]  # Swap
                index = child_index
            else:
                break


h = Heap()
h._heap = [8, 6, 5, 9, 7]
h._size = 5
h._sink()
print(h._heap)  # [5, 6, 8, 9, 7]
