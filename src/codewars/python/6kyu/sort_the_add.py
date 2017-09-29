"""

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


"""

from collections import OrderedDict


def sort_array(source_array):
    # If the source_array is empty return empty list
    if not source_array:
        return source_array

    result_list = []
    even_pos_dict = OrderedDict()

    for i, n in enumerate(source_array):
        if n % 2 == 0:
            even_pos_dict[i] = n
        else:
            result_list.append(n)

    if result_list:
        result_list = sorted(result_list)

    if even_pos_dict:
        for pos, n in even_pos_dict.items():
            result_list.insert(pos, n)

    return result_list


if __name__ == '__main__':
    # print(sort_array([5, 3, 2, 8, 1, 4]))
    print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
