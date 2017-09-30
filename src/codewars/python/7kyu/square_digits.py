"""


Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer



"""


def square_digits(num):
    str_num = str(num)
    answer = ''
    for n in str_num:
        squared = int(n) * int(n)
        answer += str(squared)

    return int(answer)



if __name__ == '__main__':
    print(square_digits(9119))
