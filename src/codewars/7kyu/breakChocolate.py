"""

Your task is to split the chocolate bar of given dimension n x m into small squares.
Each square is of size 1x1 and unbreakable.
Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break,
but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split).
Input will always be a non-negative integer.


test.assert_equals(breakChocolate(5, 5) , 24)
test.assert_equals(breakChocolate(1, 1) , 0)


"""

import unittest


def breakChocolate(n, m):
    block_counts = n * m
    if block_counts <= 1:
        return 0
    else:
        return block_counts - 1



class Test(unittest.TestCase):
    def test_breakChocolate(self):
        self.assertEqual(breakChocolate(5, 5) , 24)
        self.assertEqual(breakChocolate(1, 1) , 0)


if __name__ == '__main__':
    unittest.main()
