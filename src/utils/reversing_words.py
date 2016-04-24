

def reversing_sentence(sentence):
    return ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    sentence = "Hello! I'm gonna be reversed!"
    reversed_sentence = reversing_sentence(sentence)
    print(reversed_sentence)
