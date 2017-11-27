"""

Use list comprehensions instead of map and filter


List comrehensions are much clearer compare to zip, filter method unless the list comprehensions have more than two expressions


"""

a = [i for i in range(1, 11)]
print(a)


squares = [x**2 for x in a]
squares_with_map = map(lambda x:x**2, a)
print(squares)
print(list(squares_with_map))

even_squares = [x**2 for x in a if x % 2 == 0]
even_squares_with_map_and_filter = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
print(even_squares)
print(list(even_squares_with_map_and_filter))

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
print(chile_ranks)
rank_dict = {rank: name for name, rank in chile_ranks.items()}
print(rank_dict)
chile_len_set = {len(name) for name in rank_dict.values()}
print(chile_len_set)
