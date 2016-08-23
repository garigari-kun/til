"""

8kyu
Return Two Highest Values in List

Description:

In this kata, your job is to return the two highest values in a list, this doesn't include duplicates.

When given an empty list, you should also return an empty list, no strings will be passed into the list.

The return should also be ordered from highest to lowest.

If the argument passed isn't a list, you should return false.

Examples:

two_highest([4, 10, 10, 9]) should return [10, 9]

two_highest([]) should return []

two_highest("test") should return False

"""

def two_highest(list):
    li_uniq = []
    if len(list) > 1:
        for num in list:
            if num not in li_uniq:
                li_uniq.append(num)
        li_uniq.sort()
        return [li_uniq[-1], li_uniq[-2]]
    elif len(list) == 1:
        return False
    else:
        return []
