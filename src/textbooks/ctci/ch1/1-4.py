"""
Replace all spaces in a string with %20
"""

def replace_spaces(st):
    char_list = []

    for ch in st:
        if ch == ' ':
            ch = '%20'
        char_list.append(ch)

    return ''.join(char_list)


if __name__  == "__main__":
    TEST_DATA = [
        ["I am Keisuke Tsukamoto", "I%20am%20Keisuke%20Tsukamoto"]
    ]

    for st, expected in TEST_DATA:
        print(replace_spaces(st) == expected)
