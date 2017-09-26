"""
Remove n exclamation marks in the sentence from left to right. n is positive integer.
"""

def remove(s, n):
    new_s = ''
    for ch in s:
        if n > 0:
            if ch == '!':
                n -= 1
            else:
                new_s += ch
        else:
            new_s += ch
    return new_s


"""
best solution for this problem
"""
def remove1(s, n):
    return s.replace("!", "", n)


remove("Hi!",1)
remove("Hi!",100)
remove("!!!Hi !!hi!!! !hi",5)
