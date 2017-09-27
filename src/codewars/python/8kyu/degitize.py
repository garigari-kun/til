"""

Convert number to reversed array of digits

Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:

348597 => [7,9,5,8,4,3]



"""


def digitize(n):
    num_list = []
    for i in reversed(str(n)):
        num_list.append(int(i))

    return num_list


if __name__ == '__main__':
    print(digitize(348597))
