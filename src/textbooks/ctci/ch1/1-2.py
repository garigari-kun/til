"""

Implement a function reverse which reverses a null-terminated string.


"""


import unittest


def reverse_recursion(st):
    if st != "":
        return st[-1:] + reverse_recursion(st[:-1])
    else:
        return ""


def reverse_st(st):
    return st[::-1]




class TEST(unittest.TestCase):

    TEST_DATA = [
        ['test', 'tset'],
        ['tsukamoto keisuke', 'ekusiek otomakust'],
        ['', ''],
        ['     ', '     ']
    ]

    def test_both_reverse(self):
        for s, expected in self.TEST_DATA:
            self.assertEqual(reverse_recursion(s), expected)
            self.assertEqual(reverse_st(s), expected)



if __name__ == "__main__":
    unittest.main()
