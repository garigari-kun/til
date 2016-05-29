

def log(message, values):
    if not values:
        print(message)
    else:
        join_str = ', '.join(str(x) for x in values)
        print('{}: {}'.format(message, join_str))

def log2(message, *values):
    if not values:
        print(message)
    else:
        join_str = ', '.join(str(x) for x in values)
        print('{}: {}'.format(message, join_str))


if __name__ == '__main__':
    log('My numbers are', [1, 2, 3, 4, 5])
