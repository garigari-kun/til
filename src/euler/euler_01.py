'''
euler problem01

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def euler_pro01():
    range_last = 1000
    accumulator = 0
    for i in range(1, range_last):
        if i % 3 == 0:
            accumulator += i
        elif i % 5 == 0:
            accumulator += i
    print('Answer is: {}'.format(accumulator))



if __name__ == '__main__':
    euler_pro01()
