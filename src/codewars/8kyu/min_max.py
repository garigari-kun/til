"""

Your task is to make two functions, max and min (maximum and minimum in PHP) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples

max([4,6,2,1,9,63,-134,566]) returns 566
min([-52, 56, 30, 29, -54, 0, -110]) returns -110
max([5]) returns 5
min([42, 54, 65, 87, 0]) returns 0


"""


def min(arr):
    current_min = arr[0]
    for i in arr:
        if current_min > i:
            current_min = i
    return current_min

def max(arr):
    current_max = arr[0]
    for i in arr:
        if current_max < i:
            current_max = i
    return current_max
