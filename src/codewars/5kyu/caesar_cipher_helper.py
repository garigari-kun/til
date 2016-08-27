"""

5kyu
Caesar Cipher Helper


Write a class that,
when given a string, will return an uppercase string
with each letter shifted forward in the alphabet
by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet
(e.g. punctuation, spaces), simply leave it as is.


"""

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        encoded = ''
        for char in str:
            if char.isalpha():
                new_char = ord(char.lower()) + self.shift
                if new_char > 122:
                    rem = self.shift - (122 - ord(char.lower()))
                    new_char = 97 + (rem - 1)
                encoded += chr(new_char)
            else:
                encoded += char
        return encoded.upper()


    def decode(self, str):
        decoded = ''
        for char in str:
            if char.isalpha():
                new_char = ord(char.lower()) - self.shift
                if new_char < 97:
                    rem = self.shift - (ord(char.lower()) - 97)
                    new_char = 122 - (rem - 1)
                decoded += chr(new_char)
            else:
                decoded += char
        return decoded.upper()



c = CaesarCipher(5)
print(c.encode('Codewars'))
print(c.decode('HTIJBFWX'))
