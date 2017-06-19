'''

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
and returns the same string with all even indexed characters in each word upper cased,
and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words.
Words will be separated by a single space(' ').

Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'



'''


def to_weird_case(string):
    s_string = string.split(' ')
    s_word_list = []
    for word in s_string:
        counter = 0
        generated_str = ''
        while counter < len(word):
            if counter % 2 == 0:
                # upper later
                generated_str += word[counter].upper()

            else:
                # lower letter
                generated_str += word[counter].lower()
            counter += 1
        s_word_list.append(generated_str)

    if s_word_list:
        weird_cased_str = ' '.join(s_word_list)

    return weird_cased_str



if __name__ == '__main__':
    to_weird_case('Weird string case')
    to_weird_case('String')
