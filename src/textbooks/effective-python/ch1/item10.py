"""

Prefer enumerate over range

"""

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i



flavor_list = ['Vanila', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(flavor)



for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('{}: {}'.format(i + 1, flavor))


""" Better way """
for i, flavor in enumerate(flavor_list):
    print('{}: {}'.format(i + 1, flavor))


"""

Make this even shorter by specifying the number from
which enumerate should begin counting

"""
