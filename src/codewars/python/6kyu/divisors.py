"""

Create a function named divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself).
If the number is prime return the string '(integer) is prime' (use Either String a in Haskell).

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
You can assume that you will only get positive integers as inputs.

"""


import unittest


def divisors(integer):
    divisor_list = []
    for d in range(2, integer):
        if integer % d == 0:
            divisor_list.append(d)

    if not divisor_list:
        return '{} is prime'.format(integer)
    else:
        return divisor_list


class Test(unittest.TestCase):
    def test_divisors(self):
        self.assertEqual(divisors(15), [3, 5])
        self.assertEqual(divisors(12), [2, 3, 4, 6])
        self.assertEqual(divisors(13), "13 is prime")




if __name__ == '__main__':
    # result1 = divisors(15)
    # result2 = divisors(13)
    # print(result1)
    # print(result2)
    unittest.main()
