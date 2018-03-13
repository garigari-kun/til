"""

An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case


"""

import unittest

def is_isogram(string):
    lower_string = string.lower()
    char_dict = {}
    for c in lower_string:
        if c in char_dict:
            return False
        else:
            char_dict[c] = True
    return True



class TestCase(unittest.TestCase):

    def test_is_isogram(self):
        self.assertEqual(is_isogram('Dermatoglyphics'), True)


if __name__ == '__main__':
    unittest.main()
