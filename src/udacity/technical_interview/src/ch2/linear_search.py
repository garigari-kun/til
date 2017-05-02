
def linear_search(a_list, item):

    found = False
    pos = 0

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def linear_search_mine(a_list, item):
    found = False
    for num in a_list:
        if num == item:
            found = True

    return found



test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(linear_search(test_list, 3))
print(linear_search(test_list, 13))
print(linear_search_mine(test_list, 3))
print(linear_search_mine(test_list, 13))
