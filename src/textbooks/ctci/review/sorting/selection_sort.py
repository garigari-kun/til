import unittest


def find_smallest(a_list):
    smallest = a_list[0]
    smallest_index = 0
    for i in range(1, len(a_list)):
        if a_list[i] < smallest:
            smallest = a_list[i]
            smallest_index = i
    return smallest_index

def selection_sort(a_list):
    sorted_list = []
    for i in range(len(a_list)):
        smallest = find_smallest(a_list)
        sorted_list.append(a_list.pop(smallest))
    return sorted_list


class Test(unittest.TestCase):

    TEST_DATA = [
        [[16, 8, 4, 42, 23, 15], [4, 8, 15, 16, 23, 42]]
    ]

    def test_selection_sort(self):
        for test, result in self.TEST_DATA:
            self.assertEqual(selection_sort(test), result)


if __name__ == '__main__':
    unittest.main()
