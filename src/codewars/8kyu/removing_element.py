"""

8kyu
Removing Elements


Take an array and remove every second element out of that array.
Always keep the first element and start removing with the next element.

Example:

my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
None of the arrays will be empty, so you don't have to worry about that!


"""

def remove_every_other(my_list):
    counter = 1
    new_list = []
    for i, elm in enumerate(my_list):
        if counter % 2 != 0:
            new_list.append(elm)
        counter += 1
    return new_list

"""
One linear
"""
def remove_every_other2(my_list):
    return my_list[::2]



print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
