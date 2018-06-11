## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## ??
class Dog(Animal):

    def_init_(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def_init_(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def_init_(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def_init_(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self)._init_(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass
## ??
class Salmon(Fish):
    pass
## ??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()


