class Dog:
    def __init__(self, x):
        self.x = x

    def speak(self):
        print(f"{self.x} woofs!")


class Cat:
    def __init__(self, y):
        self.y = y

    def speak(self):
        print(f"{self.y} meows!")

def animal_speak(animal):
    animal.speak()

dog1 = Dog("Honey")
cat1 = Cat("Mittens")

animal_speak(dog1)
animal_speak(cat1)