"""

A string is considered to be in title case if each word in the string is either (a) capitalised
(that is, only the first letter of the word is in upper case) or (b)
considered to be an exception and put entirely into lower case unless it is the first word,
which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string --
it should behave in the same way even if the case of the minor word string is changed.

###Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
###Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
###Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'


"""



def title_case(title, minor_words=''):
    if not title:
        return ''

    title_words_list = title.split(' ')
    # minor_words_list = minor_words.split(' ')
    if minor_words:
        minor_words_list = [x.lower() for x in minor_words.split(' ')]
    else:
        minor_words_list = []
    title_case_list = []

    for index, t_word in enumerate(title_words_list):
        if index == 0:
            t_str = t_word[0].capitalize() + t_word[1:].lower()
            title_case_list.append(t_str)
        else:
            if t_word.lower() in minor_words_list:
                title_case_list.append(t_word.lower())
            else:
                t_str = t_word[0].capitalize() + t_word[1:].lower()
                title_case_list.append(t_str)

    return ' '.join(title_case_list)


if __name__ == '__main__':
    print(title_case('a clash of KINGS', 'a an the of'))
    print(title_case('THE WIND IN THE WILLOWS', 'The In'))
    print(title_case('the quick brown fox'))
