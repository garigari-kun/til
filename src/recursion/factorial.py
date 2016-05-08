'''
Base on cs50 short video.
'''

def fact_iter(n):
    if n == 1:
        return 1
    accumulator = 1
    for i in range(n, 0, -1):
        accumulator = accumulator * i
    return accumulator

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)






if __name__ == '__main__':
    n = 5
    result = fact_iter(n)
    result2 = fact(n)
    print('fact by iter: {}'.format(result))
    print('fact: {}'.format(result2))
