"""

Basic regex tasks. Write a function that takes in a numeric code of any lenght.
The function will check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

You can assume the input will always be a nuber.

"""

import unittest

def validate_code(code):
    valids = ["1", "2", "3"]
    # if str(code)[0] in valids:
    #     return True
    # else:
    #     return False
    return True if str(code)[0] in valids else False



class TestCase(unittest.TestCase):

    def test_validate_code(self):
        self.assertEqual(validate_code(123), True)
        self.assertEqual(validate_code(523), False)


if __name__ == "__main__":
    unittest.main()
