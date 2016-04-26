'''
Practice for implementing recursive functions
'''

def factorial(k):
    if k <= 1:
        return 1
    else:
        return k * factorial(k - 1)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def recursive_sum(my_list):
    print(my_list)
    total = 0
    for element in my_list:
        if type(element) == type([]):
            total = total + recursive_sum(element)
        else:
            total = total + element
    return total
