
def bad_comparison(seq):
    filtered = []
    for i in seq:
        if i > 4:
            filtered.append(i)
    print(filtered)

def good_comparison(seq):
    filtered = [i for i in seq if i > 4]
    print(filtered)

def another_good_comparison(seq):
    filtered = filter(lambda x: x > 4, seq)
    return filtered

def bad_adding(seq):
    added = []
    for i in range(len(seq)):
        added.append(seq[i] + 3)
    print(added)

def good_adding(seq):
    added = [i + 3 for i in seq]
    print(added)

def another_good_adding(seq):
    added = map(lambda i: i + 3, seq)
    return added


if __name__ == '__main__':
    seq = [3, 2, 5, 2, 6, 7, 134, 1]
    bad_comparison(seq)
    good_comparison(seq)
    another_good_comparison(seq)
    bad_adding(seq)
    good_adding(seq)
    another_good_adding(seq)
