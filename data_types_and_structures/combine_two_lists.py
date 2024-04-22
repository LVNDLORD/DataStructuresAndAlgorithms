
def combine_lists(list1, list2):
    complete_list = sorted(list1 + list2)
    return complete_list


print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
