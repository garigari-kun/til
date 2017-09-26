"""

7kyu
Highest and Lowest


In this little assignment
you are given a string of space separated numbers,
and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space,
and highest number is first.



"""

def high_and_low(numbers):
    num_list = numbers.split()
    int_num_list = [int(number) for number in num_list]
    if len(int_num_list) == 1:
        return "{} {}".format(int_num_list[0], int_num_list[0])
    else:
        return "{} {}".format(max(int_num_list), min(int_num_list))


"""
Clever and clean solution that I found
"""
def high_and_low2(numbers):
    nn = [int(n) for n in numbers.split(' ')]
    return "{} {}".format(max(nn), min(nn))

def high_and_low3(numbers):
    nn = map(int, numbers.split(' '))
    return '{} {}'.format(max(nn), min(nn))



print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
print(high_and_low("1 -1"))
print(high_and_low("42"))
