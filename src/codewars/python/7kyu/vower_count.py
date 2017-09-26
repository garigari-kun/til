"""

7kyu
Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.



"""

def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowel_l = 'aeiou'
    vowel_u = 'AEIOU'
    for char in inputStr:
        if char in vowel_l or char in vowel_u:
            num_vowels += 1
    return num_vowels
