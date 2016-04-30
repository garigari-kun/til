from collections import Counter


def is_anagram(s1, s2):
    counter = Counter()

    for i in s1:
        counter[i] += 1

    for i in s2:
        counter[i] -= 1

    for i in counter.values():
        if i:
            return False

    return True

def is_anagram_ver02(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    if sorted_s1 == sorted_s2:
        return True

    return False






result = is_anagram("cat", "aaa")
print(result)

result = is_anagram_ver02("cat", "acs")
print(result)
