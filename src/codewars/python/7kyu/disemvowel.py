"""

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".


"""


def disemvowel(string):
    vowels = 'aiueoAIUEO'
    removed_list = []

    for s in string:
        if s not in vowels:
            removed_list.append(s)

    return ''.join(removed_list)


if __name__ == '__main__':
    print(disemvowel("This website is for losers LOL!"))
