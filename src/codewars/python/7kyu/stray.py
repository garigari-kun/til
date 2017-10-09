"""


You are given an odd-length array of integers, in which all of them are the same,
except for one single number.

Implement the method stray which accepts such array,
and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples:

[1, 1, 2] => 2

[17, 17, 3, 17, 17, 17, 17] => 3


"""

from collections import Counter


def stray(arr):
    c_arr = Counter(arr)
    for n, i in c_arr.items():
        if i == 1:
            return n



if __name__ == '__main__':
    print(stray([1, 1, 2]))
    print(stray([1,1,1,1,1,1,2]))
