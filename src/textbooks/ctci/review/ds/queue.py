"""

Queue

- is_empty
- enqueue
- dequeue
- size


"""


class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
