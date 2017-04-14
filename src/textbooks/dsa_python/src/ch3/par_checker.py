"""




"""

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items.append(new_item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()


def paran_checker(symbol):
    stack = Stack()
    balanced = True
    index = 0

    while index < len(symbol) and balanced:
        s = symbol[index]
        if s == '(':
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()

        index = index + 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


def paran_checker_myver(symbol):
    if not len(symbol):
        return False

    stack = Stack()
    balanced = True
    for s in symbol:
        if s == '(':
            stack.push(s)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()

    if balanced and stack.is_empty():
        return True
    else:
        return False



if __name__ == '__main__':
    # print(paran_checker('((()))'))
    # print(paran_checker('(()'))
    print(paran_checker_myver('((()))'))
    print(paran_checker_myver('(()'))
