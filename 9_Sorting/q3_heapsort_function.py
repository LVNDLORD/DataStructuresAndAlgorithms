"""
Implement a heapsort function
Given the information you have received in the course about the heapsort algorithm,
implement a sort function that uses it. The function needs only to accept the array to be sorted as parameter.
Use the sift_down helper function to complete the task (it is available even if it is not visible)

Given an array like: [6, 8, 5, 1, 2], the sorted array would be: [1, 2, 5, 6, 8]
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


def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    n = len(array)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n - 1)

    # Heap sort
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i - 1)


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heap_sort(arr)
print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
