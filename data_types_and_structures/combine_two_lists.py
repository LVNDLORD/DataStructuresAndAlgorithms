"""
Write a function named combine_lists that accepts two lists of integers as parameters.
Consider that the two lists are already sorted (The numbers are already in order from smallest to biggest number).
Your function should return a list that combines the two lists and at the same time is itself also sorted.
To be clear all elements of the input lists should be in the output list and
len(input_list1)+len(input_list2) == len(output_list).

You can use whatever you want as the name of the parameters. You don't need to use any special function or functionality
 to complete the task.

 Specially don't use any kind of sorting function of lists or Python in general.

 Just normal Python list actions are enough for this task. Iterate over the lists adding one by one the the smallest of
 the remaining elements of the two lists. When one of the lists have been exhausted, you can just add the remaining
 elements of the other list to the output list."
"""


def combine_lists(list1, list2):
    full_list = []
    index1, index2 = 0, 0

    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            full_list.append(list1[index1])
            index1 += 1
        else:
            full_list.append(list2[index2])
            index2 += 1

    while index1 < len(list1):
        full_list.append(list1[index1])
        index1 += 1

    while index2 < len(list2):
        full_list.append(list2[index2])
        index2 += 1

    return full_list


print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
