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


if __name__ == '__main__':
    print(paran_checker('((()))'))
    print(paran_checker('(()'))
