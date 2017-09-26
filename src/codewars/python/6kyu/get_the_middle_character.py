"""

6kyu
Get the Middle Character


You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.

Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
Input

A word (string) of length 0 < str < 1000

Output

The middle character(s) of the word represented as a string.


"""
def get_middle(s):
    length_s = len(s)
    if length_s % 2 == 0:
        # even
        s_point = int((length_s / 2) - 1)
        return s[s_point:s_point + 2]
    else:
        # odd
        s_point = int((length_s - 1) / 2)
        return s[s_point]




print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("A"))
