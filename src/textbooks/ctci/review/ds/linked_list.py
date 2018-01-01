"""

LinkedList


"""


class Node(object):

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

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


class LinkedList(object):

    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def add(self, value):
        new_node = Node(value)
        new_node.next = self._root
        self._root = new_node
        self._size += 1
        return True

    def find(self, value):
        current_node = self._root
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False

    def remove(self, value):
        current_node = self._root
        prev = None
        while current_node:
            if current_node.value == value:
                if prev:
                    prev.next = current_node.next
                else:
                    self._root = current_node.next
                self._size -= 1
                return True
            else:
                prev = current_node
                current_node = current_node.next
        return False

    def find(self, value):
        current_node = self._root
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False




if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(3)
    linked_list.add(10)
    linked_list.add(12)
    linked_list.add(20)
    print(linked_list)
    print(linked_list.size)
    linked_list.remove(12)
    print(linked_list)
    print(linked_list.find(10))
    print(linked_list.find(100))














# end
