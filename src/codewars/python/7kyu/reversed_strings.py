"""

Complete the solution so that it reverses the string value passed into it.

solution('world') # returns 'dlrow'


"""

import unittest

def solution(string):
    return "".join([c for c in reversed(string)])


class TestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("world"), "dlrow")



if __name__ == "__main__":
    unittest.main()
