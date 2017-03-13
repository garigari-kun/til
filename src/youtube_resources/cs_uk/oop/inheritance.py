'''
Inheritance

Classes can inherit other classes.

Human -> Man
      -> Woman

'''


class Human(object):

    def __init__(self, human_gender='human', age=0):
        self.human_gender = human_gender
        self.age = age

    def speak(self):
        print('Hi, I am a {}'.format(self.human_gender))

    def show(self):
        print('Human gender: {}, Age: {}'.format(self.human_gender, self.age))


class Man(Human):

    def __init__(self, hair_color, age):
        #super(Man, self).__init__(self)
        super().__init__(human_gender='Male', age=age)
        self.hair_color = hair_color

    def show(self):
        print('Human gender: {}, Age: {}, Hair color: {}'.format(self.human_gender, self.age, self.hair_color))


if __name__ == '__main__':
    a_man = Man('Brown', 24)
    a_man.show()
    a_man.speak()
