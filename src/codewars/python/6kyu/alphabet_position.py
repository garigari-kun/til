"""

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.



"""

import string


def alphabet_position(text):
    alphabets = list(string.ascii_letters)
    pos_list = []
    for ch in text:
        if ch in alphabets:
            pos = alphabets.index(ch.lower())
            # index is started at 0 so need to add 1 for pos index
            pos_list.append(str(pos+1))

    return ' '.join(pos_list)



if __name__ == '__main__':
    print(alphabet_position("The sunset sets at twelve o' clock."))
