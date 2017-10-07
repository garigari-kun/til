"""


You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20


"""


def positive_sum(arr):
    pos_arr = []
    for n in arr:
        if n > 0:
            pos_arr.append(n)

    return sum(pos_arr)
