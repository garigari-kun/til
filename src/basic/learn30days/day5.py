
def parse_lists(items):
    str_items = []
    int_items = []

    for item in items:
        if isinstance(item, int) or isinstance(item, float):
            int_items.append(item)
        elif isinstance(item, str):
            str_items.append(item)
        else:
            pass

    return str_items, int_items

def my_sum(items):
    total = 0
    for item in items:
        if isinstance(item, int) or isinstance(item, float):
            total += item
    return total

def count_items(items):
    total = 0
    for item in items:
        if isinstance(item, int) or isinstance(item, float):
            total += 1
    return total

def my_avg(items):
    the_sum = my_sum(items)
    num_of_items = count_items(items)
    return the_sum / (num_of_items * 1.0)



if __name__ == '__main__':
    items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]
    print(parse_lists(items))
