'''
Implementation of insertion sort
'''
def insertion_sort(container):
    for i in range(1, len(container)):
        j = i
        while j > 0 and container[j] < container[j - 1]:
            container[j], container[j - 1] = container[j - 1], container[j]
            print(container)
            j -= 1

    return container



if __name__ == '__main__':
    unordered_nums = [23, 8, 4, 42, 16, 15]
    ordered_nums = insertion_sort(unordered_nums)
    print('ordered_nums: {}'.format(ordered_nums))
