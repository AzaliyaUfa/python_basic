class Animal:
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("meow")


class Dog(Animal):
    def voice(self):
        print("woof")


class Cow(Animal):
    def voice(self):
        print("moo")


murlok = Cat()
murlok.voice()
rex = Dog()
rex.voice()
milka = Cow()
milka.voice()
