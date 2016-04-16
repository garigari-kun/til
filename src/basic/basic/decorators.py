
def logger(func):
    def inner(*args):
        print('Arguments were: {}'.format(args))
        return func(*args)
    return inner

@logger
def foo(x, y):
    return x + y

def sum(func):
    s = 0
    for i in func():
        s += i
    return s

@sum
def interate():
    a = []
    for i in range(10):
        a.append(i)
    return a



print(interate)
print(foo(1, 2))
