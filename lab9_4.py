class Mammal:
    className = 'Mammal'
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"{self.name} является млекопитающим")
class Dog(Mammal):
    species = 'canine'
    sounds = 'woauw'
    def bark(self):
        print(f"{self.name} лает: {self.sounds}")
class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'
    def meow(self):
        print(f"{self.name} мяукает: {self.sounds}")
dog = Dog("Чапа")
cat = Cat("Мявка")
dog.info()
cat.info()
dog.bark()
cat.meow()