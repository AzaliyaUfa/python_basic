class Animal:

    numOfInstances = 0

    def __init__(self):
        Animal.numOfInstances = Animal.numOfInstances + 1

    def voice(self):
        pass


def print_number_of_created_instances():
    print("Number of created instances =", Animal.numOfInstances)


class Cat(Animal):
    def voice(self):
        return "meow"


class Dog(Animal):
    def voice(self):
        return "woof"


class Cow(Animal):
    def voice(self):
        return "moo"


instances = {Cat(), Dog(), Cow()}

for i in instances:
    print(i.__class__.__name__, "says", i.voice())

print_number_of_created_instances()
