

def recursive(input):
    if input <= 0:
        return input
    else:
        output = recursive(input - 1)
        return output


def list_sum_rec(a_list):
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + a_list[1:]



print(recursive(3))
