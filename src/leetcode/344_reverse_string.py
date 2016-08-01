"""

344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".


"""
import unittest

def reverse_string(string):
    """
    :type string: str
    :rtype: str
    """
    reversed_string = ''
    for ch in reversed(string):
        reversed_string += ch
    return reversed_string


class Test(unittest.TestCase):
    """ Test data"""
    test_data = [
        ('hello', 'olleh'),
        ('12345', '54321'),
        ('h1b1a1', '1a1b1h'),
    ]

    def test_reverse_string(self):
        for test, expected_result in self.test_data:
            result = reverse_string(test)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
