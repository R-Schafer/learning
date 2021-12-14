import animals

class Elephant:
    def __init__(self, z):
        self.z = z

    def speak(self):
        print(f"{self.z} blows his trunk!")

elephant = Elephant("Dumbo")
animals.animal_speak(elephant)