"""


My friend John and I are members of the "Fat to Fit Club (FFC)".
John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him:
"Don't worry any more, I will modify the order of the list".
 It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
 Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:

"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight",
 let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9)
 and 180 is before 90 since, having the same "weight" (9) it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.


"""

from collections import OrderedDict

def order_weight(strng):
    if not strng:
        return ''
    weight_list = strng.split(' ')
    ordered_weight_list = OrderedDict()
    weight_rank_list = []
    for index, weight in enumerate(weight_list):
        num_list = [int(n) for n in weight]
        ordered_weight_list[index] = sum(num_list)

    ordered_weight_list = sorted(ordered_weight_list.items(), key=lambda t: t[1])

    for key, value in ordered_weight_list:
        weight_rank_list.append(str(weight_list[key]))

    return ' '.join(weight_rank_list)


if __name__ == '__main__':
    print(order_weight("56 65 74 100 99 68 86 180 90"))
