import unittest


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


class Test(unittest.TestCase):
    TEST_DATA = [
        [[16, 8, 4, 42, 23, 15], [4, 8, 15, 16, 23, 42]]
    ]

    def test_quick_sort(self):
        for test, result in self.TEST_DATA:
            self.assertEqual(quick_sort(test), result)


if __name__ == "__main__":
    unittest.main()
