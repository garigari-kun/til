
class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def __str__(self):
        return 'data: {} next: {}'.format(self.data, self.next)


"""
insert
size
search
delete
"""

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data is not in the list')
        return current

    def delete(self, data):
        current = self.head
        found = False
        previous = None

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError('Data not in the list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())





node1 = Node()
node2 = Node(1)
node3 = Node()
print(node1)
print(node2)
print(node3)
