"""
Implement push and pop methods for a Stack structure
You will implement the push and pop methods for a stack. You will also implement a `__repr__()` method
to show the stack if necessary.

The push method will accept a value as parameter and adds a new node at the top of the stack with the given value.
The pointers and size should be updated accordingly. This method does not return anything.

The pop method will remove the top node from the stack and return its value. The pointers and size
should be updated accordingly. This method does not accept any parameters.
If the stack is empty, the method should return None.

The __repr__() method should return (not print) a string like this:

<Stack (3 elements): ['C', 'B', 'A']>
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        # Create the new node pointing to where top pointer is pointing
        node = Node(data, next=self._top)

        # Update top pointer and size
        self._top = node
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        if self._top is None:
            return None

        # Save the data temporary

        # Update top pointer and size, remove node and return its content
        node_to_remove = self._top
        self._top = self._top.next
        self._size -= 1
        data = node_to_remove.data
        del(node_to_remove)
        return data
