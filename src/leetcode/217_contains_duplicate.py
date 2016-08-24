"""

217. Contains Duplicate


Given an array of integers, find if the array contains any duplicates.
Your function should return true
if any value appears at least twice in the array,
and it should return false if every element is distinct.


"""

from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = Counter(nums)
        for key, value in nums_dict.items():
            if value > 1:
                return True
        return False



"""

Clever solution that I found from the github

"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
