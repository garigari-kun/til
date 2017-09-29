"""

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.


"""

def add_binary(a,b):
    bin_ans = bin(a + b)
    return bin_ans[2:]


if __name__ == '__main__':
    print(add_binary(1, 1))
