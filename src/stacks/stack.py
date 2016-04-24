
class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            last_index = len(self.items) - 1
            return self.items[last_index]

    def __repr__(self, *args, **kwargs):
        return '{}'.format(self.items)

class Node(object):

    def __init__(self, value, left_pointer, right_pointer):
        self._value = value
        self._left_pointer = left_pointer
        self._right_pointer = right_pointer

class LinkedStack(object):

    def __init__(self):
        self.top_ptr = None
        self.sz = 0

    def is_empty(self):
        return self.top_ptr == None

    def push(self, item):
        if self.top_ptr is None:
            self.top_ptr = Node(item, None, None)
        else:
            node = Node(item, left_pointer = None, right_pointer = self.top_ptr)
            self.top_ptr._left_pointer = None
            self.top_ptr = node
        self.sz += 1

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            node = self.top_ptr
            self.top_ptr = self.top_ptr._right_pointer
            self.top_ptr._left_pointer = None
            self.sz -= 1
            return node._value

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.top_ptr._value

    def size(self):
        return self.sz

    def __repr__(self, *args, **kwargs):
        rep = '['
        current = self.top_ptr
        while current is not None:
            rep += '{}'.format(current._value)
            current = current._right_pointer
            if current is not None:
                rep += ', '
        rep += ']'
        return rep


if __name__ == '__main__':
    stack = LinkedStack()
    print("Is the stack empty? ", stack.is_empty())
    print("Adding 0 to 10 in the stack...")
    for i in range(10):
        print(i)
        stack.push(i)
    print("Stack size: ", stack.size())
    print("Stack peek : ", stack.peek())
    print("Pop...", stack.pop())
    print("Stack peek: ", stack.peek())
    print("Is the stack empty? ", stack.is_empty())
    print(stack)
