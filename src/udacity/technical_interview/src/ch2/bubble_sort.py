"""

Best: O(n)
Average: O(n^2)
Worst: O(n^2)

Spacecd : O(n)


"""


def bubble_sort(a_list):
    for passnum in range(len(a_list) - 1, 0, -1):
        for i in range(passnum):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list



alist = [54,26,93,17,77,31,44,55,20]
sorted_list = bubble_sort(alist)
print(sorted_list)
