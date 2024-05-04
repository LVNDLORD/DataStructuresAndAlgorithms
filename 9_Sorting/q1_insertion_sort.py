"""
Implement an Insertion sort function
Given the information you have received in the course about the Insertion sort algorithm,
implement a function that uses it. The function needs only to accept the array to be sorted as parameter.
The function returns nothing. The array is sorted in-place.

Given an array like: [6, 8, 5, 1, 2], the sorted array would be: [1, 2, 5, 6, 8]
"""


def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(arr)
print(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]