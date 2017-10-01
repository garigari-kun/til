"""

Implement the function unique_in_order which
takes as argument a sequence
and returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]


"""



def unique_in_order(iterable):
    if isinstance(iterable, list):
        iterable = ''.join([str(i) for i in iterable])

    stack = []
    for ch in iterable:
        if stack != []:
            if stack[-1] != ch:
                stack.append(ch)
        else:
            stack.append(ch)

    # Check
    validated_stack = []
    for s in stack:
        if s.isdigit():
            validated_stack.append(int(s))
        else:
            validated_stack.append(s)

    return validated_stack





if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
    print(unique_in_order('ABBCcAD'))
    print(unique_in_order([1,2,2,3,3]))
