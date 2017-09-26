"""

Summation

Write a program that finds the summation of every number between 1 and num.
The number will always be a positive integer greater than 0.

ex.
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

"""

def summation(num):
    result = 0
    for i in range(1, num + 1):
        result += i
    return result
