"""

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him

Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)

-If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".

-If he doesn't get 10 hoops, return the string "Keep at it until you get it".


test.assert_equals(hoopCount(3),"Keep at it until you get it" )
test.assert_equals(hoopCount(11),"Great, now move on to tricks" )



"""


import unittest



def hoopCount(n):
    if n >= 10:
        return 'Great, now move on to tricks'
    else:
        return 'Keep at it until you get it'



class Test(unittest.TestCase):
    def test_hoopCount(self):
        self.assertEqual(hoopCount(3), "Keep at it until you get it")
        self.assertEqual(hoopCount(11), "Great, now move on to tricks")



if __name__ == '__main__':
    unittest.main()
