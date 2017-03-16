names = ['Cacilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

print(letters)


longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)


"""

Better than before
Using enumerate

"""
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count


"""

zip built in function makes code clearer
zip wraps two or more iterators with a lazy generator.

"""
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count


"""

Issue

it behaves strangely if the input iterators are of different length.
s
"""
