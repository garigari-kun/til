
class Deque(object):

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)


def palindrom_checker(string):
    deque = Deque()
    for s in string:
        deque.add_front(s)

    while deque.size() > 1:
        rear = deque.remove_rear()
        front = deque.remove_front()
        if rear != front:
            return False
    return True


if __name__ == '__main__':
    print(palindrom_checker("madam"))
    print(palindrom_checker("keisuke"))
