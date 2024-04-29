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

from q4_Node_based_queue import Queue


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
