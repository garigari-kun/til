"""

Avoid else blocks after for and while loops

"""

for i in range(3):
    print('Loop: {}'.format(i))
else:
    print('else block')


for i in range(3):
    print('Loop: {}'.format(i))
    if i == 1:
        break
else:
    print('Else block')



for x in []:
    print('Never runs')
else:
    print('For else block')




while False:
    print('Never runs')
else:
    print('While else block')



a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print(i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True
