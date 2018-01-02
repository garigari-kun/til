"""

Stack

"""


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return ', '.join(str(i) for i in self.items)



if __name__ == '__main__':
    s = Stack()
    for i in range(1, 11):
        s.push(i)
    s.pop()
    s.pop()
    print(s)
