"""

Your task is to sort a given string.
Each word in the String will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"


Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

"""


import unittest


def order(sentence):
    s_sentence = sentence.split(' ')
    d_sentence = {}
    for word in s_sentence:
        for ch in word:
            if ch.isdigit():
                d_sentence[int(ch)] = word

    return ' '.join(d_sentence.values())



class Test(unittest.TestCase):
    def test_order(self):
        self.assertEqual(order('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')




if __name__ == '__main__':
    # result= order('is2 Thi1s T4est 3a')
    # print(result)
    unittest.main()
