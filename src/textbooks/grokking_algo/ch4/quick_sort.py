import unittest


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)



class Test(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([2, 4, 1, 8, 6]), [1, 2, 4, 6, 8])




if __name__ == '__main__':
    # print(quick_sort([2, 4, 1, 8, 6]))
    unittest.main()
