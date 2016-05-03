
def balance_par_str_with_stack(pairs):
    i = 0
    stack = []

    if len(pairs) <= 1:
        return False

    while i < len(pairs):
        symbol = pairs[i]
        if pairs[i] == '(':
            stack.append(symbol)
        elif pairs[i] == ')':
            stack.pop()
        i += 1
    return not stack




if __name__ == '__main__':
    result1 = balance_par_str_with_stack('()')
    result2 = balance_par_str_with_stack('(((((((((())))))))))')
    result3 = balance_par_str_with_stack('((()')
    result4 = balance_par_str_with_stack(')')
    result5 = balance_par_str_with_stack('(')

    print('result1: {}'.format(result1))
    print('result2: {}'.format(result2))
    print('result3: {}'.format(result3))
    print('result4: {}'.format(result4))
    print('result5: {}'.format(result5))
