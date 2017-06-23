"""

It's pretty straightforward.
Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter.


Test.describe("Tests")
Test.assert_equals(remove_char('eloquent'), 'loquen')
Test.assert_equals(remove_char('country'), 'ountr')
Test.assert_equals(remove_char('person'), 'erso')
Test.assert_equals(remove_char('place'), 'lac')
Test.assert_equals(remove_char('ok'), '')


"""


import unittest

def remove_char(s):
    return s[1:len(s) - 1]



class Test(unittest.TestCase):
    def test_remove_char(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')



if __name__ == '__main__':
    # result = remove_char('eloquent')
    # print(result)
    unittest.main()
