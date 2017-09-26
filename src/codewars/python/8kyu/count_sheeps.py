"""

Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


"""


def count_sheeps(arrayOfSheeps):
    present = 0
    for status in arrayOfSheeps:
        if status == True:
            present += 1

    return present


def count_sheeps_better_solution(arrayOfSheeps):
  return arrayOfSheeps.count(True)




if __name__ == '__main__':
    arrayOfSheeps = [True,  True,  True,  False,
              True,  True,  True,  True ,
              True,  False, True,  False,
              True,  False, False, True ,
              True,  True,  True,  True ,
              False, False, True,  True ];
    print(count_sheeps(arrayOfSheeps))
