"""

7kyu
Credit Card Mask


Usually when you buy something,
you're asked whether your credit card number,
phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples


maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"



"""

import unittest


# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc

    first_half = cc[:len(cc) - 4]
    last_four = cc[-4:]

    return ('#' * len(first_half)) + last_four



class Test(unittest.TestCase):
    def test_maskify(self):
        self.assertEqual(maskify("Skippy"), "##ippy")
        self.assertEqual(maskify("Nananananananananananananananana Batman!"), "####################################man!")
        self.assertEqual(maskify("1"), "1")
        self.assertEqual(maskify("1234"), "1234")
        self.assertEqual(maskify(""), "")






if __name__ == '__main__':
    # result1 = maskify("Skippy")
    # result2 = maskify("Nananananananananananananananana Batman!")
    # result3 = maskify("1")
    # result3 = maskify("1234")
    # print(result1)
    # print(result2)
    # print(result3)
    unittest.main()
