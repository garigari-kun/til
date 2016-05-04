'''
Implementation of binary search
'''

def binary_search(container, target):
    lo = 0
    hi = len(container)

    while lo < hi:
        mid = (hi + lo) // 2
        if container[mid] == target:
            # return True
            return True, mid
        elif container[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return False, 0


if __name__ == '__main__':
    container = [i for i in range(1, 11)]
    target = 8
    success, index = binary_search(container, target)
    if success:
        print('The target value is located at index of : {}'.format(index))
    else:
        print('Not found')
