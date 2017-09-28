"""

In the following 6 digit number:

283910
91 is the greatest sequence of 2 digits.

In the following 10 digit number:

1234567890
67890 is the greatest sequence of 5 digits.

Complete the solution so that it returns the largest five digit number found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.

Adapted from ProjectEuler.net


"""



def solution(digits):
    current_largest = 0
    tmp = ''
    for i, d in enumerate(digits):
        if len(digits[i:]) > 4:
            tmp = digits[i] + digits[i + 1] + digits[i + 2] + digits[i + 3] + digits[i + 4]
            if int(tmp) > current_largest:
                current_largest = int(tmp)
    return current_largest



if __name__ == '__main__':
    print(solution('1234567890'))
