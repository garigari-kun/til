"""

TinyURL is a URL shortening service
 where you enter a URL such as https://leetcode.com/problems/design-tinyurl and
 it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL
and the tiny URL can be decoded to the original URL.

"""

import random
import string


class Codec:

    base_url = "http://tinyurl.com/"
    encode_chars = string.ascii_letters + string.digits

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.encoding_range = 6

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        tiny_url_code = ''
        if longUrl not in self.url_to_code:
            for _ in range(self.encoding_range):
                tiny_url_code += random.choice(self.encode_chars)
            if tiny_url_code not in self.code_to_url:
                self.code_to_url[tiny_url_code] = longUrl
                self.url_to_code[longUrl] = tiny_url_code
        return self.base_url + tiny_url_code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code_to_url[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
codec = Codec()
codec.encode("http://itusiku.io")
# print(codec.encode("http://itsuiku.io"))
