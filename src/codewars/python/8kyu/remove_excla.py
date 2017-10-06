"""

Description:

Remove a exclamation mark from the end of string.
For a beginner kata, you can assume that the input data is always a string, no need to verify it.

Examples

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi!!"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"


"""


def remove(s):
    if not len(s):
        return ''
        
    if s[-1] == '!':
        if len(s) > 1:
            return s[:len(s)-1]
        else:
            return ''
    else:
        return s



if __name__ == '__main__':
    print(remove('Hi!'))
    print(remove('!Hi'))
    print(remove('!'))
    print(remove(''))
