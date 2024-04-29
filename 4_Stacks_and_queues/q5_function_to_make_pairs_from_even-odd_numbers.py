"""
Implement a function to make pairs of even-odd numbers
You have to implement a function called get_pairs that given a list of numbers, makes pairs with them.
Each pair consists in one even number and one odd number. The function will return a list containing all pairs as tuples.
You have to implement the function using queues. A Queue class, that offers enqueue and dequeue methods,
is already available for you to use.

The function will accept as parameter a (Python) list of integer numbers.
The function will return a (Python) list containing tuples.
Each tuple is a pair of even-odd numbers (first the even, then the odd number).
The pairs have to be formed in order: the first available even number with the first available odd number.

To implement this function create two queues and traverse the numbers list. For each number, check is it an even number
or an odd number,  and check if there is a pair available in the appropriate queue.
If there is, save the pair for the output. If not, enqueue it.

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

    def __len__(self):
        return self._size

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


def get_pairs(number_list):
    queues = (Queue(), Queue())
    pairs = []
    for number in number_list:
        this_type = number % 2
        other_type = (1, 0)[this_type]
        if len(queues[this_type]) == 0:
            other = queues[other_type].dequeue()
            if other is not None:
                pairs.append((other, number) if this_type else (number, other))
                continue
        queues[this_type].enqueue(number)
    return pairs


print(get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]))
# [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)]
print(get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]))
# [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)]