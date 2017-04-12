"""

Stack

is_empty: Return if the stack is empty
push: Append the new item
pop: Remove the last item
peek: Returns the last item but not remove it
size: Returns the size of the stack



"""

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items.append(new_item)

    def is_empty(self):
        return self.items == []

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push('4')
    stack.push('dog')
    print(stack.is_empty())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
