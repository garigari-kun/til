"""

6kyu
Array.diff

Your goal in this kata is to implement an difference function,
which subtracts one list from another.

It should remove all values from list a,
which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b,
all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]


"""



def array_diff(a, b):
    if not b:
        return a
    elif not a:
        return []

    for num in b:
        while num in a:
            a.remove(num)
    return a


"""
Clever solution that I found from the github
"""
def array_diff(a, b):
    return [x for x in a if x not in b]
