"""


Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid.
validBraces should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets, and open and closed curly braces.
Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')',
 open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'.

What is considered Valid? A string of braces is considered valid if all braces are matched with the correct brace.
For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.

Examples:
validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true


"""


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []


def is_matched(open_s ,close_s):
    opening = '([{'
    closing = ')]}'

    return opening.index(open_s) == closing.index(close_s)



def validBraces(string):
    if not len(string):
        return False

    opening = '([{'
    closing = ')]}'
    stack = Stack()

    for s in string:
        if s in opening:
            stack.push(s)

        if s in closing:
            if stack.is_empty():
                return False
            else:
                open_s = stack.pop()
                matched = is_matched(open_s, s)
                if not matched:
                    return False

    if stack.is_empty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(validBraces('(){}[]'))
    print(validBraces('[(])'))
    print(validBraces('([{}])'))
