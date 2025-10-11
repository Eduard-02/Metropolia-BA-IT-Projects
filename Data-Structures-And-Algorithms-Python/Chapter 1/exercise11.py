# Exercise

# Write a function named combine_lists that accepts two lists of integers as parameters.
# Consider that the two lists are already sorted
# (The numbers are already in order from smallest to biggest number).
# Your function should return a list that combines the two lists and
# at the same time is itself also sorted.
# To be clear all elements of the input lists should be in the output list and
# len(input_list1)+len(input_list2) == len(output_list).
# Notice that your function should return the list, not print it.

def combine_lists(fst_list, snd_list):
    final_list = []
    j = 0
    i = 0
    while i < len(fst_list) and j < len(snd_list):
        if fst_list[i] < snd_list[j]:
            final_list.append(fst_list[i])
            i += 1
        else:
            final_list.append(snd_list[j])
            j += 1
    if i < len(fst_list):
        final_list.extend(fst_list[i:])
    elif j < len(snd_list):
        final_list.extend(snd_list[j:])
    return final_list