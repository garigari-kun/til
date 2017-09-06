
def rec_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + rec_sum(arr[1:])



if __name__ == '__main__':
    print(rec_sum([2, 3, 4]))
