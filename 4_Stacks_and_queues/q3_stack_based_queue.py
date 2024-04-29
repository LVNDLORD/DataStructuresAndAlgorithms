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

from q1_push_and_pop_for_stack_structure import Stack

class StackBasedQueue():
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
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

