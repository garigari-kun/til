"""

8kyu
Sum without highest and lowest number


Sum all the numbers of the array
except the highest and the lowest element (the value, not the index!).
(Only one element at each edge,
even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


If array is empty or null, or if only 1 Element exists, return 0.
Note: in C++ instead null an empty vector is used.


"""

"""
I did very poorly.
"""

def sum_array(arr):
    if not arr:
        return 0

    if arr:
        arr.remove(max(arr))
    else:
        return 0

    if arr:
        arr.remove(min(arr))
    else:
        return 0

    result = 0
    for num in arr:
        result += num

    return result


"""

Clever solution that I found from the github

"""
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
