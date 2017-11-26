"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



"""


import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for pos, num in enumerate(nums):
            finding_num = target - num
            for c_pos, c_num in enumerate(nums):
                if pos != c_pos:
                    if c_num == finding_num:
                        return [pos, c_pos]
        return False


class Test(unittest.TestCase):
    TEST_CASE = [
        {
            'par1': [2, 7, 11, 15],
            'par2': 9,
            'expected': [0, 1]
        },
        {
            'par1': [2, 3, 5, 15],
            'par2': 18,
            'expected': [1, 3]
        },
        {
            'par1': [2, 3, 5, 15],
            'par2': 100,
            'expected': False
        }
    ]
    def test_twoSum(self):
        for test in self.TEST_CASE:
            sol = Solution()
            self.assertEqual(sol.twoSum(test['par1'], test['par2']), test['expected'])



if __name__ == '__main__':
    unittest.main()
