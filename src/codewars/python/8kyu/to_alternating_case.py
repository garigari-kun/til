"""


altERnaTIng cAsE <=> ALTerNAtiNG CaSe

Define to_alternating_case(char*) such that
each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

char source[] = "hello world";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: HELLO WORLD
char source[] = "HELLO WORLD";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: hello world
char source[] = "HeLLo WoRLD";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: hEllO wOrld


"""



def to_alternating_case(string):
    alt_str = ''
    for s in string:
        if s.islower():
            alt_str += s.upper()
        elif s.isupper():
            alt_str += s.lower()
        else:
            alt_str += s

    return alt_str

if __name__ == '__main__':
    print(to_alternating_case("hello world"))
