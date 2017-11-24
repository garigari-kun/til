
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

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    def add(self, value):
        new_node = Node(value)
        new_node.next = self._root
        self._root = new_node
        self._size += 1
        return True

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
                prev, current_node = self._set_prev_and_current_node(current_node)
        return False

    def _set_prev_and_current_node(self, current_node):
        prev = current_node
        current_node = current_node.next
        return prev, current_node



    def find(self, value):
        current_node = self._root
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False



    def __str__(self):
        node_list = []
        current = self._root
        while current:
            node_list.append(str(current.value))
            current = current.next
        return " -> ".join(node_list)























# end
