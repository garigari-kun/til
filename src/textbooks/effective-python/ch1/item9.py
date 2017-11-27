"""

Consider Generator expression for large list comprehension


"""

# This causes using too much memory and crash the program
values = [len(x) for x in open('largefile.txt')]

# So Use Generator
values = (len(x) for x in open('largefile.txt'))
