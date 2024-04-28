"""
Given the base code we have seen until now and that is also provided, implement a pop method

The pop method will remove the last element from the list and return the data it contains.
If the list is empty it should return None

To actually remove a variable (like a node) use del(variable)
"""

class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        # If list is empty return None
        if not self._head:
            return None

        # Find the last node and the one before that
        previous_node = None
        current_node = self._head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        # If node to be deleted is head, update head
        if self._head == current_node:
            self._head = None
        else:
            # If not, update previous node
            previous_node.next = None

        # Finally remove the node and return its value
        value = current_node.data
        del(current_node)
        return value