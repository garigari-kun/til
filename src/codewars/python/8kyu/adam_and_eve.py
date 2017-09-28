"""
According to the creation myths of the Abrahamic religions, Adam and Eva were the first Humans to wander the earth.

You have to do God’s job. The creation method must return an array of length 2 containing objects representing Adam and Eva.
The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. 
Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.

"""



class Human(object):
    pass


class Man(Human):
    pass

class Woman(Human):
    pass




def God():
    #code
    adam = Man()
    eva = Woman()
    return [adam, eva]

#code
