"""
"""



class Node(object):

    def __init__(self, value):
        self.data = value
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next



class LinkedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, value):
        temp = Node(value)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, value):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = self.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()


        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
