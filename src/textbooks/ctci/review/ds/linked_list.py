"""

Linked list

class Node:
    __init__
    get_value
    set_value
    get_next
    set_next

class LinkedList:
    __init__
    add
    get_size
    remove
    find



"""
class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):

    def __init__(self, root=None):
        self.root = None
        self.size = size

    def size(self):
        return self.size

    def add(self, value):
        new_node = Node(value, self.root)
        self.root = new_node
        size += 1

    def remove(self, value):
        current_node = self.root
        prev_node = None

        while current_node:
            if current_node.get_value() == value:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.root = current_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = current_node
                current_node = current_node.get_next()

        return False

    def find(self, value):
        current_node = self.root
        while current_node:
            if current_node.get_value() == value:
                return value
            else:
                current_node = current_node.get_next()

        return False




class PythonicNode(object):

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


class PythonicLinkedList(object):

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
                prev, current_node = self.set_prev_and_current_node(current_node)
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







if __name__ == "__main__":
    pll = PythonicLinkedList()
    pll.add(3)
    pll.add(10)
    pll.add(12)
    pll.add(20)
    print(pll)
    print(pll.size)
    pll.remove(12)
    print(pll)
    print(pll.find(10))
    print(pll.find(100))



















# end
