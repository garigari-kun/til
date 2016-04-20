

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def encode(string):
    new_string = ''
    for letter in string:
        if letter.lower() in CONSONANTS:
            new_string += letter + 'o' + letter
        else:
            new_string += letter

    return new_string

def decode(string):
    new_string = ''
    skip = 0
    for letter_number in range(0, len(string)):
        if skip == 0:
            new_string += string[letter_number]
            if string[letter_number].lower() in CONSONANTS:
                skip += 2
        else:
            skip -= 1



if __name__ == '__main__':
    test = "I'm speaking funny language."
    print(encode(test))
