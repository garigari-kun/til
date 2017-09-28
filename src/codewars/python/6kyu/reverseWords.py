"""

Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"


"""


def reverseWords(str):
    word_list = str.split(' ')
    reversed_word_list = [word for word in reversed(word_list)]
    return ' '.join(reversed_word_list)



if __name__ == '__main__':
    print(reverseWords('The greatest victory is that which requires no battle'))
