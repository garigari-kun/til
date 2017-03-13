
class Human(object):
    ''' This is a human class '''

    def __init__(self, human_gender='unknown', age=0, mungry_level='peaceful', hunger_level=0):
        self.human_gender = human_gender
        self.age = age
        self.mungry_level = mungry_level
        self.hunger_level = hunger_level

    def set_gender(self):
        self.human_gender = input("Please enter human's gender: ")

    def set_age(self):
        self.age = int(input("Please enter human's age: "))

    def set_hunger_level(self):
        self.hunger_level = int(input("Please enter human's hunger level: "))

    def change_mungry_level(self):
        if 0 <= self.hunger_level < 4:
            self.mungry_level = 'Human is currently peaceful'
        elif 4 <= self.hunger_level < 8:
            self.mungry_level = 'Human is now getting narky'
        elif 8 <= self.hunger_level <= 10:
            self.mungry_level = 'Human is now aggressive! Watch out!'
        return self.mungry_level

    def show_info(self):
        print("Human's info-- Gender: {}, Age: {}, Hunger level: {}, Mungly level: {}".format(
            self.human_gender,
            self.age,
            self.hunger_level,
            self.mungry_level))



if __name__ == '__main__':
    human_a = Human()
    human_a.set_gender()
    human_a.set_age()
    human_a.set_hunger_level()
    human_a.change_mungry_level()
    human_a.show_info()
