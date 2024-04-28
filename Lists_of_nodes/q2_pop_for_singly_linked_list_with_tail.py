"""
Now the singly linked list has two pointers: a head pointer and a tail pointer.
Some things are easier and faster this way.
In this exercise you will implement again a pop method to the SinglyLinkedList class.

The pop methods will remove the last element/node from the list and return its value.
Same as before, if the list is empty, it should return None.
The method will update the head and tail properties accordingly.

"""

class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list

        Parameters: None

        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # If list is empty return None
        if not self._size:
            return None

        # Locate previous_node (the node just before last node)
        if self._size == 1:
            previous_node = None
        else:
            previous_node = self._head
            for _ in range(self._size-2):
                previous_node = previous_node.next

        # If head is also last node, then update head
        if self._head == self._tail:
            self._head = None
        else:
            previous_node.next = None

        # Save the content of the last node and remove it
        value = self._tail.data
        del(self._tail)

        # Update tail
        self._tail = previous_node

        # Finally update size and return the value of the removed node
        self._size -= 1
        return value
