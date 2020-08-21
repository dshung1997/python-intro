class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Dog's barking")


class Whale(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Whale's howling")


d = Dog("dog", 13)
w = Whale("whale", 14)

d.speak()
w.speak()
