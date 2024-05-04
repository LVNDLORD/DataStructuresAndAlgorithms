"""
Implement a sift_down function
Given the information you have received about the sift_down function, implement it.

Given an array like: [6, 2, 5, 8, 1], and calling the sift_down function with the parameters "array, start=1, end=4"
(sink the node with the value of 1), the array should be modified to look like this: [6, 8, 5, 2, 1]

Remember that the left child on a zero based array is at position: 2*current_node_index+1 and
the right child is at: 2*current_node_index+2
"""


def sift_down(array, start, end):
    """
    Move the node at index 'start' down the heap until it satisfies the heap invariant

    Parameters:
    - array: The array representing the heap
    - start: The index of the node to be sifted down
    - end: The index of the last element in the heap (inclusive)

    Returns: Nothing. The array may be modified in-place.
    """
    root = start
    while True:
        child = 2 * root + 1  # Left child index
        if child > end:
            break

        # Find the larger child (or right child if it's larger)
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1

        # If the root is smaller than the largest child, swap them
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


arr = [6, 2, 5, 8, 1]
sift_down(arr, 1, 4)
print(arr)  # [6, 8, 5, 2, 1]
