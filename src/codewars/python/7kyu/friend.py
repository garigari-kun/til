"""

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]



"""



def friend(x):
    friend_list = []
    for f in x:
        if len(f) == 4:
            friend_list.append(f)

    return friend_list


if __name__ == '__main__':
    print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
