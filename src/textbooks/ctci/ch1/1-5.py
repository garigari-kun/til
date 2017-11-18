"""

Implement a method to perform basic string compression using the counts of
repeated characters.
If the compressed string would not become smaller than the original string,
return the original string


"""


def comp_str(st):
    comp_list = count_same_str(st)
    comp_str = ''.join(comp_list)

    if len(comp_str) > len(st):
        return st
    else:
        return comp_str


def count_same_str(st):
    comp_list = []
    char_count = 0
    prev = ''

    for ch in st:
        if ch == prev:
            char_count += 1
        else:
            if prev != '':
                comp_list.append(prev + str(char_count))
            char_count = 1
        prev = ch

    if prev and char_count:
        comp_list.append(prev + str(char_count))

    return comp_list





if __name__ == '__main__':
    TEST_DATA = [
        ['aabbcaaa', 'a2b2c1a3'],
        ['aaaaa', 'a5'],
        ['', '']
    ]

    for st, expected in TEST_DATA:
        print(comp_str(st))
