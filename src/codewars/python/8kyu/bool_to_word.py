"""

Complete the bool_to_word (Javascript: boolToWord ) method.

Given: a boolean value

Return: a 'Yes' string for true and a 'No' string for false


"""


import unittest

def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'


class Test(unittest.TestCase):
    def test_bool_to_word(self):
        self.assertEqual(bool_to_word(True), 'Yes')
        self.assertEqual(bool_to_word(False), 'No')




if __name__ == '__main__':
    unittest.main()
