"""


Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay


"""


import string


def pig_it(text):
    valid_list = string.ascii_letters
    print(valid_list)
    new_word_list = []
    word_list = text.split(' ')
    for word in word_list:
        if len(word) > 1 or word[0] in valid_list:
            new_word = word[1:] + word[0] + 'ay'
            new_word_list.append(new_word)
        else:
            new_word_list.append(word)
    return ' '.join(new_word_list)



if __name__ == '__main__':
    print(pig_it('Pig latin is cool'))
    print(pig_it('O emporatay oay oresmay !'))
