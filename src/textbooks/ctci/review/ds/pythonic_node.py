"""

Creating setter and getter in pythonic way!


"""


class NotPythonicNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value(value)

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.value)


class Node(object):

    def __init__(self, value, next=None):
        self._value = value
        self.next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


if __name__ == '__main__':
    npn1 = NotPythonicNode(1)
    print(npn1.get_value())
    npn2 = NotPythonicNode(2)
    npn1.set_next(npn2)
    print(npn1.get_next())

    print('---------------')
    node1 = Node(1)
    print(node1.value)
    node1.value = 3
    print(node1.value)
