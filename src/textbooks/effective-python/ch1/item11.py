"""


Use zip to process iterators in parallel


"""

from itertools import zip_longest


names = ['Caciliea', 'Lise', 'Marie']
letters = [len(name) for name in names]

print(names)
print(letters)

names.append("Keisuke")


for name, count in zip_longest(names, letters):
    print("{} has {} letters".format(name, count))
