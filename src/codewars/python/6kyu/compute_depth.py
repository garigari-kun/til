"""

The depth of an integer n is defined to be how many multiples of n it is necessary to compute before all 10 digits
have appeared at least once in some multiple.

example:

let see n=42

Multiple         value         digits     comment
42*1              42            2,4
42*2              84             8         4 existed
42*3              126           1,6        2 existed
42*4              168            -         all existed
42*5              210            0         2,1 existed
42*6              252            5         2 existed
42*7              294            9         2,4 existed
42*8              336            3         6 existed
42*9              378            7         3,8 existed
Looking at the above table under digits column you can find all the digits from 0 to 9,
Hence it required 9 multiples of 42 to get all the digits. So the depth of 42 is 9.
Write a function named computeDepth which computes the depth of its integer argument.
Only positive numbers greater than zero will be passed as an input.


"""

import unittest

def compute_depth(n):
    digits = [i for i in range(0, 10)]
    multip = 1
    while len(digits):
        value = n * multip
        for i in str(value):
            if int(i) in digits:
                digits.remove(int(i))
        multip += 1
    return multip - 1


class TestCase(unittest.TestCase):

    def test_compute_depth(self):
        self.assertEqual(compute_depth(42), 9)
        self.assertEqual(compute_depth(1), 10)



if __name__ == "__main__":
    unittest.main()
