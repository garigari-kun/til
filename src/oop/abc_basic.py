'''
Example of abstract base class in python
'''

class Base(object):
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()


class Concrete(Base):
    def foo(self):
        return 'foo() called'

#c = Concrete()
#print(c.foo())
#print(c.bar())

#b = Base()
#print(b.foo())

'''
The problem is that we can still instatiate Base just fine without
getting an error.
Privide incomlete subclasses, instatiating Concrete will not raise an
error until we call the missing methodo bar()
'''


from abc import ABCMeta, abstractmethod

class BaseVer2(metaclass = ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class ConcreteVer2(BaseVer2):
    def foo(self):
        pass

c = ConcreteVer2()
