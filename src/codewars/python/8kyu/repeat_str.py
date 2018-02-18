"""

Write a function called repeatStr which repeats the given string string exactly n times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"


"""

import unittest


def repeat_str(repeat, string):
    repeated_str = ''
    for i in range(repeat):
        repeated_str += string
    return repeated_str



class TestCase(unittest.TestCase):

    def test_repeat_str(self):
        self.assertEqual(repeat_str(6, "I"), "IIIIII")
        self.assertEqual(repeat_str(5, "Hello"), "HelloHelloHelloHelloHello")


if __name__ == "__main__":
    unittest.main()
