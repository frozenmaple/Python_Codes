class Person:
    population=0

    def __init__(self,name):
        self.name=name
        print('Initializing',self.name)
        Person.population +=1
    def __del__(self):
        print('%s say bye'%self.name)
        Person.population -=1
        if Person.population == 0:
            print('I am the last one')
        else:
            print('There are still %d people left.'%Person.population)
    def sayhi(self):
        print('hello,my name is',self.name)
    def howmany(self):
        if Person.population ==1:
            print('I am the last one')
        else:
            print('We have %d persons here'%Person.population)
swaroop = Person('Swroop')
swaroop.sayhi()
swaroop.howmany()

kalam = Person('Abdul Kalam')
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()

del kalam

swaroop.sayhi()
swaroop.howmany()

del swaroop