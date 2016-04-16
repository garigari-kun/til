'''
LIFO stack implementation
'''

class Empty(Exception):
    pass

class Stack(object):

    #-----------------------------------
    class _Node(object):
        __slots__ = '_element', '_next'

        def __init__(self, element = None, next = None):
            self._element = element
            self._next = next

    #----------------------------------

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def peek(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        return value

    def display(self):
        print(self._head)
        print(self._size)
        print(self._head._element)
        print(self._head._next)
