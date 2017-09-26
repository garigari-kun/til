"""

Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior")

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")


"""



def to_camel_case(text):
    if not len(text):
        return ''

    result = ''
    word_list = []
    text = text.replace('_', '-')
    if '-' in text:
        word_list = text.split('-')

    print(word_list)

    for index, word in enumerate(word_list):
        if index == 0:
            result += word
        else:
            if word[0].islower():
                result += word[0].capitalize() + word[1:]
            else:
                result += word

    return result


if __name__ == '__main__':
    print(to_camel_case("the-stealth-warrior"))
    print(to_camel_case("The_Stealth_Warrior"))
    print(to_camel_case("The-pippi_was_Hungry"))
