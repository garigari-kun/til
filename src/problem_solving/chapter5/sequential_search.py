
def sequential_search(a_list, target):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == target:
            found = True
        else:
            pos = pos + 1
    return found


def ordered_sequential_search(a_list, target):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == target:
            found = True
        else:
            if a_list[pos] > target:
                stop = True
            else:
                pos = pos + 1
    return found



test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))
print('------------------------------------')
ordered_test_list = sorted(test_list)
print(ordered_sequential_search(ordered_test_list, 3))
print(ordered_sequential_search(ordered_test_list, 13))
