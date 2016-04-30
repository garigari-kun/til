
class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return 'Queue: {}'.format(self.items)



if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.size())
    print(q.is_empty())
    print(q)
