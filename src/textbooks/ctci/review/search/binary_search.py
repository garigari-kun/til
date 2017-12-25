import unittest


def binary_search(container, target):
    low = 0
    high = len(container) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = container[mid]
        if guess == target:
            return True
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


class Test(unittest.TestCase):

    TEST_DATA = [
        [
            [[1, 2, 3, 4, 5], 3],
            True
        ],
        [
            [[1, 2, 3, 4, 5], 8],
            False
        ],
    ]

    def test_binary_search(self):
        for test_data, test_target in self.TEST_DATA:
            self.assertEqual(binary_search(test_data[0], test_data[1]), test_target)






if __name__ == "__main__":
    unittest.main()
