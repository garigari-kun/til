"""

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


"""

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


def primeFactors(n):
    pf_list = []
    divider = 2
    while n // 2 > 1:
        while n % divider == 0:
            pf_list.append(divider)
            n = n // divider
        divider += 1


    if pf_list:
        formula = ''
        count_pf_list = OrderedCounter(pf_list)
        key_list = set(pf_list)
        key_list = sorted(key_list)
        for key in key_list:
            if count_pf_list[key] > 1:
                formula += '(' + str(key) + '**' + str(count_pf_list[key]) + ')'
            else:
                formula += '(' + str(key) + ')'

        return formula







if __name__ == '__main__':
    primeFactors(86240)
