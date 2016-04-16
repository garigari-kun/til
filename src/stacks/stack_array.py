'''
LIFO stack implementation
'''

class Empty(Exception):
    pass

class Stack(object):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def display(self):
        return self._data


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    top = stack.peek()
    removed = stack.pop()
    print(stack.display())
    print(removed)
