def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

x = 0
y = 5
success, result = divide(x, y)
if not success:
    print('Invlaid inputs')
