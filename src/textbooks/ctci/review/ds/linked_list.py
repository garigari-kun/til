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
            if current_node.get_value() = value:
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
            if current_node.get_value() = value:
                return value
            else:
                current_node = current_node.get_next()

        return False

















# end
