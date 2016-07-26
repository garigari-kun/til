"""

349. Intersection of two array

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

"""


class Solution(object):
    def intersection(self, num1, num2):
        """
        :type num1: List[int]
        :type num2: List[int]
        :rtype List[int]
        """
        if len(num1) < len(num2):
            return self.intersection(num2, num1)

        lookup = set()
        for n1 in num1:
            lookup.add(n1)

        result = []
        for n2 in num2:
            if n2 in lookup:
                result.append(n2)
                lookup.discard(n2)

        return result






num1 = [1, 2, 2, 1]
num2 = [2, 2]
expected_result = [2, 2]
result = Solution().intersection(num1, num2)
print(result)
