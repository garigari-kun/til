"""

6kyu
Format a string of names like 'Bart,Lisa & Maggie'


Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''



"""


import unittest


def namelist(names):
    l_names = len(names)
    concat_str = ''
    if not l_names:
        return ''
    elif l_names == 1:
        return names[0]['name']
    else:
        for count, name in enumerate(names):
            if l_names - 2 == count:
                concat_str = concat_str + name['name'] + ' & '
            elif l_names - 1 == count:
                concat_str = concat_str + name['name']
            else:
                concat_str = concat_str + name['name'] + ', '

    return concat_str


class Test(unittest.TestCase):

    def test_namelist(self):
        self.assertEqual(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
        self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa')
        self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart')
        self.assertEqual(namelist([]), '')






if __name__ == '__main__':
    # result1 = namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
    # result2 = namelist([{'name': 'Bart'},{'name': 'Lisa'}])
    # result3 = namelist([{'name': 'Bart'}])
    # result4 = namelist([])
    #
    # print(result1)
    # print(result2)
    # print(result3)
    # print(result4)

    unittest.main()
