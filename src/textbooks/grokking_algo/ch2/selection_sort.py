import unittest




def find_smallest(arr):
    cur_smallest = arr[0]
    cur_smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < cur_smallest:
            cur_smallest = arr[i]
            cur_smallest_index = i

    return cur_smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_index))

    return sorted_arr



class Test(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual(selection_sort([5, 3, 6, 2, 10]), [2, 3, 5, 6, 10])



if __name__ == '__main__':
    # print(selection_sort([5, 3, 6, 2, 10]))
    unittest.main()
