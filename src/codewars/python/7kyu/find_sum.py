"""

Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)


"""

import unittest

def find(n):
    three_multi_list = multiply(3, n)
    five_multi_list = multiply(5, n)
    return sum(three_multi_list) + sum(five_multi_list)


def multiply(m, n):
    counter = 1
    num_list = []
    multi = m * counter
    while multi <= n:
        num_list.append(multi)
        counter += 1
        multi = m * counter

    return num_list


class TestCase(unittest.TestCase):

    def test_find(self):
        self.assertEqual(find(10), 33)
        self.assertEqual(find(100), 2418)



if __name__ == "__main__":
    unittest.main()
