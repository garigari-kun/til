"""

Running time: O(nlogn)
Space: O(n)


"""


def merge_sort(a_list):
    if len(a_list) > 1:
        print(a_list)
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        print(left_half)
        print(right_half)




alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
