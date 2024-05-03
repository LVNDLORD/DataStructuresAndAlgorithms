"""
Implement an Interpolation search function
Write a function that implements an interpolation search in a given array.
The function accepts as parameters the array where to perform the search and the value being searched.
The function returns the index of the value being searched, if it is found or None if it is not found.
The function can accept more parameters but they must not be mandatory.
The user only needs to pass the array and the value. You are free to implement an iterative or recursive algorithm.

The algorithm is almost the same than Binary search algorithm. Take into account that in this algorithm the calculated
midpoint is not always within the limits of the search area.
"""


def interpolation_search(array, value):
    """
    Performs an Interpolation search in the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    # Define the start and end indices
    low = 0
    high = len(array) - 1

    while low <= high and array[low] <= value <= array[high]:
        # Calculate the approximate position of the value in the array
        pos = low + ((value - array[low]) * (high - low) // (array[high] - array[low]))

        if array[pos] == value:
            return pos
        elif array[pos] < value:
            low = pos + 1
        else:
            high = pos - 1

    return None


arr = [1, 2, 3]
print(interpolation_search(arr, 2))  # 1
