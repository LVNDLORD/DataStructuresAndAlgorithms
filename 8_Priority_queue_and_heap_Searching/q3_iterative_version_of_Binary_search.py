"""
Implement an iterative version of the Binary search
Write a function that implements an iterative version of the binary search. The function accepts two parameters,
the array in question and the value being searched. The function returns the index of the value if
it's found or None if not found in the array.

Use two pointers/variables to limit the search area and update them adequately.
Loop while the search area is big enough to hold at least one element inside it.
Other than that, it is quite similar than the recursive version.
"""


def binary_search_iterative(array, value):
    """
    Performs a binary search in the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return None


arr = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]
print(binary_search_iterative(arr, 0))  # 0
print(binary_search_iterative(arr, 98))  # 19
print(binary_search_iterative(arr, 29))  # 6
print(binary_search_iterative(arr, 100))  # None
print(binary_search_iterative(arr, -1))  # None
print(binary_search_iterative(arr, 44))  # None
