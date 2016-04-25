'''
Implementation of selection sort
'''
def selection_sort(container):
    for i in range(len(container)):
        min_pos = i
        for j in range(i + 1, len(container)):
            if container[j] < container[min_pos]:
                min_pos = j
        container[i], container[min_pos] = container[min_pos], container[i]
        print(container)
    return container



if __name__ == '__main__':
    unordered_nums = [23, 8, 4, 42, 16, 15]
    ordered_nums = selection_sort(unordered_nums)
    print('ordered_nums: {}'.format(ordered_nums))
