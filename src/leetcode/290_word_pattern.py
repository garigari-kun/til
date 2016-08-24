"""

290, Word Pattern

Given a pattern and a string str,
find if str follows the same pattern.

Here follow means a full match,
such that there is a bijection
between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.


"""




class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != self.str_count(str):
          return False

        wp = {}
        pw = {}
        for p, w in zip(pattern, self.sep_str(str)):
          if w not in wp and p not in pw:
            wp[w] = p
            pw[p] = w
          elif w not in wp or wp[w] != p:
            return False
        return True

    def str_count(self, str):
        sep_str = str.split()
        return len(sep_str)

    def sep_str(self, str):
      return str.split()



Solution().wordPattern('abba', 'dog cat cat dog')
