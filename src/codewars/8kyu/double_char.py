"""


Given a string,
ou have to return a string in which each character (case-sensitive) is repeated once.


double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "


"""


def double_char(s):
    print(s)
    for c in s:
        print(c)





if __name__ == '__main__':
    double_char('String')
