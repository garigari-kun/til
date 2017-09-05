import unittest




def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None



class Test(unittest.TestCase):

    test_list = [1, 3, 5, 7, 9]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.test_list, 3), 1)
        self.assertEqual(binary_search(self.test_list, -1), None)



if __name__ == '__main__':
    unittest.main()
    # binary_search([1, 3, 5, 7, 9], 3)
