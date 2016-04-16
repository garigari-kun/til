from fractions import Fraction


def rounding_floats(num1, places):
    return round(num1, places)

def float_to_fractions(number):
    return Fraction(*number.as_integer_ratio())

def get_denominator(num1, num2):
    a = Fraction(num1, num2)
    return a.denominator

def get_numerator(num1, num2):
    a = Fraction(num1, num2)
    return a.numerator


if __name__ == '__main__':
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num5 = 6

    print(rounding_floats(num1, num2))
    print(rounding_floats(num1 * 10, num3))
    print(float_to_fractions(num1))
    print(get_denominator(num2, num5))
    print(get_numerator(num2, num5))
