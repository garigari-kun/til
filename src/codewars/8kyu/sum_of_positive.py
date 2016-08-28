"""

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

"""



def positive_sum(arr):
    return sum([n for n in arr if n > 0])



print(positive_sum([1,2,3,4,5]))
print(positive_sum([1,-2,3,4,5]))
print(positive_sum([-1,2,3,4,-5]))
