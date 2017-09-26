"""

7kyu
Descending Order


Your task is to make a function that can take any non-negative integer
as a argument and return it with it's digits in descending order.
Descending order means that
you take the highest digit and place the next highest digit immediately
after it.

Examples:

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221


"""
def Descending_Order(num):
    num_list = [int(n) for n in str(num)]
    sorted_num_list = sorted(num_list, reverse=True)
    return int(''.join(str(n) for n in sorted_num_list))





print(Descending_Order(0))
print(Descending_Order(123456789))
print(Descending_Order(15))
