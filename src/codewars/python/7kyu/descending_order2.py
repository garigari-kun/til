"""

Your task is to make a function that can take any non-negative integer as a argument and return it with it's digits in descending order.
 Essentially, rearrange the digits to create the highest possible number.

Examples:

Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221


"""


def Descending_Order(num):
    if num <= 10:
        return num

    num_list = [int(n) for n in str(num)]
    sorted_num_list = sorted(num_list, reverse=True)

    result = ''.join([str(n) for n in sorted_num_list])
    return int(result)


if __name__ == '__main__':
    print(Descending_Order(0))
    print(Descending_Order(15))
    print(Descending_Order(123456789))
