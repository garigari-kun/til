"""

7kyu
Count all the sheep on farm in the heights of New Zealand



Every week (Friday and Saturday night), the farmer and his son count amount of sheep returned to the yard of their farm.
They count sheep on Friday night, the same goes for Saturday (suppose that sheep returned on Friday are not feeding back on hills on Saturday).

As sheep are not coming in one flock,
you will be given two arrays (one for each night) representing number of sheep as they were returning to the yard during the evenings
(entries are positive ints, higher than zero).

Farmer and his son know the total amount of their sheep, you will be given this number as third parameter.
Your goal is to calculate the amount of sheep lost (not returned) to the farm after Saturday night counting.


Example 1: Input: {1, 2}, {3, 4}, 15 --> Output: 5

Example 2: Input: {3, 1, 2}, {4, 5}, 21 --> Output: 6


Test.describe("Basic Tests")
test.assert_equals(lostSheep([1,2],[3,4],15),5)
test.assert_equals(lostSheep([3,1,2],[4,5],21),6)
test.assert_equals(lostSheep([5,1,4],[5,4],29),10)


"""


import unittest


def lostSheep(friday,saturday,total):
    total_list = friday + saturday
    sum_of_sheep = sum(total_list)
    return total - sum_of_sheep


class Test(unittest.TestCase):
    def test_lostSheep(self):
        self.assertEqual(lostSheep([1,2],[3,4],15),5)
        self.assertEqual(lostSheep([3,1,2],[4,5],21),6)
        self.assertEqual(lostSheep([5,1,4],[5,4],29),10)


if __name__ == '__main__':
    # lostSheep([1,2],[3,4],15)
    # lostSheep([3,1,2],[4,5],21)
    unittest.main()
