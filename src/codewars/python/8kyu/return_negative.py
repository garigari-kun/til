'''

In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?


Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes:

The number can be negative already, in which case no change is required.
Zero (0) can't be negative, see examples above.

'''

import unittest



def make_negative(number):
    if number <= 0:
        return number

    answer = number - (number * 2)
    return answer


class Test(unittest.TestCase):
    def test_make_negative(self):
        self.assertEqual(make_negative(42), -42)
        self.assertEqual(make_negative(-9), -9)
        self.assertEqual(make_negative(0), 0)



if __name__ == '__main__':
    unittest.main()
