"""

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


"""



def anagrams(word, words):
    s_word = ''.join(sorted(word))
    anagram_words = []
    # Create new list which contains sorted words
    sorted_words = [''.join(sorted(w)) for w in words]
    for index, s_w in enumerate(sorted_words):
        if s_word == s_w:
            anagram_words.append(words[index])

    return anagram_words




if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
