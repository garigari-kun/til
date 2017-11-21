"""


class Node
    attributes:
        _value
        _next: None
        _prev: None

    setters:
        value
        next
        prev

    getters:
        value
        next
        prev


"""


class Node(object):

    def __init__(self, value, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = prev
