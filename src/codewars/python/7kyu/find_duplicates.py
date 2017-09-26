

from collections import Counter

def duplicates(array):
    c = Counter(array)
    dup = []
    for key, value in c.items():
        if value > 1:
            dup.append(key)
    return dup


print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']))
print(duplicates([0, 1, 2, 3, 4, 5]))
