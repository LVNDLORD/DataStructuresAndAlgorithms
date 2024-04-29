"""
mplement a Node based Queue
You have to implement a Queue class called Queue that uses the ListNode class to store the data.
ListNode class is already available.

Queue class should implement a __init__() method that initialize internal variables/properties.
It also has to implement the enqueue and dequeue methods. These methods are very similar (if not the same)
 that some of the methods already available in the DoublyLinkedList class. So it can be of help to get these two methods.
 Finally a __repr__() method should be implemented. After enqueuing 'A', 'B' and 'C' (in this order),
 it should show a text like this:

<Queue (3 elements): [C, B, A]>
Notice that it shows the newer elements at the left and the older elements at the right. So it is a line where
new elements come from the left and the old elements come out from the right.
"""


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self._front = self._rear = None
        self._size = 0

    def __repr__(self):
        current_node = self._rear
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.prev
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def enqueue(self, data):
        new_node = ListNode(data)
        if self._rear is None:
            self._front = self._rear = new_node
        else:
            new_node.prev = self._rear
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        if self._front is None:
            return None
        data = self._front.data
        if self._front.next is None:
            self._front = self._rear = None
        else:
            self._front = self._front.next
            self._front.prev = None
        self._size -= 1
        return data



queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
print(val, queue)