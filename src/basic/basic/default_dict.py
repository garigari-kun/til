from collections import defaultdict

def default_dict_example():
    pairs = {('a', 1), ('b', 2), ('c', 3)}

    normal_dict = {}
    for key, value in pairs:
        if key not in normal_dict:
            normal_dict[key] = []
            normal_dict[key].append(value)
    print(normal_dict)

    default_dict = defaultdict(list)
    for key, value in pairs:
        default_dict[key].append(value)
    print(default_dict)




if __name__ == '__main__':
    default_dict_example()
