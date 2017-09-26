"""
Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


If array is empty, null or None, or if only 1 Element exists, return 0.
Note:In C++ instead null an empty vector is used. In C there is no null. ;-)


-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.
Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.



"""


def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0

    max_index = arr.index(max(arr))
    del arr[max_index]
    min_index = arr.index(min(arr))
    del arr[min_index]

    return sum(arr)



if __name__ == '__main__':
    print(sum_array([6, 2, 1, 8, 10]))
    print(sum_array([1, 1, 11, 2, 3]))
    print(sum_array([-6, 20, -1, 10, -12]))
