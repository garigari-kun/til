"""

Prefer enumurator over a range


"""


flavor_list = ['chocolate', 'vanilla', 'pecan', 'strawberry']
for index, flavor in enumerate(flavor_list):
    print("{}: {}.".format(index, flavor))

print('--------------------------\n')

# You can specify the starting number
for index, flavor in enumerate(flavor_list, 1):
    print("{}: {}.".format(index, flavor))
