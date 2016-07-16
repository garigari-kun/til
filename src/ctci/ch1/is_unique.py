
def is_unique(string):
    # Let's say characters set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True



if __name__ == '__main__':
    test_words = ['abcd', 'abac', 'abca']
    for test_word in test_words:
        result = is_unique(test_word)
        print(result)
