"""


Given a string of digits,
you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.


"""


def fake_bin(x):
    fakebin = ''
    for n in x:
        if int(n) < 5:
            fakebin += '0'
        else:
            fakebin += '1'

    return fakebin
