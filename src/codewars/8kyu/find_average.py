"""


Write function avg which calculates average of numbers in given list.



"""

def find_average(array):
    if not len(array):
        return 0

    return sum(array) / len(array)

if __name__ == '__main__':
    print(find_average([ 1, 2, 3 ]))
    print(find_average([]))
