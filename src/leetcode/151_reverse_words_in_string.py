"""

151. Reverse words in a string

Given s = 'the sky is blue'
Return s = 'blue is sky the'

"""

class Solution(object):

    def reverse_words(self, s):
        """
        :type s: str
        :rtype str
        """
        # new_list_s = []
        # list_s = s.split(' ')
        # for word in reversed(list_s):
        #     new_list_s.append(word)
        list_s = reversed(s.split(' '))
        result = ' '.join(list_s)

        return result





if __name__ == '__main__':
    s = 'the sky is blue'
    expected_result = 'blue is sky the'
    result = Solution().reverse_words(s)
    print(result)
