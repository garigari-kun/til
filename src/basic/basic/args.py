
def simple(*args):
    print(args)

def simple2(a, *args):
    print(args)

def simple3(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    simple(1, 2, 3)
    simple2(1, 2, 3)
    simple3(x = 1, y = 2)
