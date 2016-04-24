from stack import Stack


def balance_par_str_with_stack(str1):
    s = Stack()
    balanced = True
    index = 0


    while (index < len(str1)) and balanced:
        if str1[index] == '(':
            s.push('(')
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
    print(balance_par_str_with_stack(')('))
