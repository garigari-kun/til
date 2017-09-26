"""

8kyu
One's and Zero's


Given an array of one's and zero's convert
the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11


"""

def binary_array_to_number(arr):
    binary = ''.join(str(n) for n in arr)
    return int(binary, 2)



print(binary_array_to_number([0,0,0,1]))
print(binary_array_to_number([0,0,1,0]))
print(binary_array_to_number([1,1,1,1]))
