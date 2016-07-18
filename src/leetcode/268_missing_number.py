"""

268. Missing number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.


"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = -1
        for num in nums:
            if num != previous + 1:
                return previous + 1
            previous = num





test = [0, 1, 3]
result = Solution().missingNumber(test)
print(result)
