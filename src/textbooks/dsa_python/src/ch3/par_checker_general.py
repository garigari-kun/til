
class Stack(object):

    def __init__(self):
        self.container = []

    def is_empty(self):
        return self.container == []

    def push(self, new_value):
        self.container.append(new_value)

    def pop(self):
        return self.container.pop()


def check_matched(open ,close):
    openings = '([{'
    closings = ')]}'
    return openings.index(open) == closings.index(close)


def par_checker_general(symbol):
    stack = Stack()
    balanced = True
    openings = '([{'

    for s in symbol:
        if s in openings:
            stack.push(s)
        else:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                is_matched = check_matched(top, s)
                if not is_matched:
                    return False

    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    # print(paran_checker('((()))'))
    # print(paran_checker('(()'))
    print(par_checker_general('{{([][])}()}'))
    print(par_checker_general('[{()]'))
