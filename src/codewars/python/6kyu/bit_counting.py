"""

Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case



"""


def countBits(n):
    bin_n = bin(n)[2:]
    s_of_one = bin_n.replace('0', '')
    return int(len(s_of_one))



if __name__ == '__main__':
    print(countBits(1234))
