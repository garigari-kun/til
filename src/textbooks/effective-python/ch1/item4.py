from urllib.parse import parse_qs


my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))


print('Red: {}'.format(my_values.get('red')))
print('Green: {}'.format(my_values.get('green')))
print('Opacity: {}'.format(my_values.get('opacity')))


red = int(my_values.get('red', [''])[0] or 0)
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print(red)
print(green)
print(opacity)



"""

This is hard to read....

"""
red = int(my_values.get('red', [''])[0] or 0)

"""

Better

"""
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0


"""

Better for reading

"""
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0


"""

Writing helper class

"""
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


green = get_first_int(my_values, 'green')
print('Green: {}'.format(green))
