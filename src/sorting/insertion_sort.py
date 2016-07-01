'''
Implementation of insertion sort
'''
def insertion_sort(container):
    for i in range(1, len(container)):
        j = i
        while j > 0 and container[j] < container[j - 1]:
            container[j], container[j - 1] = container[j - 1], container[j]
            j -= 1
    return container

"""
for j = 2 to A.length
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
"""
def insertion_sort_clrs(nums):
    for j in range(1, len(nums)):
        key = nums[j]
        i = j - 1
        while i > 0 and nums[i] > key:
            nums[i + 1] = nums[i]
            i = i - 1
        nums[i + 1] = key
    return nums



if __name__ == '__main__':
    unordered_nums = [23, 8, 4, 42, 16, 15]
    ordered_nums = insertion_sort(unordered_nums)
    print('insertion_sort result : {}'.format(ordered_nums))
    result2 = insertion_sort_clrs(unordered_nums)
    print('insertion_sort_clrs result: {}'.format(result2))
