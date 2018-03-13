"""

Write a function called that takes a string of parentheses, and determines
if the order of the parentheses is valid.
The function should return true if the string is valid,
and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis,
input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

"""

import unittest

def valid_parentheses(string):
    paren_stack = []
    valid_parens = "()"
    for c in string:
        if c in valid_parens:
            if c == "(":
                paren_stack.append(c)
            else:
                if len(paren_stack):
                    paren_stack.pop()
                else:
                    return False
    if len(paren_stack):
        return False
    else:
        return True

class TestCase(unittest.TestCase):

    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses(")(()))"), False)


if __name__ == '__main__':
    unittest.main()
