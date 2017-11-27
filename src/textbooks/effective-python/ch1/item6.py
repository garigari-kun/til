"""

Avoid using start, end and stride in a single slice



"""


a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

odds = a[::2]
even = a[1::2]

print(odds)
print(even)
