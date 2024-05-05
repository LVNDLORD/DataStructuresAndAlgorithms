"""
Given the information you have received about Dynamic programming and Tabulation, implement a function called fib()
to solve the Fibonacci series with this technique. The function should accept the value for which we should calculate
the Fibonacci series. The function should return the calculated value of this series.

Function should be implemented with Tabulation. That means that it does not use recursion, but instead iterate from 0
 to n and calculate the value of the Fibonacci series for that step. Loop should remember the last two steps values,
 so it doesn't need to calculate them.
"""


def fib(n):
    """
    Calculate the Fibonacci's series value for integer n

    Parameters:
    - n: The number to use in the Fibonacci's series.

    Returns: The calculated value of the Fibonacci's series for n
    """
    if n <= 1:
        return 1

    # Initialize an array to store Fibonacci numbers
    fib_values = [1, 1]

    # Iterate from 2 to n, calculating Fibonacci numbers
    for i in range(2, n + 1):
        fib_values.append(fib_values[-1] + fib_values[-2])

    return fib_values[n]


print(fib(10)) # 89
