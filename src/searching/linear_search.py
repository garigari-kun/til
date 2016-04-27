def linear_search(container, target):
    if len(container) == 0:
        return False, None

    for (index, value) in enumerate(container):
        if value == target:
            return True, index

    return False, None


container = [8, 5, 6, 4, 3, 2, 9]
target = 8
success, found = linear_search_algorithm(container, target)

if success != False:
    print('target {} is found at index of {}'.format(target, found))
else:
    print('Not Found')
