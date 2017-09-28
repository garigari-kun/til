"""

Have you heard about the myth that if you fold a paper enough times,
you can reach the moon with it? Sure you do, but exactly how many? Maybe it's time to write a program to figure it out.

You know that a piece of paper has a thickness of 0.0001m.
Given distance in units of meters, calculate how many times you have to fold the paper to make the paper reach this distance.
(If you're not familiar with the concept of folding a paper: Each fold doubles its total thickness.)

Note: Of course you can't do half a fold. You should know what this means ;P

Also, if somebody is giving you a non-positive distance, it's clearly bogus and you should yell at them by returning null (or whatever equivalent in your language).



Test.describe("Basic tests")
Test.assert_equals(fold_to(384000000),42)
Test.assert_equals(fold_to(0.00005),0)
Test.assert_equals(fold_to(-1),None)


"""


def fold_to(distance):
    thickness = 0.0001
    fold_count = 0
    if distance <= 0:
        return None

    while thickness < distance:
        thickness *= 2
        fold_count += 1

    return fold_count






if __name__ == '__main__':
    print(fold_to(384000000))
    print(fold_to(0.00005))
    print(fold_to(-1))
