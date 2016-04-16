from collections import OrderedDict

def ordered_dict_example():
    '''
    Demonstrate how normal dict and ordered dict works
    '''
    pairs = [('a', 1), ('b', 2), ('c', 3)]

    plain_dict = {}
    for key, value in pairs:
        if key not in plain_dict:
            plain_dict[key] = []
            plain_dict[key].append(value)
    for key, value in plain_dict.items():
        print('{} : {}'.format(key, value))

    ordered_dict = OrderedDict(pairs)
    for key, value in ordered_dict.items():
        print('{} : {}'.format(key, value))


if __name__ == '__main__':
    ordered_dict_example()
