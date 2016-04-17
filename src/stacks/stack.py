'''
__init__
is_empty
push
pop
peek
size
'''


class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        last_item = len(self.items) - 1
        return self.items[last_item]

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

    def test(self):
        print('First call is_empty')
        print(self.is_empty())
        for i in range(10):
            self.push(i)
        print('After push 10 items')
        self.display()
        print('pop method will be called')
        self.pop()
        self.display()
        print('peek method will be called')
        print(self.peek())
        print('size method')
        print(self.size())
        print('is_empty method')
        print(self.is_empty())




if __name__ == '__main__':
    stack = Stack()
    stack.test()
