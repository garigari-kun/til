"""

In list complehensions, create a whole new list containing one item for each value in the input sequence.



"""

value = [len(x) for x in open('/tmp/my_file.txt')]
print(value)


"""

In generator expressions, do not materialize the whole output sequence when they are run
Instead, generator expressions evaluate to an iterator that yield one item at a time from the expressions

"""
it = (len(x) for x in open('/tmp/my_file.txt'))
print(it)


roots = ((x, x ** 0.5) for x in it)
print(next(roots))
