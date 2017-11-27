"""

- Know the difference between bytes, str and unicode


python2
str: raw 8bit values
unicode: Unicode characters

python3
bytes: raw 8bit values
str: Unicode characters




"""


# python3

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value



if __name__ == '__main__':
    test_bytes1 = to_bytes('Hello')
    test_bytes2 = to_bytes('こんにちは')
    test_str1 = to_str(test_bytes1)
    test_str2 = to_str(test_bytes2)
    print(test_bytes1)
    print(test_bytes2)

    print(test_str1)
    print(test_str2)
