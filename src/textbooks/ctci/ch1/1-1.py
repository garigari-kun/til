"""

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structure?

"""


import unittest



def check_if_unique_str(st):
    return len(set(st)) == len(list(st))


def check_if_unique_str_no_ds(st):
    for ch in st:
        if st.count(ch) > 1:
            return False

    return True


def check_if_unique_str_no_ds2(st):
    for index, ch in enumerate(st):
        if ch in st[index+1:]:
            return False

    return True



class Test(unittest.TestCase):

    TEST_DATA = [
        ['tsuka', True],
        ['test', False],
        ['a', True],
        [' ', True],
        ['  ', False],
    ]

    def test_check_if_uniuque_str(self):
        for st, expected_result in self.TEST_DATA:
            self.assertEqual(check_if_unique_str(st), expected_result)
            self.assertEqual(check_if_unique_str_no_ds(st), expected_result)
            self.assertEqual(check_if_unique_str_no_ds2(st), expected_result)






if __name__ == "__main__":
    unittest.main()
    # test1 = 'tsuka'
    # test2 = 'test'
    #
    # print(check_if_unique_str(test1))
    # print(check_if_unique_str(test2))
    #
    # print(check_if_unique_str_no_ds(test1))
    # print(check_if_unique_str_no_ds(test2))
    #
    # print(check_if_unique_str_no_ds2(test1))
    # print(check_if_unique_str_no_ds2(test2))
