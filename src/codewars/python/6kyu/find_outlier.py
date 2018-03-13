"""

You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

"""

import unittest

def find_outlier(integers):
    even_list = []
    odd_list = []
    for n in integers:
        if n % 2 == 0:
            even_list.append(n)
        else:
            odd_list.append(n)

    if len(even_list) < len(odd_list):
        return even_list[0]
    else:
        return odd_list[0]


class TestCase(unittest.TestCase):

    def test_find_outlier(self):
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)



if __name__ == "__main__":
    unittest.main()
