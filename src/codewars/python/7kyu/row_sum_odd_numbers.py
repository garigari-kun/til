"""

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8



"""




def row_sum_odd_numbers(n):
    odd_number_count = sum([i for i in range(n, 0, -1)])
    odd_numbers = []
    counter = 1
    while odd_number_count > 0:
        odd_numbers.append(counter)
        counter += 2
        odd_number_count -= 1

    return sum(odd_numbers[-n:])




if __name__ == '__main__':
    print(row_sum_odd_numbers(2))
    print(row_sum_odd_numbers(4))
