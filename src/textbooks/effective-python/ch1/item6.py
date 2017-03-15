"""
somelist[start:end:stride]

This lets us take every nth item when slicing a sequence


"""


a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)



x = b'mongoose'
y = x[::-1]
print(y)


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])

print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])


"""

Avoid using stride along with start and end indexes.



"""
b = a[::2]
c = b[1:-1]
