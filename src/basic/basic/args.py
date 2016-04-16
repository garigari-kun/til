
def simple(*args):
    print(args)

def simple2(a, *args):
    print(args)

def simple3(**kwargs):
    print(kwargs)

def simple4(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == '__main__':
    simple(1, 2, 3)
    simple2(1, 2, 3)
    simple3(x = 1, y = 2)
    simple4(1, 2, 3, 4, 5, 6, 7, x = 2, y = 2, name = 'someone')
