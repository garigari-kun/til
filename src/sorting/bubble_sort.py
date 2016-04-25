'''
Implementation of bubble sort
'''

def bubble_sort(container):
    for i in range(len(container)):
        for j in range(len(container) - 1 - i):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
    return container

if __name__ == '__main__':
    unordered_nums = [23, 8, 4, 42, 16, 15]
    ordered_nums = bubble_sort(unordered_nums)
    print('unordered_nums: {}'.format(unordered_nums))
