import unittest



def linear_search(container, target):
    for i in container:
        if i == target:
            return True
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

    def test_linear_search(self):
        for test_data, test_target in self.TEST_DATA:
            self.assertEqual(linear_search(test_data[0], test_data[1]), test_target)



if __name__ == "__main__":
    unittest.main()
