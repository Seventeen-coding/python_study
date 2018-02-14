
class Person:
    pass

p = Person()
print(p)

class Person_2:
    def say_hi(self):
        print('Hello')

p = Person_2()
p.say_hi()

class Person_3:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello my name is {name}'.format(name = self.name))

p = Person_3('Swaroop')
p.say_hi()


