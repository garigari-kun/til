import unittest

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)



class Test(unittest.TestCase):

    TEST_DATA = [
        [[16, 8, 4, 42, 23, 15], [4, 8, 15, 16, 23, 42]]
    ]

    def test_merge_sort(self):
        for test, result in self.TEST_DATA:
            self.assertEqual(merge_sort(test), result)



if __name__ == "__main__":
    unittest.main()
