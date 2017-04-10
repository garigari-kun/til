"""
You have a sequence of positive numbers starting with 1, but one number is missing!

Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.

In short: an invalid sequence (a string with non numeric character) must return 1, an already complete (or empty) sequence must return 0; a broken sequence with more than one number missing should return the lowest missing number; otherwise return the missing number.


"""

import string

def find_missing_number(sequence):
    invalid_chars = list(string.ascii_letters)
    seq_list = sorted(sequence.split(' '))
    is_completed = False
    for ch in seq_list:
        if ch in invalid_chars:
            return 1







find_missing_number("1 3 2 5")
find_missing_number("1 2 3 4")
find_missing_number("1 5")
find_missing_number("2 1 4 3 a")
