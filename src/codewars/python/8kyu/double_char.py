"""


Given a string,
ou have to return a string in which each character (case-sensitive) is repeated once.


double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "


"""


import unittest


def double_char(s):
    result = ''
    for c in s:
        result = result + c + c
    return result


class Test(unittest.TestCase):
    def test_double_char(self):
        self.assertEqual(double_char("String"), "SSttrriinngg")
        self.assertEqual(double_char("Hello World"), "HHeelllloo  WWoorrlldd")
        self.assertEqual(double_char("1234!_ "), "11223344!!__  ")


if __name__ == '__main__':
    # double_char('String')
    unittest.main()
