import unittest

def bubble_sort(a_list):
    length = len(a_list)
    for i in range(0, length - 1):
        for j in range(0, length - 1 - i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


class Test(unittest.TestCase):

    TEST_DATA = [
        [[16, 8, 4, 42, 23, 15], [4, 8, 15, 16, 23, 42]]
    ]

    def test_bubble_sort(self):
        for test, result in self.TEST_DATA:
            self.assertEqual(bubble_sort(test), result)



if __name__ == "__main__":
    unittest.main()
