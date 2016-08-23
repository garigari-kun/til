"""

5kyu
Simple Pig Latin

Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay

"""

def pig_it(text):
    sep_by_space = text.split()
    modified_words = []
    for word in sep_by_space:
        if len(word) > 1:
            m_word = word[1:] + word[0] + 'ay'
            modified_words.append(m_word)
        else:
            if ord(word[0].lower()) >= 97:
                word = word[0] + 'ay'
            modified_words.append(word)
    return ' '.join(modified_words)
