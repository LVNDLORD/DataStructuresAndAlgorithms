"""
Implement a Stack based Queue
You have to implement a stack based queue called "StackBasedQueue". A Stack class is already available.
The class is already defined and you have to complete the requested methods. Notice that a "__repr__()"
function is already provided so the exercise can be tested. This function forces you to use certain names
for the internal properties: self._size, self._InboundStack and self._OutboundStack.
You can also use whatever you prefer and rename the variables in the provided method.

The class should use two stacks as explained in the theory. The enqueue method will push to the Inbound stack and the
dequeue method will pop from the Outbound stack. But if the Outbound stack is empty, it will try first to transfer
all available elements from Inbound stack to Outbound stack.
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
        del (node_to_remove)
        return data


class StackBasedQueue():
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = []

        # Iterate over InboundStack
        current = self._InboundStack._top
        while current:
            values.append(str(current.data))
            current = current.next

        # Iterate over OutboundStack
        current = self._OutboundStack._top
        while current:
            values.append(str(current.data))
            current = current.next

        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        # Push the data to the Inbound Stack
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None

        if len(self._OutboundStack) == 0:
            # If Outbound Stack is empty, transfer whatever is in the Inbound Stack
            while data := self._InboundStack.pop():
                self._OutboundStack.push(data)

        # Return the pop of Outbound Stack
        self._size -= 1
        return self._OutboundStack.pop()


queue = StackBasedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
val = queue.dequeue()
print(val, queue)  # A <StackBasedQueue (2 elements): [B, C]>
