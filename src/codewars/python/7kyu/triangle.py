"""

Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

1st (1)   2nd (3)    3rd (6)
*          **        ***
           *         **
                     *
You need to return the nth triangular number. You should return 0 for out of range values:

  triangular(0)==0,
  triangular(2)==3,
  triangular(3)==6,
  triangular(-10)==0


"""


def triangular_test(n):
    dots = 0
    for i in range(1, n+1):
        dots += i
    return dots


def triangular_test2(n):
    return sum(range(1, n + 1))


def triangular(n):
    if n == 0:
        return 0
    else:
        return n + triangular(n - 1)


if __name__ == '__main__':
    print(triangular(0))
    print(triangular(3))
    print(triangular(10))
