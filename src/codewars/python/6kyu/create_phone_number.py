"""

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parenthesis!

"""


def create_phone_number(n):
    if len(n) == 10:
        num_str = ''.join([str(i) for i in n])
        format_ver = '({}) {}-{}'.format(num_str[0:3], num_str[3:6], num_str[6:])
        print(format_ver)
        return '(' + num_str[0:3] + ') ' + num_str[3:6] + '-' + num_str[6:]




if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
