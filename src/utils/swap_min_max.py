def swap_min_max(container):
    if len(container) <= 1:
        return container

    min_pos = max_pos = 0
    min_val = max_val = container[0]

    for i in range(1, len(container)):
        if container[i] < min_val:
            min_val = container[i]
            min_pos = i
        if container[i] > max_val:
            max_val = container[i]
            max_pos = i
    container[min_pos], container[max_pos] = max_val, min_val

    return container


container = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(swap_min_max(container))
