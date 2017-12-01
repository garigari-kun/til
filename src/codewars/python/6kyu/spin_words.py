"""

Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
 (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
 Spaces will be included only when more than one word is present.


Examples:

spin_words( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spin_words( "This is a test") => returns "This is a test"
spin_words( "This is another test" )=> returns "This is rehtona test"

"""

import unittest


def spin_words(sentence):
    if not sentence:
        return sentence
    words_list = sentence.split(' ')
    returning_words_list = []
    for word in words_list:
        if len(word) >= 5:
            returning_words_list.append(''.join(reversed(word)))
        else:
            returning_words_list.append(word)
    return ' '.join(returning_words_list)


class TestCase(unittest.TestCase):

    def test_spin_words(self):
        self.assertEqual(spin_words("welcome"), "emoclew")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This is a test"), "This is a test")
        self.assertEqual(spin_words("This is another test"), "This is rehtona test")


if __name__ == '__main__':
    unittest.main()
