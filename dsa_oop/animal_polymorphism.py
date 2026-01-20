class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"
d = Dog()
print(d.make_sound())   
c = Cat()
print(c.make_sound())  
