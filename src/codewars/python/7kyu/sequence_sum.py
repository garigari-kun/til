"""

Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0

Examples

sequenceSum(2,2,2) === 2
sequenceSum(2,6,2) === 12 // 2 + 4 + 6
sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequenceSum(1,5,3) === 5 // 1 + 4


"""

import unittest

def sequence_sum(begin_number, end_number, step):
    seq_sum = 0
    for i in range(begin_number, end_number+1, step):
        seq_sum += i
    return seq_sum


class TestCase(unittest.TestCase):

    def test_sequence_sum(self):
        self.assertEqual(sequence_sum(2, 2, 2), 2)
        self.assertEqual(sequence_sum(2, 6, 2), 12)
        self.assertEqual(sequence_sum(1, 5, 1), 15)



if __name__ == "__main__":
    unittest.main()
