

def iterate(x):
    for i in range(x):
        yield i

def generator1():
    a = iterate(10)
    print(next(a))
    print(next(a))
    print(next(a))

def reverse(seq):
    for i in range(len(seq) - 1, -1, -1):
        yield seq[i]

def generator2():
    for c in reverse('awesome'):
        print(c)

if __name__ == '__main__':
    generator1()
    generator2()
