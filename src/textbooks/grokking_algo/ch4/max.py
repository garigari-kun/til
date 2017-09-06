
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        submax = max(list[1:])
        return list[0] if list[0] > submax else submax



if __name__ == '__main__':
    print(max([1, 2, 3, 4]))
