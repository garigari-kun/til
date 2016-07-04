
def check_permutation(string):
    # Checks if a string is permutation of another
    str1, str2 = string[0], string[1]
    if len(str1) == len(str2):
        arr1 = [char for char in str1]
        arr2 = [char for char in str2]
        arr1.sort()
        arr2.sort()
        for index in range(len(arr1)):
            if arr1[index] != arr2[index]:
                return False
        return True
    else:
        return False




test_data = [(['abcd', 'adcb']), (['aaaa', 'bbbb'])]
for data in test_data:
    result = check_permutation(data)
    print(result)
