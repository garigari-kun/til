
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleting_element = self.head
            self.head = self.head.next
            deleting_element.next = None
        else:
            return None


    def get_position(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None

        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1

        return None


    def insert(self, new_element, position):
        current = self.head
        counter = 1
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = current
            self.head = new_element


    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.li.insert_first(new_element)

    def pop(self):
        return self.li.delete_first()
