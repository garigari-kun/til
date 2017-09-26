"""

6kyu
Replace With Alphabet Position

Welcome.
In this kata you are required to, given a string,
replace every letter with its position in the alphabet.
If anything in the text isn't a letter,
ignore it and don't return it. a being 1, b being 2, etc.

As an example:
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)

"""

def alphabet_position(text):
    chars = list(text)
    result = ''
    for char in chars:
        if char.isalpha():
            ascii_char = ord(char.lower())
            pos = ascii_char - 97 + 1
            result += '{} '.format(pos)

    return result.strip()
