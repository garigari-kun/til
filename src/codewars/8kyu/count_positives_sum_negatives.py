'''

Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array


input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
return [10, -65].



'''



import unittest



def count_positives_sum_negatives(arr):
    p_list = []
    n_list = []
    if not len(arr):
        return []

    for num in arr:
        if num > 0:
            p_list.append(num)
        else:
            n_list.append(num)

    count_of_p_list = len(p_list)
    sum_of_n_list = sum(n_list)


    return [count_of_p_list, sum_of_n_list]





class Text(unittest.TestCase):
    def test_count_positives_sum_negatives(self):
        test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
        test2 = []
        self.assertEqual(count_positives_sum_negatives(test1), [10, -65])
        self.assertEqual(count_positives_sum_negatives(test2), [])



if __name__ == '__main__':
    unittest.main()
    # test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    # count_positives_sum_negatives(test1)
