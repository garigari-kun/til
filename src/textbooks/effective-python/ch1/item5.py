a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print('First four: {}'.format(a[:4]))
print('Last four: {}'.format(a[-4:]))
print('Middle Two: {}'.format(a[3:-3]))


print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])


first_twenty_items = a[:20]
print(first_twenty_items)


"""

In contrast, accessing the same index directly causes an exception

a[20]
"""


b = a[4:]
print('Before: {}'.format(b))
b[1] = 99
print('After: {}'.format(b))
print('No change: {}'.format(a))



print('Before: {}'.format(a))
a[2:7] = [99, 22, 14]
print('After: {}'.format(a))



b = a
print('Before: {}'.format(a))
a[:] = [101, 102, 103]
print('After: {}'.format(a))
print('B: {}'.format(b))
