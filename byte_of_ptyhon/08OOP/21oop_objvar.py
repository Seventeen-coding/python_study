#coding=UTF-8

class Robot:
    '''表示有一个带有名字的机器人'''
    population = 0

    def __init__(self,name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def broken(self):
        '''坏掉的'''
        print("{} is being destoryed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        print('Hello, my name is {name}'.format(name = self.name))


    @classmethod
    def how_many(cls):
        '''打印当前人口数量'''
        print("we have {:d} robots.".format(cls.population)) # :d :o :x :f :02d 

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.broken()
droid2.broken()
Robot.how_many()
