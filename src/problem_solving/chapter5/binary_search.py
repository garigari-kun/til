
def binary_search(a_list, target):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if a_list[mid] == target:
            found = True
        else:
            if a_list[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
    return found


def binary_search_rec(a_list, target):
    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
        if a_list[mid] == target:
            return True
        else:
            if a_list[mid] > target:
                return binary_search_rec(a_list[:mid], target)
            else:
                return binary_search_rec(a_list[mid + 1:], target)

    




test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
ordered_test_list = sorted(test_list)
print(binary_search(ordered_test_list, 3))
print(binary_search(ordered_test_list, 13))

print(binary_search_rec(ordered_test_list, 3))
print(binary_search_rec(ordered_test_list, 13))
