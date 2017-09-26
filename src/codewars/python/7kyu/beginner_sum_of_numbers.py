'''
Given two integers, which can be positive and negative,
find the sum of all the numbers between including them too and return it.
If both numbers are equal return a or b.

Note! a and b are not ordered!

Example:
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
'''


def get_sum(a,b):
    if a == b:
        return a

    integer = [a, b]
    s_integer = sorted(integer)
    result = 0
    while s_integer[0] <= s_integer[1]:
        result += s_integer[0]
        s_integer[0] += 1

    return result


def refactored_get_sum(a, b):
    high = max(a, b)
    low = min(a, b)
    return sum(range(min, high + 1))



if __name__ == '__main__':
    get_sum(1, 0)
    get_sum(1, 1)
    get_sum(-1, 2)
    get_sum(2, -1)
