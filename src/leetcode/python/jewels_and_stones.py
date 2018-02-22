import unittest


def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    unique_j = set(J)
    count = 0
    for s in S:
        if s in unique_j:
            count += 1
    return count


class Test(unittest.TestCase):

    def testNumJewelsInStones(self):
        self.assertEquals(numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEquals(numJewelsInStones("z", "ZZ"), 0)



if __name__ == "__main__":
    unittest.main()
