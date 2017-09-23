"""

You need to write a function that reverses the words in a given string. A word can also fit an empty string.
If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.


reverse('Hello World') == 'World Hello'
reverse('Hi There.') == 'There. Hi'


"""



def reverse(st):
    word_list = st.split(' ')
    b_word_list = []
    for word in reversed(word_list):
        b_word_list.append(word)
    return ' '.join(b_word_list)



if __name__ == '__main__':
    print(reverse('Hello World'))
    print(reverse('Hi There.'))
